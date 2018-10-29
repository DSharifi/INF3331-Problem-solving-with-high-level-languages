import argparse
import toolz
import re


def dict_syntax_color(syntax_string, theme_string):
    """
    Returns a dictionary with syntax and themes.
    
    Arguments:
        syntax {str} -- String representation of syntaxfile
        theme {str} -- String representation of themefile
    
    Returns:
        dict -- key is name, and value are pairs of regex string and color_sequence respectively
    """
    syntax_dict = {}
    
    regex_syntax = r"^\"(.*)\": (.*)$"
    regex_theme = r"(.*): (.*)"

    syntax = re.findall(regex_syntax, syntax_string, re.MULTILINE)
    theme = re.findall(regex_theme, theme_string, re.MULTILINE)

    for synt in syntax:
        syntax_dict[synt[1]] = [re.compile(synt[0], re.S)]
    for them in theme:
        syntax_dict[them[0]].append(them[1])
    #print (str(syntax_dict))
    return syntax_dict

def color_string(syntax_dict, sourcefile_to_color):
    source = sourcefile_to_color.read()
    outputString = source

    end_code = "\033[0m"
    match_list_1 = []; match_list_2 = []
    for name in syntax_dict[:-2]:
        regex = syntax_dict[name][0]
        theme = syntax_dict[name][1]
        color_code = "\033[{}m".format(theme)
        for m in regex.finditer(source):
            # (text, startpos, endpos, name)
            match_list_1.append((m[0], m.start(), m.end(), color_code, name))
    
    # reverse sort match_list after 'start' value
    match_list_1.sort(key=lambda x: x[1], reverse=True)
    match_list_2.sort(key=lambda x: x[1], reverse=True)
    # remove duplicates of match_list 'start' value
    toolz.unique(match_list_1, key=lambda x: x[1])
    toolz.unique(match_list_2, key=lambda x: x[1])

    for t in match_list_1:
        outputString = outputString[:t[1]] + \
            t[3]+t[0]+end_code+outputString[t[2]:]

    for name in syntax_dict[-2:]:
        regex = syntax_dict[name][0]
        theme = syntax_dict[name][1]
        color_code = "\033[{}m".format(theme)
        for m in regex.finditer(outputString):
            # (text, startpos, endpos, name)
            match_list_2.append((m[0], m.start(), m.end(), color_code, name))

    for t in match_list_2:
        uncolored_text = uncolor_text(t[0])
        outputString = outputString[:t[1]] + \
            t[3]+uncolored_text+end_code+outputString[t[2]:]
    return outputString


def uncolor_text(text):
    return re.sub()

def highlight(syntaxfile, themefile, sourcefile_to_color):
    syntax_string = syntaxfile.read()
    theme_string = themefile.read()
    syntaxfile.close()
    themefile.close()
    
    syntax_dictionary = dict_syntax_color(syntax_string, theme_string)
    print(color_string(syntax_dictionary, sourcefile_to_color))


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
