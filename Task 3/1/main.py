import re

f = open("onelinefile.txt")
contents = f.read()
f.close()

pattern = re.compile(r'(\d+)([A-Za-z]+)(\d+\.\d+)([A-Za-z]+)')
table = pattern.findall(contents)

f = open("Filename2.csv", "w")
for i in table:
    f.write(",".join(i) + "\n")
f.close()
