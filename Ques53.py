# 53	File I/O Operations	Open the file is read & write mode and apply following functions
# a) All 13 functions mentioned in Tutorial File object table.

fo = open("firstFile.txt", "r+")
print("Name of the file: ", fo.name)
# Close opend file
fo.close()

fo = open("firstFile.txt", "r")
print("Name of the file: ", fo.name)
fo.flush()
fo.close()

fo = open("firstFile.txt", "r+")
print("Name of the file: ", fo.name)
fid = fo.fileno()
print("File Descriptor: ", fid)
fo.close()

fo = open("firstFile.txt", "r+")
print("Name of the file:", fo.name)
ret = fo.isatty()
print("Return value : ", ret)
fo.close()

fo = open("firstFile.txt", "r+")
print("Name of the file: ", fo.name)
for index in range(2):
   line = fo.read()
   print("Line No %d - %s" % (index, line))
fo.close()

fo = open("firstFile.txt", "r+")
print("Name of the file: ", fo.name)
line = fo.read(100)
print("Read Line: %s" % (line))
fo.close()

fo = open("firstFile.txt", "r+")
print("Name of the file: ", fo.name)
line = fo.readline()
print("Read Line: %s" % (line))
line = fo.readline(5)
print("Read Line: %s" % (line))
fo.close()

fo = open("firstFile.txt", "r+")
print("Name of the file: ", fo.name)
line = fo.readlines()
print("Read Line: %s" % (line))
line = fo.readlines(2)
print("Read Line: %s" % (line))
fo.close()

fo = open("firstFile.txt", "r+")
print("Name of the file: ", fo.name)
line = fo.readline()
print("Read Line: %s" % (line))
# Again set the pointer to the beginning
fo.seek(0, 0)
line = fo.readline()
print("Read Line: %s" % (line))
fo.close()

fo = open("firstFile.txt", "r+")
print("Name of the file: ", fo.name)
line = fo.readline()
print("Read Line: %s" % (line))
# Get the current position of the file.
pos = fo.tell()
print("Current Position: %d" % (pos))
# Close opend file
fo.close()


fo = open("firstFile.txt", "r+")
print("Name of the file: ", fo.name)
line = fo.readline()
print("Read Line: %s" % (line))
# Now truncate remaining file.
fo.truncate()
# Try to read file now
line = fo.readline()
print("Read Line: %s" % (line))
fo.close()

fo = open("firstFile.txt", "r+")
print("Name of the file: ", fo.name)
str = "This is 6th line"
# Write a line at the end of the file.
#fo.seek(0, 1)
line = fo.write( str )
# Now read complete file from beginning.
fo.seek(0,0)
lines=fo.read()
print(lines)
fo.close()

fo = open("firstFile.txt", "r+")
print("Name of the file: ", fo.name)
str = "This is 6th line"
# Write a line at the end of the file.
#fo.seek(0, 1)
line = fo.writelines( str )
# Now read complete file from beginning.
fo.seek(0,0)
lines=fo.read()
print(lines)
fo.close()