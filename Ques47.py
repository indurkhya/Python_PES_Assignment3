# Write function to extend the tuple with elements of list. Pass list and Tuple as parameter to the function.

def Extnd(tup1,list1):
  'This extends the tuple with elements of list'
  tup1=list(tup1)
  result=tup1+list1
  print(result)
tupp=(1,2,3,4)
listt=[11,22,33,44]
Extnd(tupp,listt)
