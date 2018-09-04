LOGFILE="$(pwd)"/LOGFILE.txt""

track() {
  touch $LOGFILE
  #start
  if [[ $1 == 'start' ]]; then
    #wrong arity
    if [[ $3 != '' || $2 == '' ]]; then
      echo "track start takes 1 additional argument. Insert a label as 2nd parameter.
            -track start [label]
            -Example:
            track start task1"
    #run start with arg
    else
      eval "$1 '$2'"
    fi

  #stop, track or log
  elif [[ $1 == 'stop' || $1 == 'status' || $1 == 'log' ]]; then
    if [[ $2 != '' ]]; then
      eval wrongArity $1
    else
      eval $1
    fi
  else
    echo "Please provide a proper argument: status, start, stop or log."
  fi
}

#start
start() {
  if isActive; then
    echo "ERROR: A task is already active. Please stop the current task before starting a new one"
  else
    locDate="$(date '+%a %b %d %H:%M:%S %Z %G')"

    echo "START $locDate" >> $LOGFILE
    echo "LABEL $1" >> $LOGFILE
  fi
}

#stops task
stop() {
  locDate="$(date '+%a %b %d %H:%M:%S %Z %G')"
  if ! isActive; then
    echo "No task is active."
  else
    echo "STOP $locDate">>$LOGFILE
    echo "">>$LOGFILE
  fi
}

#prints out status
status() {
  if isActive; then
    line="$(tail -1 $(pwd)'/LOGFILE.txt')"
    prefix="LABEL "
    label=${line#$prefix} #Strips "LABEL from the line"
    echo "The task '$label' is currently being tracked"
  else
    echo "No task is active"
  fi
}


#error message, for wrong arity for start or stop
wrongArity() {
  echo  "Error: 'track $1' takes no additional args.
  -Example:
  track $1"
}


#checks if a task is active
isActive() {
  if  [[ "$(tail -2 $LOGFILE | head -1 | awk '{ print $1; }')" == "START" ]]; then
    true
  else
    false
  fi
}

#prints out log
log() {
  message=""
  startDate=""
  label=""
  #read every line
  #Store every block in $message with label and duration on a new line.
  while read lines;
  do
    stamp="$(echo $lines | awk '{ print $1; }')"
    if [[ $stamp == "START" ]]; then
      startDate=${lines#"START"}

    elif [[ $stamp == "LABEL" ]]; then
      label=${lines#"LABEL "}

    elif [[ $stamp == "STOP" ]]; then
      stopDate=${lines#"STOP"}
      timeDifference="$(timeDifference $startDate $stopDate)"
      message="$message$label: $timeDifference\n"
    fi
  done < $LOGFILE
  echo $message
}

#Returns time difference in HH:MM:SS for two dates
timeDifference() {
  seconds="$(($(date -d "$2" '+%s') - $(date -d "$1" '+%s')))"
  difference="$(printf '%02d:%02d:%02d\n' $(($seconds / 3600)) $(($seconds % 3600 / 60)) $(($seconds % 60)))"
  echo $difference
}
