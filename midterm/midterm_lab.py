'''# Question 1
def print_days():
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    for day in days:
        print(f"One of the months of the year is {day}.")

print_days()

# Question 3 
def division_check():
    numbers_divisible = []
    for i in range(2, 101):
        if not i in numbers_divisible:
            if (i % 2 == 0 or i % 3 == 0 or i % 5 == 0):
                numbers_divisible.append(i)
    
    return numbers_divisible

def main():
    print("These are all the numbers that are divisible by 2 or 3 or 5.")
    print(division_check())

if __name__ == "__main__":
    main()

# Question 4
def get_ascii_value(character):
    return ord(character)

def count_letters_digits_symbols(string):
    letters_count = 0
    numbers_count = 0
    symbols_count = 0

    for char in string:
        char_ascii_value = get_ascii_value(char)
        if (char_ascii_value <= 57 and char_ascii_value >= 48):
            numbers_count += 1
        elif ((char_ascii_value >= 97 and char_ascii_value <= 122) or (char_ascii_value >= 65 and char_ascii_value <= 90)):
            letters_count += 1
        else:
            symbols_count += 1
    
    return letters_count, numbers_count, symbols_count

def main():
    user_string = str(input("Enter a string: "))
    l_count, n_count, s_count = count_letters_digits_symbols(user_string)
    print(f"Letters in the string: {l_count}")
    print(f"Numbers in the string: {n_count}")
    print(f"Symbols in the string: {s_count}")

if __name__ == "__main__":
    main()

# Question 5
def find_occurence(string, substring):
    occurrence = 0
    i = 0 
    j = 5
    five_char_of_main_string = string[i:j]
    length_of_string = len(string)

    while(j <= length_of_string):
        if (five_char_of_main_string == substring):
            occurrence += 1
        i += 1
        j += 1
        five_char_of_main_string = string[i:j]

    result = f"The number of times string '{substring}' occurs in the string '{string}' is {occurrence}."
    return result

print(find_occurence("AayusAayusAayusAayus", "Aayus"))'''

# Question 2
import random
def generate_random_number():
    return random.uniform(0, 1)

def main():
    random_number = generate_random_number()
    if (random_number >= 0 and random_number < 1/12):
        print("The hour prediction is 1.")
    elif(random_number >= 1/12 and random_number < 2/12):
        print("The hour prediction is 2.")
    elif(random_number >= 2/12 and random_number < 3/12):
        print("The hour prediction is 3.")
    elif(random_number >= 3/12 and random_number < 4/12):
        print("The hour prediction is 4.")
    elif(random_number >= 4/12 and random_number < 5/12):
        print("The hour prediction is 5.")
    elif(random_number >= 5/12 and random_number < 6/12):
        print("The hour prediction is 6.")
    elif(random_number >= 6/12 and random_number < 7/12):
        print("The hour prediction is 7.")
    elif(random_number >= 7/12 and random_number < 8/12):
        print("The hour prediction is 8.")
    elif(random_number >= 8/12 and random_number < 9/12):
        print("The hour prediction is 9.")
    elif(random_number >= 9/12 and random_number < 10/12):
        print("The hour prediction is 10.")
    elif(random_number >= 10/12 and random_number < 11/12):
        print("The hour prediction is 11.")
    elif(random_number >= 11/12 and random_number <= 12/12):
        print("The hour prediction is 12.")

if __name__ == "__main__":
    main()
    
