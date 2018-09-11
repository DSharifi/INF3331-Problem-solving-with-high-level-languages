from sys import argv
import os

#global counters, for total input
total_lines, total_words, total_characters = 0, 0, 0

def counter(path):
    """
    Counts total number of lines, words and characters in a file, given a 
    path.

    Arguments:
        path: type: string. Should be path of the desired file counted.
    

    Implementation:
    reads a file from path in binary. Iterate line for line in file, and increment
    local line, word and char count, for words in line, and chars in words.
    
    Side effect:
        -increments global variables 'total_lines, total_words, total_characters' with 
        line-, word- and character count of the file path given respectively.

    Returns:
        tuple containing lines, words, characters. All the three as ints.

    Raises:
        FileNotFoundError:
    """
    global total_lines, total_words, total_characters
    #open the file in binary
    input_file = open(path, "rb")
    #wc in bash counts lines from 0, thuns lines is initialised at -1
    lines, words, characters = -1,0,0
    for line in input_file:
        lines += 1
        characters += len(line)
        words += len(line.split())

    #correct line count to 0 (file is empty)
    if lines == -1: lines = 0
    
    #increment global variables
    total_lines += lines
    total_words += words
    total_characters += characters
    
    return (lines, words, characters)


def file_handler(path):
    """
    Determine whether a path is a file, directory or non existant.
    The result is returned as a string, with word count included.
    
    Arguments:
        path: type: string
    Returns:
        type: string
        returns a formatted string with the word count.
    Implementation:
        If the path is a:
        file    --->    call counter with path as arg, and return the string
        else    --->    return a string with the format of the path.
    """
    #is a file
    if os.path.isfile(path):
        return "\t{0}\t{1}\t{2}\t{3}".format(*counter(path), path)
    #path is dir
    elif os.path.isdir(path):
        return "{0}: Is a directory\n\t0\t0\t0\t{0}".format(path)
    #path 
    else:
        return "wc: {0}: No such file or directory".format(path)

#main
def main():
    """
    Main method that runs word counter. Prints out word count of files provided
    as sys args in terminal.

    Implementation:
        Sends system args to file_handler, and prints out the return string for every arg
        given.
    """
    #loop through all sys args
    for i in range (1, len(argv)):
        print
        print(file_handler(argv[i]))

    #print total, if more than one arg is given
    if len(argv) > 2:
        print("\t{}\t{}\t{}\ttotal".format(total_lines, total_words, total_characters))


if __name__ == "__main__":
    main()