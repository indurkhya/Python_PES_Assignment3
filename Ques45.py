# Write a program to check given string is Palindrome or not. (Use function Concepts and Required keyword, Default
# parameter concepts) i.e Reverse the given string and check whether it is same as original string, if so then it is
# palindrome. Example: String "malayalam" when reversed will be "malayalam" hence palindrome.

def PalindromeCheckRequiredParam(myStr):
  'this checks for the palindrokme string'
  #myStr="Hello buddy"
  myStr=myStr.lower()
  myStr1=myStr[::-1]
  if myStr==myStr1:
    print("The given string",myStr,"is palindrome")
  else:
    print("The given string",myStr,"is not palindrome")
  return
#myStr=input("Enter the string")
PalindromeCheckRequiredParam("hello world")
PalindromeCheckRequiredParam("POP")

def PalindromeCheckDefaultParam(myStr="Malayalam"):
  'this checks for the palindrokme string'
  #myStr="Hello buddy"
  myStr=myStr.lower()
  myStr1=myStr[::-1]
  if myStr==myStr1:
    print("The given string",myStr,"is palindrome")
  else:
    print("The given string",myStr,"is not palindrome")
  return
#myStr=input("Enter the string")
PalindromeCheckDefaultParam("duud")
PalindromeCheckDefaultParam()
