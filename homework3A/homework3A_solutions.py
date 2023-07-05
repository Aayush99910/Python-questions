'''def fib(n):
  # if the n is 0 we return an empty list and similary for 1 we return [0] and for 2 we return [0, 1]
  # else we use the logic
  if n <= 0:
    return []
  elif n == 1:
    return [0]
  elif n == 2:
    return [0, 1]
  else:
    fibonacci_series = [0, 1]
    current_position = 2
    current_number = 0
    next_number = 1

    # looping until the current_position variable is equal to the nth_position variable
    while current_position <= n:
      next_number_after = current_number + next_number # next_number_after is the sum of current_number and next_number
      fibonacci_series.append(next_number_after)
      current_number = next_number # after the sum, current_number is assigned the value of next_number
      next_number = next_number_after # after the sum, next_number is assigned the sum of those two number which was stored in next_number_after
      current_position += 1 # current_position is increamented

    return fibonacci_series

# Testing the function
result = fib(10)
print(result)

def power(x, n):
  powers = []
  for i in range(1, n + 1):
    powers.append(x ** i)
  return powers

# Testing the function
result = power(5, 3)
print(result)

def sum_sq(n):
  sum_of_squares = 0
  for i in range(1, n + 1):
    sum_of_squares = sum_of_squares + i**2
  
  return sum_of_squares

result = sum_sq(2)
print(result)


def sum_cb(n):
  sum_of_cubes = 0
  for i in range(1, n + 1):
    sum_of_cubes = sum_of_cubes + i**3
  
  return sum_of_cubes

result = sum_cb(3)
print(result)

import math # importing math 

# function that gives the factor of a number
def get_factor(n):
  factor = 1
  for i in range(1, n + 1):
    factor = factor * i

  return factor

# sine function 
def sine(x):
  x = math.radians(x) # converting the degree into radian
  total = 0 
  power_number = 3
  # iterating 10 times 
  for i in range(10):
    # first we add the whole x
    if (i == 0):
      total += x
    else:
      # if it is the odd iteration we subtract
      if (i % 2 != 0):  
        factor = get_factor(power_number)
        factor_that_will_be_subtracted = ((x**power_number)/factor)
        total = total - factor_that_will_be_subtracted
        power_number = power_number + 2
      # if it is the even iteration we add
      elif (i % 2 == 0):
        factor = get_factor(power_number)
        factor_that_will_be_added = ((x**power_number)/factor)
        total = total + factor_that_will_be_added
        power_number = power_number + 2
  
  return total

sine_summation = sine(30)
print(sine_summation)'''

import math # importing math

# function that gives the factor of a number
def get_factor(n):
  factor = 1
  for i in range(1, n + 1):
    factor = factor * i

  return factor

def cosine(x):
  x = math.radians(x) # converting the degree into radian
  total = 0
  power_number = 2
  # iterating 10 times 
  for i in range(10):
    # first we add the whole x
    if (i == 0):
      total += 1
    else:
      # if it is the odd iteration we subtract
      if (i % 2 != 0):  
        factor = get_factor(power_number)
        factor_that_will_be_subtracted = ((x**power_number)/factor)
        total = total - factor_that_will_be_subtracted
        power_number = power_number + 2
      # if it is the even iteration we add
      elif (i % 2 == 0):
        factor = get_factor(power_number)
        factor_that_will_be_added = ((x**power_number)/factor)
        total = total + factor_that_will_be_added
        power_number = power_number + 2
  
  return total

cosine_summation = cosine(30)
print(cosine_summation)






  

