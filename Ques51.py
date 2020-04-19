# In a given directory search all text files for the pattern "Treasure".
# a) Find how many text files has the pattern.
# b) Count how many times pattern repeats in each file Note: Create at least 4 text files in a directory and keep the pattern in at least 2 files. Repeat the pattern in the file many times.

import glob
totalCount = 0
for eachfile in glob.glob("*.txt"):
    myfile = open(eachfile, "r")
    list1 = myfile.read().split()
    if "Treasure" in list1:
        print("File name:",eachfile,"\nCount of letter Treasure in this file:", list1.count("Treasure"))
        totalCount += list1.count("Treasure")
    else:
        print("File name:",eachfile,"\nCount of letter Treasure in this file:", 0)
    myfile.close()
print("Total counts of letter Treasure in all the files:", totalCount)