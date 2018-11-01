import argparse
import re
import highlighter as hg

def create_dict(regex_list):
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
    description="Code highlighter")

    parser.add_argument("sourcefile", metavar="sourcefile_to_color",
                        help="Desired sourcefile to highlight", type=argparse.FileType("r"))
    
    parser.add_argument("regex", metavar="regex pattern", help="", nargs='+', type=str)

    parser.add_argument('--highlight', dest='highlight', action='store_const',
                        const=True, help='sum the integers (default: find the max)')

    args = parser.parse_args()
    
    grep(args.sourcefile, args.regex, args.highlight)
