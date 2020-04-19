# Write a program to handle following exceptions using Try block.
# a) IO Error while you try writing contents into the file that is opened in read mode only.
# b) ValueError

try:
    myfile =open("file.txt","r")
    print(myfile.read())
    myfile.write("Hello")
except IOError:
    print("Writing mode is not allowed")

try:
    num = int(input("Enter value:"))
except ValueError:
    print("ValueError")

'''Output Extract:
Enter value:'trttr'
ValueError'''