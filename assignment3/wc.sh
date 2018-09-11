#bash script that will run wc.py
path=$(pwd)
wc() {
    python3 $path/wc.py $@
}