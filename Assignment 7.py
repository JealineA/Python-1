#User enter Year
Year = float(input ('Enter Year: '))

#If year is leap year
if (Year % 4 == 0 and Year % 100 != 0) or(Year % 400 ==0):
    print (Year, 'is a leap year.')
else:
    print(Year, 'is not a leap year.')