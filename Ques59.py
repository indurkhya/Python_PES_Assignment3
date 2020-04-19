# Create file called "stringop.py" which has following functions
# i) functions to sort numbers (Use loops for  sorting, do not use built in function)
# ii) function to search given element through binary search method.(Refer to net for the Binary search algorithm)
# iii) function to reverse the given string
# Write new program in file strpackage.py such that you import functions of file "stringop.py" to your new program

# strpackage.py
from stringop import *

sortNumbers([34, 56, 21, 11, 3])
reverselist([11, 22, 12, 10, 32, 13])
print("binarySearch([22,33,44,12,34]):", binarySearch([22, 33, 44, 12, 34], 22))