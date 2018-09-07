from sys import argv
import os

total_lines, total_words, total_characters = 0, 0, 0

#returns a tuple with lines, words and chars in a file
def word_counter(path):
    global total_lines, total_words, total_characters
    input_file = open(path, "r")
    lines, words, characters = 0,0,0
    for line in input_file:
        lines += 1
        characters += len(line)
        words += len(line.strip())

    total_lines += lines
    total_words += words
    total_characters += characters

    return (lines, words, characters)

#determine whethere a path is a file, directory or non existant
def file_handler(path):
    if os.path.isfile(path):
        return "\t{0}\t{1}\t{2}\t{3}".format(*word_counter(path), path)
    elif os.path.isdir(path):
        return "{0}: Is a directory\n\t0\t0\t0\t{0}".format(path)
    else:
        return "wc: {0}: No such file or directory".format(path)

#main
def main():
    for i in range (1, len(argv)):
        print
        print(file_handler(argv[i]))


        
    if len(argv) > 2:
        print("\t{}\t{}\t{}".format(total_lines, total_words, total_characters))


if __name__ == "__main__":
    main()