import argparse
import highlighter as hg

def diff(initial_file, compare_file):
    """Compares files line by line
    takes two files as input, and outputs a file containing all changes which have 
    to be made to the first file to make it into the second file
    
    Arguments:
        initial_file {file} -- initial file
        compare_file {file} -- file that is made changes to
    """


    initial_text = initial_file.read().split("\n")
    initial_file.close()

    compare_text = compare_file.read().split("\n")
    compare_file.close()
    
    themes = open('diff.theme', 'r')
    themes_str = themes.read()
    themes.close()

    syntax = open('diff.syntax', 'r')
    syntax_str = syntax.read()
    syntax.close()

    # get syntax and theme as dict
    theme_syntax_dict = hg.dict_syntax_color(syntax_str, themes_str)


    # indexes detected in compare_file
    initial_text = list(enumerate(initial_text))
    changes = ''

    # find added lines, and lines untouched
    for line1 in compare_text:
        found = False
        for line2 in initial_text:
            if line1 == line2[1]:
                changes += '0\t{}\n'.format(line1)
                initial_text.remove(line2)
                found = True
                break
        if not found:   
            changes += '+\t{}\n'.format(line1)

    changes = changes.split('\n')

    # add removed lines
    for removed in initial_text:
        changes.insert(removed[0], '-\t{}'.format(removed[1]))

    changes_str = ''
    # color lines
    for line in range(len(changes)-1):
        changes_str += ("\033[{}m{}\033[39m\n".format(
            theme_syntax_dict[changes[line][0]][1], changes[line]))
    
    # print the diff
    print(changes_str)






if __name__ == "__main__":
    parser = argparse.ArgumentParser(description= """Compares files line by line
    takes two files as input, and outputs a file containing all changes which have 
    to be made to the first file to make it into the second file""")

    parser.add_argument("file1", metavar="initial file",
                        help="Initial file", type=argparse.FileType("r"))
    
    parser.add_argument("file2", metavar="Compare to file",
                        help="File made changes to", type=argparse.FileType("r"))

    args = parser.parse_args()
    
    diff(args.file1, args.file2)
