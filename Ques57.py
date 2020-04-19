# Try implementing atleast any 5 exceptions in you program.

import math
import sys
import time

# Exception
try:
    a = int(input("enter a: "))
    num = a / 2
    print(num)
except Exception:
    print("Exception")

# Standard error
try:
    f0 = open("firstFile.txt", "r")
except StandardError as e:
    print("Standard error:No file exists",e)

# Arithmetic error
try:
    div = 2 / 0
except ArithmeticError:
    print("Arithmetic error exception")

# StopIteration
try:
    fo = open('firstFile.txt', "r")
    for i in range(1, 10):
        print(fo.read())
except StopIteration:
    print("Stop Iteration Exception")
fo.close()

# Systemexit
try:
    sys.exit()
except SystemExit:
    print("system exit exception")

# Overflow error
try:
    a = math.exp(4 / 42 * 349304332)
except OverflowError:
    print("Overflow error exception")

# Value error
try:
    a = math.sqrt(-32 / 3)
except ValueError:
    print("ValueError")

# Zero division error
try:
    a = 2 / 0
except ZeroDivisionError:
    print("Zero Division exception")

# AssertionErrror
try:
    a = 12
    assert (a > 10), "assertion error"
except AssertionError:
    print("Assertion error")

# Attribute Error
try:
    raise AttributeError
except AttributeError:
    print("Attribute error")

# EOF error
try:
    fo = open("firstFile.txt", "r")
    fo.read()
except EOFError:
    print("EOF error")

# import error
try:
    import dummy
except ImportError:
    print("Import error exception")

# look up error
dict = {'empid': 'empname'}
try:
    print(dict['abc'])
except LookupError:
    print('Lookup error')

# index error
try:
    list1 = [12, 13, 14, 45, 34]
    print(list1[9])
except IndexError:
    print("IndexOutofbound")

# name error:
try:
    name = input("Enter name")
    print(name)
except NameError:
    print("Name Error")

# keyboard interrupt
try:
    x = input()
    time.sleep(1)
except KeyboardInterrupt:
    print("Keyboard interrupt")

# KeyError
try:
    print(dict['1'])
except:
    print('Key Error')

# Unbound Local Error
try:
    raise UnboundLocalError
except UnboundLocalError:
    print('UnboundLocalError!')
# IOError
try:
    fo = open('file.txt', "r")
    fo.write('write hereafter')
except IOError:
    print('IOError!')

# SyntaxError
try:
    raise SyntaxError
except SyntaxError:
    print('Syntax Error !')

# TypeError
try:
    str = 'hello'
    str = str - 1
except TypeError:
    print('Type Error')

# ValueError
try:
    str = 'hello'
    print(int(str))
except ValueError:
    print('Value Error')

# Runtime Error
try:
    raise RuntimeError
except RuntimeError:
    print('Runtime Error occured !')