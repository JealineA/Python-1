# Input display the 3 values
principal= float(input("enter the principal amount: "))

rate = float(input("Enter the interest rate in percentage: "))

time = float(input("Enter the time period in years: "))

# Calculate the simple interest

simpleIntrest = (principal * rate * time)/ 100

# Display the output

print("The calculated simple interest is: ", simpleIntrest)