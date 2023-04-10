# Python program to check if year is a leap year or not
Year=int(input("Enter a year: "))

# divided by 100 means century year (ending with 00)
# century year divided by 400 is leap year
if (Year % 400 == 0) and (Year % 100 == 0):
    print("{0} is a leap year".format(Year))

# not divided by 100 means not a century year
# year divided by 4 is a leap year
elif (Year % 4 ==0) and (Year % 100 != 0):
    print("{0} is a leap year".format(Year))

# if not divided by both 400 (century year) and 4 (not century year)
# year is not leap year
else:
    print("{0} is not a leap year".format(Year))
