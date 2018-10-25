import argparse
import re


def dict_syntax_color(syntaxfile, themefile):
    syntax_dict = {}

    regex_syntax = r"^\"(.*)\": (.*)$"
    for line in syntaxfile:
        syntax = re.findall(regex_syntax, line)
        syntax_dict[syntax[0][1]] = [syntax[0][0]]

    regex_theme = r"(.*): (.*)"
    for line in themefile:
        i = re.findall(regex_theme, line)
        syntax_dict[i[0][0]].append(i[0][1])

    return syntax_dict



def highlight(syntaxfile, themefile, sourcefile_to_color):
    dicter = dict_syntax_color(syntaxfile, themefile)
    



if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Code highlighter")

    parser.add_argument("syntax", metavar="syntaxfile", help="""A syntax file containing lines of the form regex: name where
                        regex is a quoted string specifying a regex, and name is some arbitrary
                        alphabetical string giving some name to the thing specified by the regex.""", type = argparse.FileType("r"))

    parser.add_argument("theme", metavar="themefile", help=""".theme file should have lines of the form name: color sequence
                        where name is one of the names specified in the matching .syntax file,
                        and color sequence is some bash color sequence. (i.e. something which
                        would be valid if you did "\033[{}m".format(color sequence)""", type=argparse.FileType("r"))
    
    parser.add_argument("sourcefile", metavar="sourcefile_to_color", help="Desired sourcefile to highlight", type=argparse.FileType("r"))

    args = parser.parse_args()

    highlight(args.syntax, args.theme, args.sourcefile)
