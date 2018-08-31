climb() {
  #climbs one step if no args are given
  mssg='../'
  comm='../'

  if [ ${1} ]; then
    for ((i = 0; i < $1 - 1; i++));
    do
      mssg=$mssg$comm
    done
  fi
  eval "cd ${mssg}"
}
