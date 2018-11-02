How to run files:
5.1 Syntax highlighting
    usage: highlighter.py syntaxfile themefile sourcefile_to_color
    use --help flag to get information on how to use the script.

 5.4 grep
    usage: grep.py file [regex patterns] --highlight
    use --help flag to get information on how to use the script.
    example:  
    - python3 grep.py  diff1.txt grep.py a b '\d'
    (with highlighting): 
    - python3 grep.py  diff1.txt grep.py a b '\d' --highlight

5.5 superdiff
    usage: diff.py initial_file compare_to_file
    example: python3 diff.py diff1.txt diff2.txt
