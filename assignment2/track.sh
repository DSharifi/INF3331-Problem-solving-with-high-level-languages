track() {
  #start
  if [[ $1 == 'start' ]]; then
    #wrong arity
    if [[ $3 != '' || $2 == '' ]]; then
      echo "track start takes 1 additional argument. Insert a label as 2nd parameter.
            -track start [label]
            -Example:
            track start task1"
    else
      eval "$1 '$2'"
    fi

  #stop or track
  elif [[ $1 == 'stop' || $1 == 'status' ]]; then
    if [[ $2 != '' ]]; then
      eval wrongArity $1
    else
      eval $1
    fi

  else
    echo "Please provide a proper argument: status, start or stop."
  fi
}

startMessage() {
  echo
}


start() {
  if activeTask; then
    echo "ERROR: A task is already active. Please stop the current task before starting a new one"
  else
    filelocation=$(pwd)"/LOGFILE.txt"
    locDate="$(date '+%a %b %d %H:%M:%S %Z %G')"
    echo "START $locDate">>$(pwd)"/LOGFILE.txt"
    echo "LABEL $1">>$(pwd)"/LOGFILE.txt"
  fi
}


stop() {
  filelocation=$(pwd)"/LOGFILE.txt"
  locDate="$(date '+%a %b %d %H:%M:%S %Z %G')"
  if ! activeTask; then
    echo "No task is active."
  else
    echo "STOP $locDate" >> $filelocation
    echo "" >> $filelocation
  fi
}

status() {
  if activeTask; then
    line="$(tail -1 $(pwd)'/LOGFILE.txt')"
    prefix="LABEL "
    label=${line#$prefix} #Strips "LABEL from the line"
    echo "The task '$label' is currently being tracked"
  else
    echo "No task is active"
  fi
}



wrongArity() {
  echo  "Error: 'track $1' takes no additional args.
  -Example:
  track $1"
}


#checks if any task is active
activeTask() {
  touch LOGFILE.txt
  if  [[ "$(tail -2 $(pwd)"/LOGFILE.txt" | head -1 | awk '{ print $1; }')" == "START" ]]; then
    true
  else
    false
  fi
}
