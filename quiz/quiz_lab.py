'''# Question 1
my_name = " \t \n Aayush \t"


print(f"'{my_name}'") #printing without doing any stripping
print(f"'{my_name.lstrip()}'") # printing with left stripping
print(f"'{my_name.rstrip()}'") # printing with right stripping
print(f"'{my_name.strip()}'") # printing with stripping all the whitespace

# Question 2
# I would like to invite Neymar, Messi, Ronaldo
people_I_would_like_to_invite = ["Neymar", "Messi", "Ronaldo"]

for people in people_I_would_like_to_invite:
  print(f"Hi Mr.{people} I would like to invite you to dinner.")

print("I got a bigger table for all of us.")
people_I_would_like_to_invite.insert(0, "Pele")
middle_point = len(people_I_would_like_to_invite) / 2
people_I_would_like_to_invite.insert(int(middle_point), "Luka Modric")
people_I_would_like_to_invite.append("Halaand")


print(f"Hi there Mr. {people_I_would_like_to_invite[0]} I would like to tell you that I got a new table. Can you come over and join my dinner party?")
print(f"Dear Mr. {people_I_would_like_to_invite[1]} Can you come over and join my dinner party?")
print(f"Respected there Mr. {people_I_would_like_to_invite[2]} Would you mind joining my party?")
print(f"Hey there Mr. {people_I_would_like_to_invite[3]} Come around brother!")
print(f"Hey {people_I_would_like_to_invite[4]} Come over!")

# Question 3
user_choice_list = []

for i in range(5):
  user_input = input("Enter an item you would like to store in the list: ")
  user_choice_list.append(user_input)

print(user_choice_list)'''

# Question 4
list_of_cubes_1_to_10 = []

for i in range(1, 11):
  list_of_cubes_1_to_10.append(i**3)
  
print(list_of_cubes_1_to_10)

'''list_1_to_million = list(range(1, 1000001))
minimum_number = min(list_1_to_million)
maximum_number = max(list_1_to_million)
total = sum(list_1_to_million)
print(minimum_number, maximum_number, total)

tuple_of_food_items = ("Daal Baati", "Gobi Manchurian Dry", "Chinese Bhel", "Spicy Chicken Drumsticks", "Shrimp Fried")

print("Original Menu:")
for food in tuple_of_food_items:
  print(food)

# Trying to modify an item (Python will raise an error)
tuple_of_food_items[0] = 'Sushi'

new_tuple_of_food_items = ("Sushi", "Burger", "Pancake", "Pizza", "Raabdi")

print("\nNew Menu:")
for food in new_tuple_of_food_items:
  print(food)'''

