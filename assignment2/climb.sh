climb() {
  mssg=''
  comm='../'
  for ((i = 1; i <= $1; i++))
  do
    mssg=$mssg$comm
  done
  eval "cd ${mssg}"
}
