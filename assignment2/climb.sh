climb() {
  #climbs one step if no args are given
  mssg='../'
  comm='../'

  #Print out error if arg is not a number
  if ! [[ "$1" =~ ^[0-9]+$ || $1 == '' ]]; then
    echo "Error: climb only accepts positive integers as arguments.
    -Examples:
      - climb 3
      - climb"
    return

  #climb 0. do nothng.
  elif [[ $1 == 0 ]]; then
    return

  #iterator for climb level, if $1 is not an empty string
  elif [ ${1} ]; then
    for ((i = 0; i < $1 - 1; i++));
    do
      mssg=$mssg$comm
    done
  fi
  eval "cd ${mssg}"
}
