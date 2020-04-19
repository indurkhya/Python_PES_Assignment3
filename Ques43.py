# Write a program to search given element from the list. Use your own function to search an element
# from list. Note: Function should receive variable length arguments and search each of these arguments present in the list.


# need to verify


def find(n):
  "This finds element from the list"
  list1=input("Enter list elements")
  list1=list(list1)
  list1.sort()
  found=0
  for each in list1:
    if n==each:
        print("element",n,"is present in the list")
        found=1
        break
  if found==0:
    print("element",n,"is not presnt in the list")
number=input("enter element to check in the list")
find(number)