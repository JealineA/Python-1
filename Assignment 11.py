#User input postive number

user_input = input('Enter a positive number: ')

#Check if the user entered a postive number
while not user_input.isdigit() or int(user_input) <0:
    user_input = input('Invalid input. Please enter a postive number: ')

#Convert the user input to int
number = int(user_input)

#Generate the collatz sequence steps below

sequence = []
while number != 1:
    sequence.append(number)
    if number % 2 == 0: # expression to identity if the number is even
        number //=2 # expression to divide this number by 2
    else: #if it is odd then multiply by 3 and add plus 1
        number = 3 * number + 1

    #Add one at the end of the sequence
    sequence.append(1)
    print('The collatz sequence is: ', sequence)


