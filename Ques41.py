# Using calendar module perform following operations.
# a) Print the 2016 calendar with space between months as 10 characters.
# b) How many leap days between the years 1980 to 2025.
# c) Check given year is leap year or not.
# d) print calendar of any specified month of the year 2016.

import calendar
print(calendar.calendar(2016,c=10))
print("calendar for year 2016 with space between months as 10 character is", calendar.calendar(2016,c=10))
print("Leap days between the years 1980 to 2025 are",calendar.leapdays(1980,2025),"days")
enterYear=int(input("enter the year to see if leap or not"))
if calendar.isleap(enterYear)==True:
  print("year",enterYear,"is a leap year")
else:
  print("year",enterYear,"is not a leap year")
enterMonth2016=int(input("Enter the month no of 2016 year to print it"))
print(calendar.month(2016,enterMonth2016,w=2,l=1))