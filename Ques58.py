# Create file called  "calc.py" which has following functions
# i) functions to add 2 numbers
# ii) function to find diff of 2 numbers
# iii) function to multiply 2 numbers
# iv) all maths operations ( sqrt, div, floor div, modulus, primenumber)
# v) Fibonacci series
# a) Write a new program in file "maths.py" such that you import functions of file "calc.py" to your new program
# b) Use From <module> import <function> statement to import only few function  from calc module.

# math.py
from calc import *

add(4, 5)
diff(34, 12)
multiply(5, 7)
div(6, 2)
sqroot(9)
floor_div(33, 5)
fib(8)
isprime(443)