
# Question 1
print("Name: Dick Smith")
print("\n")
print("Address: 120E, 87th Street,")
print("\n")
print("\tNew York 10128.")
print("\n")
print("Phone: +440-995-5900")
print("\n")
print("My College major is Object Oriented Programming System (OOPS))")

# Question 2
amount_of_sales = float(input("Enter the projected amount of sales: ")) # asking for the input and then converting it into float datatype
print(amount_of_sales) # printing the amount_of_sales


# Question 3
tip_percentage = 15 # tip percentage that is predefined in the question
sales_tax_percentage = 7 # sales tax percentage that is predefined in the question
amount_of_meal = float(input("Enter the price of meal that you purchased: ")) # asking the user for the input and converting that to float datatype

tip = (15/100) * amount_of_meal # calculating the tip
sales_tax = (7/100) * amount_of_meal # calculating the sales tax
total_amount_to_be_paid = amount_of_meal + tip + sales_tax # total amount that needs to be paid 

# printing all the necessary things to output
print("The price of the meal was" + ' ' + "$" + str(amount_of_meal))
print("The tip added was" + ' ' + "$" + str(tip))
print("The sales tax added was" + ' ' + "$" + str(sales_tax))
print("The total amount that needs to be paid is" + ' ' + "$" + str(total_amount_to_be_paid))

