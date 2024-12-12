#Grading input
from getpass import GetPassWarning

First_Grade = float(input ('Enter First Grade:'))
Second_Grade= float(input ('Enter Second Grade:'))
Third_Grade = float(input ('Enter Third Grade: '))

#GPA calculation
GPA = ((First_Grade + Second_Grade + Third_Grade)/3)

#Grading Structure
if GPA >=90:
        print('Your final grade is: A')
elif GPA >=80 <=89:
         print ('Your final grade is: B')
elif GPA >=70 <=79:
         print ('Your final grade is: C')
elif GPA >=60 <=69:
         print ('Your final grade is: D')
elif GPA <= 60:
         print ('Your final grade is: F')



