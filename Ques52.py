# Open existing text file and reverse its contents. i.e
# a) print the last line as first line and first line as last line (Reverse the lines of the file)
# b) print characters of file from last character of file till the first character of the file.(Reverse entire contents of  file )

strlist = list()
for lines in reversed(open("firstFile.txt").readlines()):
    print(lines.rstrip())
    strlist.append(lines.rstrip())

for string in strlist:
    print(string[::-1])