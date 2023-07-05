# Disclaimer:  Please note that every question is a single program
# Question 1
secret_number = 69 # secret number that user has to guess
user_guess = int(input("Guess a number from 10 upto 99: ")) # getting the input from the user
guess_count = 1 # keeping the track of user guess count in a variable guess_count

number_guessed = False # assigning the False boolean value to number_guessed which will be True if the user guesses the number

# checking if the user complies
# looping until user gives number between 10 and 99
while (user_guess < 10 or user_guess > 99):
  print(f"Enter something between 10 and 99.(Not {user_guess}): ") # giving them direction
  user_guess = int(input("Guess a number from 10 upto 99: ")) # getting the input from the user

# looping until user guesses the correct number
while (not number_guessed):
  if (user_guess == secret_number): # Exiting the loop when the user guesses the number
    number_guessed = True # changing the value from False to True when user guesses the number
    print("Congrats! The secret number was 69.") 
    print(f"It took you {guess_count} guesses to guess the correct number.") # printing how many guesses it took to guess the secret number
  else:
    # conditions to see by how much off the user_guess is and outputting the required directions for user
    if (user_guess > secret_number):
      gap_secret_number_guessed_number = user_guess - secret_number
      if (gap_secret_number_guessed_number <= 5):
        print("Your guess is higher but you are right there.")
      elif (gap_secret_number_guessed_number <= 10):
        print("Your guess is higher but you are close to guessing it.")
      elif (gap_secret_number_guessed_number > 10 and gap_secret_number_guessed_number <= 20):
        print("Your guess is higher and you are very off.")
      elif (gap_secret_number_guessed_number > 20):
        print("Your guess is higher and you are wayyy off.")
    
    # conditions to see by how much off the user_guess is and outputting the required directions for user
    elif (user_guess < secret_number):
      gap_secret_number_guessed_number = secret_number - user_guess
      if (gap_secret_number_guessed_number <= 5):
        print("Your guess is lower but you are right there.")
      elif (gap_secret_number_guessed_number <= 10):
        print("Your guess is lower and you are close to guessing it.")
      elif (gap_secret_number_guessed_number > 10 and gap_secret_number_guessed_number <= 20):
        print("Your guess is lower and you are very off.")
      elif (gap_secret_number_guessed_number > 20):
        print("Your guess is lower and you are wayyy off.")

    guess_count += 1 # increamenting the guess_count everytime user guesses a wrong number
    user_guess = int(input("Guess a number from 10 upto 99: ")) # prompting the user again for the guess 
    
    # checking if the user complies
    # looping until user gives number between 10 and 99
    while (user_guess < 10 or user_guess > 99):
      print(f"Enter something between 10 and 99.(Not {user_guess}): ")
      user_guess = int(input("Guess a number from 10 upto 99: ")) # getting the input from the user

# Question 2
list_1 = [2, 26, 563, 3584, 9, 0] # a list of numbers in random order
index_i = 0 # starting index of i
last_index = len(list_1) - 1 # last index of the list here it is 5

# this loop will work till the ith index is less than or equal to last_index
while (index_i <= last_index):
  index_j = index_i + 1 # jth index is always one step next to ith

  # while jth index is less than or equal to last_index this loop works
  while (index_j <= last_index):
    if (list_1[index_i] < list_1[index_j]): # if we find any jth position number greater than the current ith number we swap the two number
      temp = list_1[index_i] 
      list_1[index_i] = list_1[index_j]
      list_1[index_j] = temp
    
    index_j += 1 # increamenting the jth index by 1
  index_i += 1 # increamenting the ith index by 1
  
print(f"The list in descending order is {list_1}") # printing the list at last



# Question 3
import math # importing the math module 

user_input = int(input("Enter a number: "))  # getting the input from the user
prime = True # assuming that the number is already prime even though they give a number that is not prime
if (user_input <= 1): # if the number is less than 1 or 1 then it is not prime
  print("The number is not prime.")
else: # if the number is greater than 1 the following commands are executed
  """This is a trail division method which will get the square root of the number and 
  if the number is divisible by any number in the sequence from 2 to that (squareroot(number) + 1) 
  we say that it is not prime."""
  for i in range(2, int(math.sqrt(user_input)) + 1):
    if (user_input % i == 0):
      prime = False # if the number is divisible by anything else than 1 then we say that it is not prime.


# these will print if the number is prime or not depending on what is stored in the variable prime.
if (prime):
  print("The number is prime.")
else:
  print("The number is not prime.")

  
# Question 4
number = int(input("Enter a number: ")) # asking for input from user 

if (number < 0): # if the number is less than 0 we output error
  print("Error! Try again!")
elif (number == 0): # if the number is 0 we output 1
  print("The factorial of 0 is 1.")
else: # if the number is greater than 1 we find the factorial 
  factorial_result = 1 # result is stored in this variable
  for i in range(1, number + 1):
    factorial_result = factorial_result * i
  
  print(f"The factorial of {number} is {factorial_result}.") # at the end we print the factorial

# Question 5
nth_position = 20 # position till where we want the number to be printed here we want it to be printed till 20.
current_position = 2 # current position is 2 as the first is 0th is 0, and 1st is 1.
current_number = 0 # current number is 0 
next_number = 1 # next number is 1
next_number_after = 0 # this is the number that will be the number after the next_number 0, 1, 1 <-- (this is next_number_after)

# looping until the current_position variable is equal to the nth_position variable
while (current_position <= nth_position):
  next_number_after = current_number + next_number # next_number_after is the sum of current_number and next_number
  current_number = next_number # after the sum, current_number is assigned the value of next_number
  next_number = next_number_after # after the sum, next_number is assigned the sum of those two number which was stored in next_number_after
  current_position += 1 # current_position is increamented
    
print(f"The {nth_position}th fibonacci number in the series is {next_number_after}.") # printing the required position number
