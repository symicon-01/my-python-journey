year = int(input('please enter your year of birth, '))
if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))
    print ('Hence, your year of birth is a leap year')
elif (year % 4 ==0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))
    print ('Hence, your year of birth is a leap year')
# if not divided by both 400 (century year) and 4 (not century year)
# year is not leap year
else:
    print("{0} is not a leap year".format(year))
    print ('Hence, your year of birth is not a leap year')
