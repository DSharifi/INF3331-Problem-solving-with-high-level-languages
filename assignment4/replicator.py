def repeat_good(text):
    """
    Takes in a string and returns a new string where every character is repeated 
    according to it’s position in the original string.
    The first occurence is always capitalized, and the other ones are always lower
    case
    
    Arguments:
        text {str} -- desired string to replicate
    
    Returns:
        str -- replicated version of the string

    Examples:
        >>> repeat_good('abcd')
        'A-Bb-Ccc-Dddd'
        >>> repeat_good('abcBd')
        'A-Bb-Ccc-Bbbb-Ddddd'
    """

    # First char is empty
    if text == "":
        return ""
    # Capitalize first string
    output = text[0].upper()
    # For loop to concatinate output with next char * its index
    for count, char in enumerate(text[1:], 1):
        output +="{}{}{}".format("-", char.upper(), char.lower()*(count))
    return output


def repeat_bad(text):
    """
    Takes in a string and returns a new string where every character is repeated
    according to it’s position in the original string.
    The first occurence is always capitalized, and the other ones are always lower
    case

    Arguments:
        text {str} -- desired string to replicate

    Returns:
        str -- replicated version of the string

    Examples:
        >>> repeat_good('abcd')
        'A-Bb-Ccc-Dddd'
        >>> repeat_good('abcBd')
        'A-Bb-Ccc-Bbbb-Ddddd'
    """

    output = ""
    First = True

    # first char is empty
    if text == "":
        return ""

    # for char in text
    for char in range(len(text)):
        # if first, dont add '-', just char
        if First:
            output += text[char].upper()
        # not first
        else:
            output += '-'
            for repetition in range (char + 1):
                if repetition == 0:
                    output += text[char].upper()
                else:
                    output += text[char].lower()
        First = False
    return output

print(repeat_good("abcD"))
print(repeat_bad("abcd"))
