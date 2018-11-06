import argparse
import re
import highlighter as hg

def create_dict(regex_list):
    """
    Returns a dictionary with syntax and themes, given a list of regexes.
    
    Arguments:
        regex_list {list} -- list of regexes
    
    Returns:
        dict -- key is name, and value are pairs of regex string and color_sequence respectively
    """

    regex_dict = {}
    colors = ("0;30", "0;31", "0;32", "0;33",
              "0;34", "0;35", "0;36", "0;37", "0;38")
    i = 0
    
    for regex in regex_list:
        if i >= len(colors):
            i = 0
        regex_dict[i] = (re.compile(regex, re.S), colors[i])
        i += 1

    return regex_dict


def grep(sourcefile, regex_list, highlight):
    """
    Prints out all matches from the regex_list given a sourcefile. Highlight flag
    decides whether the matches are color coded or not.
    
    Arguments:
        sourcefile {file} -- source file
        regex_list {list} -- list of regexes
        highlight {bool} -- flag. Decides whether to highlight the output or not.
    """
    source = sourcefile.read()
    sourcefile.close()
    
    dictionary = create_dict(regex_list)
    matches = hg.find_matches(dictionary, source)
    
    #output = hg.remove_duplicate_coloring(matches)
    output = hg.color_matches(matches, source)
    output = output.split("\n")

    # filter out non colored lines (i.e. not matched)
    lines = list(filter(lambda line: re.search(
        '\\033\[0(?:\;)?\d*m', line), output))


    # no highlighting
    if not highlight:
        removeColoring = "\\033\[0(?:\;)?\d*m"
        lines = list(map(lambda line: re.sub(removeColoring, "", line), lines))
    
    for line in lines:
        print(line)



if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=" grep searches for given PATTERNS in input FILE.")

    parser.add_argument("sourcefile", metavar="sourcefile_to_find_paterns",
                        help="Desired sourcefile to highlight", type=argparse.FileType("r"))
    
    parser.add_argument("regex", metavar="regex pattern", help="", nargs='+', type=str)

    parser.add_argument('--highlight', dest='highlight', action='store_const',
                        const=True, help='Highlight the matches found (default: no higlighting)')

    args = parser.parse_args()
    
    grep(args.sourcefile, args.regex, args.highlight)
