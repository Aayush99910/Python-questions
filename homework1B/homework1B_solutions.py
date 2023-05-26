# Question 1
n_number = int(input("Enter a number: "))

if (n_number <= 0):
    print('Error. Please enter a number greater or equal to 1.')
else:
    # doing range(1, n_number + 1) because I want the range to start from 1 not 0
    # moreover n_number + 1 because the range function doesn't include the last number so doing n + 1 will include that number 
    for i in range(1, n_number + 1):
        output = int(i * (i + 1) / 2) # using a formula to get the required output
        print(i, "\t%d" % output) #printing the output using some formatting       

# Question 2
# Getting the number from the user
user_input = int(input("Enter a number: "))
length_number = len(str(user_input))

x = 1 # x is the starting number that will be used to compare with the length of the user_input digit
even_count = 0 # variable that stores the even occurence of the digit in the number
while(x <= length_number): # we loop until we go through every single digit in the number
    last_digit = user_input % 10 # this is to extract the last digit in every iteration
    if (last_digit % 2 == 0): # if the digit is divisible by 2 then we say thats even and even counter is increamented
        even_count += 1
    user_input = str(user_input) # user_input is changed to a str type
    last_index = len(user_input) - 1 # we get the last index of the number
    user_input = user_input[0:last_index] # user_input is updated to have digit from 0 index to second last index
    
    if (user_input == ''): # if there is no digit left we break from the loop
        break
    else:
        user_input = int(user_input) # if not we comvert the user_input that was converted to str back to int
    x = x + 1 # increamenting the x 
print(even_count) # outputing the even_count at the end


# Question 3

list1 = [2, 3, 4]  # list of numbers
total = 0 # a variable called total that is used to keep track of the sum of all the squared numbers

# looping over each item in the list1
for number in list1:
    square = number*number # squaring each number
    total = total + square # calculating the total everytime

print(total) # outputing the print at last


# Question 4
user_input = int(input("Enter a number: ")) # getting the input from the user

# if the input is less than zero or zero we output Error! Try again!
if (user_input < 0):
    print("Error! Try again!")
elif (user_input == 0):
    print(0)
else:
    result = 1 # result is 1 as in factorial we have to multiply by 1 anyway
    for i in range(1, user_input + 1): # ranging from 1 to the number that user provides
        result = result * i # multiplying result at each iteration 

    print(result) # outputing the result at the end
    

# Question 5
# getting the grade and type casing it into float and after that checking the what grade the student got
grade = float(input("What is your grade? "))

if (grade > 100):
    print("Error! Try again!")
elif (grade < 0):
    print("Error! Try again!")
elif (grade >= 90):
    print("Congrats you got an A.")
elif (grade >= 80):
    print("You got a B.")
elif (grade >= 70):
    print("You got a C.")
elif (grade >= 60):
    print("You got a D.")
else:
    print("You got a F.")


# Question 6
random_number_from_1_to_7 = int(input("Enter a number from 1 to 7(inclusive): "))

if (random_number_from_1_to_7 > 7):
    print("Error! Try again!")
elif (random_number_from_1_to_7 < 1):
    print("Error! Try again!")
    
if (random_number_from_1_to_7 == 1):
    print("Monday")
elif (random_number_from_1_to_7 == 2):
    print("Tuesday")
elif (random_number_from_1_to_7 == 3):
    print("Wednesday")
elif (random_number_from_1_to_7 == 4):
    print("Thursday")
elif (random_number_from_1_to_7 == 5):
    print("Friday")
elif (random_number_from_1_to_7 == 6):
    print("Saturday")
elif (random_number_from_1_to_7 == 7):
    print("Sunday")
