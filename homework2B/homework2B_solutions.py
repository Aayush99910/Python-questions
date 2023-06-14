'''# Question 1
def calculate_slope(x1, y1, x2, y2):
  delta_y = y2- y1 # gets the delta y
  delta_x = x2 - x1 # gets the delta x
  slope = delta_y / delta_x # calculating the slope
  return slope

slope_of_a_line = calculate_slope(5, 6, 10, 10)
slope_of_a_line_1 = calculate_slope(4, 3, 9, 12)
print(f"The slope of the line is {slope_of_a_line}.")
print(f"The slope of the line is {slope_of_a_line_1}.")

# Question 2
from math import sqrt
def Euclidean_dist(x1, y1, x2, y2):
  delta_y = y2 - y1 # getting the delta y
  delta_x = x2 - x1 # getting the delta x

  square_of_delta_y = delta_y**2 # squares of delta_y
  square_of_delta_x = delta_x**2 # squares of delta_x

  distance = sqrt(square_of_delta_x + square_of_delta_y) # getting the distance by using the formula
  return distance

distance = Euclidean_dist(4, 5, 9, 10)
distance_1 = Euclidean_dist(2, 4, 8, 18)
print(f"The distance between the coordinates are {distance}.")
print(f"The distance between the coordinates are {distance_1}.")'''

# Question 2 (b)
# asking the user for how many clusters we have o do
clusters_number = int(input("How many clusters of data you want to calculate the centroids of(if there are 3 clusters enter 3): "))
all_coordinates = []

# looping as per the requirement of the user (if there are 5 clusters it will loop 5 times)
for i in range(clusters_number):
  number_of_data_points = int(input("How many data points are you trying to find the centroids of(if there are 5 (x,y) coordinates enter 5): "))
  coordinates = [] # list that will be  used to store the coordinates 

  # looping as per the requirement of the user (if there are 3 coordinates then it will loop 3 times)
  for number in range(number_of_data_points):
    x_point = float(input("Enter the x coordinate: ")) # letting user enter the x coordinate
    y_point = float(input("Enter the y coordinate: ")) # letting user enter the y coordinate

    coordinate = {"x": x_point, "y": y_point} # making the coordinates into a dictionary
    coordinates.append(coordinate) # appending that dictionary to the list coordinates
    print()

  all_coordinates.append(coordinates) # appending the list of clusters of data in all coordinate list


# calculating the centroid
# looping through the coordinates
for coordinates in all_coordinates:
  sum_x = 0 # sum of the x points
  sum_y = 0 # sum of the y points
  count = 0 # count variable that will store the count of the coordinates
  for coordinate in coordinates: # looping though each coordinate
    sum_x = sum_x + coordinate['x'] 
    sum_y = sum_y + coordinate['y']
    count = count + 1
  
  centroid_x = sum_x / count # finally calculating the centroid of x
  centroid_y = sum_y / count # finally calculating the centroid of y

  print(f"The centroid of {coordinates} is ({centroid_x}, {centroid_y}).") # printing a nice output to the user
    



'''# Question 3
from math import sqrt

def get_factors(number):
  factors = []
  for i in range(1, number+1):
    if (number % i == 0):
      factors.append(i)
  return factors

def prime_factorization(n):
  product = 1
  factors = get_factors(n)
  for factor in factors:
    is_prime = True
    for i in range(2, int(sqrt(factor))+1):
      if factor % i == 0:
        is_prime = False
        break
    
    if is_prime:
      product *= factor
  return product


product_total = prime_factorization(69)
product_total_1 = prime_factorization(35)
product_total_2 = prime_factorization(100)
print(product_total, product_total_1, product_total_2)

# Question 4
def gcd(m ,n):
  if (m > n):
    while (n != 0):
      remainder = m % n
      m = n 
      n = remainder
    return m
  else:
    while (m != 0):
      remainder = n % m
      n = m 
      m = remainder
    return n
  
print(gcd(18, 9))
print(gcd(36, 48))

# Question 5
year = int(input("Enter a year: "))

if (year % 4 == 0):
  if (year % 100 == 0):
    if (year % 400 == 0):
      print("It is a leap year")
    else:
      print("Not a leap year.")
  else:
      print("It is a leap year.")
else:
      print("Not a leap year.")'''
