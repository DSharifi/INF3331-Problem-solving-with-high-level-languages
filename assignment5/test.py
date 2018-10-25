import re

regex = r"^\"(.*)\": (.*)$"
regkex = r"(.*): (.*)"

filen = open("naython.syntax", "r")
theme = open("naython.theme", "r")

for comment in theme:
    print(re.findall(regkex, comment))
    print(re.findall(regkex, comment)[0][0])

filen.close()
