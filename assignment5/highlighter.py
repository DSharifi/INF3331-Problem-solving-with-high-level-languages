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



def find_matches(syntax_dict, source):
    """
    Finds all matches from dict in the source string, and returns list of tuples 
    for all matches.
    
    Arguments:
        syntax_dict {dict} -- dictionary containing regex and theme
        source {str} -- string of sourcefile to find matches
    
    Returns:
        list -- list containing tuples of every match: 
                (text, startpos, endpos, startcolor, endcolor name)
    """

    outputString = source
    matches = []
    end_code = "\033[0m"

    for name in syntax_dict:
        regex = syntax_dict[name][0]
        theme = syntax_dict[name][1]
        color_code = "\033[{}m".format(theme)
        for m in regex.finditer(outputString):
            # (text, startpos, endpos, startcolor, endcolor name)
            matches.append((m[0], m.start(), m.end(),
                            color_code, end_code, name))
    
    # reverse sort match_list after 'start' value
    matches.sort(key=lambda x: x[1], reverse=True)
    # remove duplicates of match_list 'start' value
    toolz.unique(matches, key=lambda x: x[1])
    matches = remove_duplicate_coloring(matches)
    return matches


def color_matches(matches, source, round1 = True):
    """
    Takes in a sourcestring and matches, to color all the matches in the source
    
    Arguments:
        matches {str} -- matches
        source {str} -- source file
    
    Returns:
        str -- colored source file
    """
    outputString = source
    if round1: 
        for match in matches:
                outputString = outputString[:match[1]] + \
                    match[3]+match[0]+match[4]+outputString[match[2]:]
    else:
        for match in matches:
            print(match[-1])
        second_color = list(
            filter(lambda match: match[-1] == "escape_char", matches))
        print("RUNNING")
        map(lambda x: print(x[1]), second_color)
        for match in second_color:
                outputString = outputString[:match[1]] + \
                    match[3]+match[0]+"\033[0;93m"+outputString[match[2]:]
        

    return outputString
    

def highlight(syntaxfile, themefile, sourcefile_to_color):
    """
    Prints out a colored version of a source file, given a theme and syntaxfile.
    
    Arguments:
        syntaxfile {file} -- syntaxfile containing a regex for every name
        themefile {file} -- themefile with UNIX color coding for every name
        sourcefile_to_color {file} -- file to be colored
    """

    syntax_string = syntaxfile.read()
    theme_string = themefile.read()
    source = sourcefile_to_color.read()

    syntaxfile.close()
    themefile.close()
    sourcefile_to_color.close()

    
    syntax_dictionary = dict_syntax_color(syntax_string, theme_string)

    # first round
    matches = find_matches(syntax_dictionary, source)
    first_color = color_matches(matches, source)

    print(first_color)


def remove_duplicate_coloring(matches):
    """
    Returns a list with all matches from a given list that are nested removed.

    Arguments:
        matches {list} -- list of all matches

    Returns:
        {list} -- 
    """
    indices = set()

    for i, match in enumerate(matches):
        for j, compare_match in enumerate(matches):
            if matches is compare_match:
                continue
            if compare_match[1] < match[1] <= compare_match[2]:
                indices.add(i)
            elif match[1] < compare_match[1] < match[1]:
                indices.add(j)

    indices = list(indices)
    indices.sort(reverse=True)
    
    list(map(lambda match: indices.__getitem__, indices))

    return_val = []
    for i, match in enumerate(matches):
        if not i in indices:
            return_val.append(match)
    
    return return_val

            
    



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
