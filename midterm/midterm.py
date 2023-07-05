'''# Question 1
# function that calculates the factorials
def get_factorial(n):
    if (n == 0):
        return 1
    else:
        factorial = 1
        for i in range(1, n + 1):
            factorial = factorial * i 

        return factorial

# combination function that uses n!/k!(n-k)!
def combination(n, k):
    numerator = get_factorial(n)
    denominator = get_factorial(k) * get_factorial(n - k)

    return numerator / denominator

# main function
def main():
    n = int(input("Enter the n things: "))
    k = int(input("Enter the k times: "))
    print(combination(n, k))

if __name__ == "__main__":
    main()

# Question 2
def LCM(a, b):
    maximum_number = max(a, b)
    lcm = maximum_number
    while True:
        if (lcm % a == 0 and lcm % b == 0):
            break

        lcm += maximum_number

    return lcm

def main():
    number_1 = int(input("Enter the number: "))
    number_2 = int(input("Enter another number: "))
    lowest_common_multiple = LCM(number_1, number_2)
    print(f"The lowest common multiple of {number_1} and {number_2} is {lowest_common_multiple}.")

if __name__ == "__main__":
    main()

# Question 3
import math

def compute_prime_numbers():
    prime_numbers = []
    for n in range(2, 21):
        prime = True
        for i in range(2, int(math.sqrt(n)) + 1):
            if (n % i == 0):
                prime = False
        
        if (prime):
            prime_numbers.append(n)
    
    return prime_numbers

def main():
    nums = compute_prime_numbers()
    print(f"The prime numbers from 2 to 20 are {nums}.")

if __name__ == "__main__":
    main()

# Question 4
def calculate_x(x):
    result = 3 * x + 2
    for i in range(1, 9):
        if (i % 2 != 0):
            result = result * x
        elif (i == 2):
            result = result - 5
        elif (i == 4):
            result = result - 1
        elif (i == 6):
            result = result + 7
        elif (i == 8):
            result = result - 6 
    return result

def main():
    x_value = int(input("Enter the x value: "))
    final_result = calculate_x(x_value)
    print(f"The value of x for ((((3x + 2)x - 5)x - 1)x + 7)x - 6 is {final_result}.")

if __name__ == "__main__":
    main()

# Question 5 
def get_gcd(n, d):
    if (n > d):
        while(True):
            if (d == 0):
                return n
            else:
                remainder = n % d
                n = d
                d = remainder
    elif (d > n):
        while (True):
            if (n == 0):
                return d
            else:
                remainder = d % n
                d = n
                n = remainder

def reduce_fraction(nu, de):
    gcd = get_gcd(nu, de)
    numerator = nu / gcd
    denominator = de / gcd 

    return numerator, denominator

def get_numerator_and_denominator(frac):
    numerator = ""
    denominator = ""
    j = 0
    for i in frac:
        if (i == "/"):
            numerator = frac[0:j]
            denominator = frac[j+1:]
        j += 1
    
    return numerator, denominator

def main():
    fraction = str(input("Enter a fraction: "))
    num, den = get_numerator_and_denominator(fraction)
    numerator, denominator = reduce_fraction(int(num), int(den))
    print(f"The lowest term: {int(numerator)}/{int(denominator)}")

if __name__ == "__main__":
    main()'''


# Question 6
import math

# prints the star pattern
def print_pattern(height):
    middle_point = int(math.ceil(height / 2))
    stars = height

    for h in range(1, height + 1):
        if (h < middle_point):
            space_before_stars = int((height - stars) / 2)
            space_after_stars = int((height - stars) / 2)

            for _sp_ in range(0, space_before_stars):
                print(" ", end="")
            
            for _st_ in range(0, stars):
                print("*", end="")

            for _spa_ in range(0, space_after_stars):
                print(" ", end="")
            
            print("\n")

            stars = stars - 2
        
        elif (h == middle_point):
            stars = 1
            space_before_stars = int((height - stars) / 2)
            space_after_stars = int((height - stars) / 2)

            for _sp_ in range(0, space_before_stars):
                print(" ", end="")
            
            for _st_ in range(0, stars):
                print("*", end="")

            for _spa_ in range(0, space_after_stars):
                print(" ", end="")
            
            print("\n")

            stars = stars + 2
            
        elif (h > middle_point):
            space_before_stars = int((height - stars) / 2)
            space_after_stars = int((height - stars) / 2)

            for _sp_ in range(0, space_before_stars):
                print(" ", end="")
            
            for _st_ in range(0, stars):
                print("*", end="")

            for _spa_ in range(0, space_after_stars):
                print(" ", end="")
            
            print("\n")

            stars = stars + 2

def main():
    height_of_pattern = int(input("Enter the height: "))
    print_pattern(height_of_pattern)

if __name__ == "__main__":
    main()
