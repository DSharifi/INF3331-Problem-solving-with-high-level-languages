def repeat_good(text):
    output = text[0].upper()
    for count, char in enumerate(text[1:], 2):
        output +="{}{}{}".format("-", char.upper(), char.lower()*(count))
    return output




def repeat_bad(text):
    output = ""
    First = True

    for char in range(len(text)):
        if First:
            output += text[char].upper()
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