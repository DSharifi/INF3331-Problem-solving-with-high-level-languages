#bash script that will run wc.py
wc() { 
    python3 "$(pwd)"/wc.py $@
}