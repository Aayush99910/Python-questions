'''# Question 1
user_input = int(input("Enter number from 0 to 11: "))

# checking if the input is valid
if (user_input < 0 or user_input > 11):
  print("Invalid input. Number should be from 0 to 11.")

# outputing the month based on input
if (user_input == 0):
  print("January")
elif (user_input == 1):
  print("Febuary")
elif (user_input == 2):
  print("March")
elif (user_input == 3):
  print("April")
elif (user_input == 4):
  print("May")
elif (user_input == 5):
  print("June")
elif (user_input == 6):
  print("July")
elif (user_input == 7):
  print("August")
elif (user_input == 8):
  print("September")
elif (user_input == 9):
  print("October")
elif (user_input == 10):
  print("November")
elif (user_input == 11):
  print("December")


# Question 2
def next_compass_point(direction):
  if (direction == "N"):
    return "E"
  elif (direction == "E"):
    return "S"
  elif (direction == "S"):
    return "W"
  elif (direction == "W"):
    return "N"
  
# calling the function
print(next_compass_point("E"))

# Question 3
def hours_in(total_seconds):
  hours = total_seconds / 3600
  hours = int(hours)
  return hours

def minutes_in(total_seconds):
  seconds_after_hours = total_seconds % 3600
  minutes = seconds_after_hours / 60
  minutes = int(minutes)
  return minutes

def seconds_in(total_seconds):
  seconds_after_hours = total_seconds % 3600
  seconds_after_minutes = seconds_after_hours % 60
  seconds = seconds_after_minutes
  seconds = int(seconds)
  return seconds

print(f"The hours are {hours_in(2768)}")
print(f"The minutes are {minutes_in(2768)}")
print(f"The seconds are {seconds_in(2768)}")

# Question 4
# Making a list of temperatures
celsius_inputs = [36, 41, 82, 53, 69]
print("--------")

#looping the list
for temp in celsius_inputs:
  fahrenheit = ((9/5) * temp) + 32
  print(f"|{temp}|{fahrenheit}|")
  print("--------")

# Question 5
def remove(occurence, sentence):
  i = 0
  first_part = ""
  second_part = ""
  length_of_string = len(sentence)
  while(i < length_of_string):
    j = i + 1
    part_string = sentence[i] + sentence[j]
    if (part_string == occurence):
      first_part = sentence[0:i]
      second_part = sentence[j+1:]
      full_sentence = first_part + second_part
      return full_sentence
    i = i + 1

print(remove("pp", "apple"))

# Question 6
def is_palidrome(sentence):
  length_of_string = len(sentence)
  last_item = length_of_string - 1
  reverse_string = "" # empty string
  done = False

  while (not done):
    if (last_item < 0):
      done = True
      break
    
    reverse_string = reverse_string + sentence[last_item]
    last_item = last_item - 1
  
  if (sentence == reverse_string):
    print("The string is a palindrome.")
  else: 
    print("The string is not a palindrome.")
  
is_palidrome("level")'''
