# 1 Question: There are four numbers: 1, 2, 3, 4. How many different three-digit numbers can be formed without repeated numbers? What are the numbers?

# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if (i != k) and (i != j) and (j != k):
#                 print (i,j,k)

# ------------------------------------------------------------------

# 2 Question: The bonuses issued by the company are based on profit commission. When the profit (I) is less than or equal
# to 100,000, the bonus can be increased by 10%; when the profit is higher than 100,000 and lower than 200,000, the portion
# below 100,000 is increased by 10% and the portion above 100,000 is increased by 7.5%; when the profit is between 200,000 and 400,000,
# the portion above 200,000 is increased by 5%; when the profit is between 400,000 and 600,000, the portion above 400,000 is increased by 3%;
# when the profit is between 600,000 and 1 million, the portion above 600,000 is increased by 1.5% and when the profit is higher than 1 million,
# the portion above 1 million is increased by 1%. Enter the profit I of the month from the keyboard and calculate the total amount of bonuses that should be issued?

# def calculate_bonus(net_profit):
#     net_profit_range = [1000000, 600000, 400000, 200000, 100000, 0]
#     bonus_ratio = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
#     bonus = 0

#     for bonus_index in range(0, 6):
#         if net_profit > net_profit_range[bonus_index]:
#             bonus += (net_profit - net_profit_range[bonus_index]) * bonus_ratio[bonus_index]
#             net_profit = net_profit_range[bonus_index]

#     return bonus

# net_profit = int(input('Enter the net profit: '))
# total_bonus = calculate_bonus(net_profit)
# print(f"Total bonus: {total_bonus}")

# ------------------------------------------------------------------

# 3 Question: An integer, when adding 100, it is a perfect square number, and when adding 168, it is another perfect square number. What is the integer?

# Program analysis:

# Assume that the integer is x.

# 1. Then: x + 100 = n^2, x + 100 + 168 = m^2

# 2. Calculate the equation: m^2 - n^2 = (m + n)(m - n) = 168

# 3. Set: m + n = i, m - n = j, i * j = 168, at least one of i and j is an even number

# 4. It can be obtained: m = (i + j) / 2, n = (i - j) / 2, i and j are either both even numbers or both odd numbers.

# 5. From 3 and 4, we can know that i and j are both even numbers greater than or equal to 2.

# 6. Since i * j = 168, j>=2, then 1 < i < 168 / 2 + 1.

# 7. Next, loop through all the numbers of i.

# Floating point numbers (i.e. decimals) are not always represented exactly in Python. Because computers store numbers
# in binary, some decimal fractions cannot be stored exactly as binary numbers, which can cause precision issues.
# Floating point operations may produce approximate values ​​rather than exact values, especially when performing operations such as square roots.

# import math
# def find_integer():
#     for i in range(2,85): #1 < i < 168 / 2 + 1
#         if 168 % i == 0:
#             j = 168 // i # result 7 // 2; result = 3
#             if i > j  and (i + j) % 2 == 0 and (i - j) % 2 == 0:
#                 m = (i + j) // 2
#                 n = (i - j) // 2
#                 x = n * n -100

#                 if math.isqrt(x + 100) ** 2 == (x + 100) and math.isqrt(x + 100 + 168) ** 2 == (x + 100 + 168): # a ** b =a^b; 2 ** 3 = 8
#                     print(f"x: {x}, m: {m}, n: {n}")

# find_integer()

# ------------------------------------------------------------------

# 4 Question: Input a certain year, month and day, and determine which day of the year it is?

# def calculate_days():
#     year = int(input('year: '))
#     month = int(input('month: '))
#     day = int(input('day: '))
#     month_day = (0,31,59,90,120,151,181,212,243,273,304,334)

#     if 0 < month <= 12:
#         which_day = month_day[month - 1]
#     else:
#         print ('Month must be between 1 and 12')
#         return

#     which_day += day

#     if (year % 4 == 0) and (year %100 != 0) or (year % 400 == 0): # 'and' has higher priority than 'or'
#         if month > 2:
#           which_day += 1

#     print(f"It is the {which_day}th day of the year.")
#     return which_day

# calculate_days()

# ------------------------------------------------------------------

# 5 Question: Fibonacci sequence.

# Program analysis: Fibonacci sequence, also known as the golden section sequence, refers to a sequence of numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

# In mathematics, the Fibonacci sequence is defined recursively:

# F0 = 0 (n=0)

# F1 = 1 (n=1)

# Fn = F[n-1]+ F[n-2](n=>2)

# def fib(n):
#     a,b=1,1

#     for i in range(n-1):
#         a,b = b,a+b
#     return a

# n = int(input('n: '))
# print (fib(n))

# ------------------------------------------------------------------

# 6 Question: Copies the data of one numbers to another list.

# Program analysis: Using list[:].

# a = [1, 2, 3]
# a.append([4, 5])  # 添加一个列表作为元素
# print(a)  # 输出: [1, 2, 3, [4, 5]]，列表作为单个元素被添加
# a = [1, 2, 3]
# a.extend([4, 5])  # 将 [4, 5] 中的每个元素逐一添加
# print(a)  # 输出: [1, 2, 3, 4, 5]


# a = [1, 2, 3]
# b = a[:]
# print (f'b = {b}')

# ------------------------------------------------------------------

# 7 Question: Output 9*9 multiplication table.

# for i in range(1, 10):
#     print() #new line = \n
#     for j in range(1, i+1):
#         print ("%d*%d=%d" % (i, j, i*j), end=" " )

# ------------------------------------------------------------------

# 8 Question: Pause output for one second

# import time

# myD = {1: 'a', 2: 'b'}
# for key, value in dict.items(myD):
#     print(key, value)
#     time.sleep(1)

# ------------------------------------------------------------------

# 9 Question: Input three integers x, y, z, and output them from small to large.

# numbers = []
# for i in range (3):
#     x = int(input('Integers: \n'))
#     numbers.append(x)

# numbers.sort()
# print (numbers)

# ------------------------------------------------------------------

# 10 Question: Pause the output for 5 seconds and format the current time.

# import time

# print (time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
# time.sleep(10)
# print (time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

# ------------------------------------------------------------------

# 11 Question: There is a pair of rabbits. From the third month after birth, they give birth to a pair of rabbits every
# month. After the third month, the little rabbits give birth to another pair of rabbits every month.
# If none of the rabbits die, how many rabbits will there be in total each month?
# Program analysis: The pattern of rabbits is the sequence 1,1,2,3,5,8,13,21....

# while True:
#     months = input("Enter the number of months: ")
#     if months.isdigit() and int(months) > 0:
#         months = int(months)
#         break
#     else:
#         print("Please enter a valid positive integer.")
#
# p1 = 1
# p2 = 2
# for i in range(1, months + 1):
#     print(f'{p1:12d} {p2:12d}', end=" ")
#     if (i % 3) == 0:
#         print('')  # wrapping every 3 lines
#     p1 = p1 + p2
#     p2 = p1 + p2

# ------------------------------------------------------------------

# 12 Question: Determine how many prime numbers there are between 101-200, and output all prime numbers.
# # Program analysis: Method to determine prime numbers: Use a number to divide 2 to sqrt (this number) respectively.
# If it can be divided by an integer, it means that this number is not a prime number, otherwise it is a prime number.
# update to determine how many prime numbers there are between 101 to entered number.

# import math
#
# while True:
#     prime_number = input("Enter the number: ")
#     if prime_number.isdigit() and int(prime_number) > 101:
#         prime_number = int(prime_number)
#         break
#     else:
#         print("Please enter a valid positive integer larger than 101.")
#
# # define a variable to count how many prime numbers
# leap = 0
#
# # 遍历 101 到 prime_number 之间的所有数，检查是否是素数
# for i in range(101, prime_number + 1):
#     is_prime = True  # 假设当前数是素数
#     for j in range(2, int(math.sqrt(i)) + 1):
#         if i % j == 0:
#             is_prime = False  # 该数能被 j 整除，所以不是素数
#             break  # 找到一个因数就可以停止检查
#     if is_prime:  # 如果该数是素数
#         print(f'{i:6d}', end=' ')
#         leap += 1
#         if leap % 10 == 0:  # 每10个素数换行
#             print('')
#
# # 输出结果
# print(f'\nThere are {leap} prime numbers between 101 and {prime_number}.')

# ------------------------------------------------------------------

# extra practices 1-1

# 1. Personal Information
# Write a program that displays the following information:
#  Your name
#  Your address, with city, state, and ZIP
#  Your telephone number
#  Your college major

# def personal_information():
#     name = "ss"
#     address = "123, 456, 789"
#     phone_number = "123-456-789"
#     college_major = "Python_develop"
#
#     print("Personal Information:")
#     print(f"Name: {name}")
#     print(f"Address: {address}")
#     print(f"Phone Number: {phone_number}")
#     print(f"College Major: {college_major}")
#
# if __name__ == "__main__":
#     personal_information()

# ------------------------------------------------------------------

# extra practices 1-2

# 2. Sales Prediction
# A company has determined that its annual profit is typically 23 percent of total sales.
# Write a program that asks the user to enter the projected amount of total sales, then
# displays the profit that will be made from that amount.
# Hint: Use the value 0.23 to represent 23 percent.

# def profit_of_total():
#     total_sales = float(input("Enter the total sales: $"))
#
#     profit = total_sales * 0.23
#
#     print(f"The profit is: ${profit:.2f}")
#
# if __name__ == "__main__":
#     profit_of_total()


# ------------------------------------------------------------------

# extra practices 1-3

# 3. Land Calculation
# One acre of land is equivalent to 43,560 square feet. Write a program that asks the user
# to enter the total square feet in a tract of land and calculates the number of acres in the tract.
# Hint: Divide the amount entered by 43,560 to get the number of acres.

# def acres_calculate():
#     total_square_feet = float(input("Enter the total square feet: "))
#     total_acres = round(total_square_feet / 43560, 2)
#     print(f"The total acres of the land is: {total_acres}")
#
#
# if __name__ == "__main__":
#     acres_calculate()

# ------------------------------------------------------------------

# extra practices 1-4

# 4. Total Purchase
# A customer in a store is purchasing five items. Write a program that asks for the price of
# each item, then displays the subtotal of the sale, the amount of sales tax, and the total.
# Assume the sales tax is 7 percent.

# def purchase_detail():
#     item_1st = float(input("Enter the 1st item's price: "))
#     item_2nd = float(input("Enter the 2nd item's price: "))
#     item_3rd = float(input("Enter the 3rd item's price: "))
#     item_4th = float(input("Enter the 4th item's price: "))
#     item_5th = float(input("Enter the 5th item's price: "))
#
#     subtotal = item_1st + item_2nd + item_3rd + item_4th + item_5th
#     sales_tax = subtotal * 0.07
#     total = subtotal + sales_tax
#
#     print(f"The subtotal of the sale is: ${subtotal:.2f}")
#     print(f"The amount of sales tax is: ${sales_tax:.2f}")
#     print(f"The total cost is: ${total:.2f}")
#
# if __name__ == "__main__":
#     purchase_detail()

# ------------------------------------------------------------------

# extra practices 1-5

# 5. Distance Traveled
# Assuming there are no accidents or delays, the distance that a car travels down the
# interstate can be calculated with the following formula:
# Distance=Speed×Time
# A car is traveling at 70 miles per hour. Write a program that displays the following:
#  The distance the car will travel in 6 hours
#  The distance the car will travel in 10 hours
#  The distance the car will travel in 15 hours

# def distance_traveled():
#
#     speed = 70
#     distance_in_6 = speed * 6
#     distance_in_10 = speed * 10
#     distance_in_15 = speed * 15
#
#     print(f"The distance the car will travel in 6 hours is {distance_in_6}")
#     print(f"The distance the car will travel in 10 hours is {distance_in_10}")
#     print(f"The distance the car will travel in 15 hours is {distance_in_15}")
#
# if __name__ == "__main__":
#     distance_traveled()

# ------------------------------------------------------------------

# extra practices 1-6

# 6. Sales Tax
# Write a program that will ask the user to enter the amount of a purchase. The program
# should then compute the state and county sales tax. Assume the state sales tax is 5
# percent and the county sales tax is 2.5 percent. The program should display the amount
# of the purchase, the state sales tax, the county sales tax, the total sales tax, and the
# total of the sale (which is the sum of the amount of purchase plus the total sales tax).
# Hint: Use the value 0.025 to represent 2.5 percent, and 0.05 to represent 5 percent.

# def calculate_amount():
#
#     amount_purchase = float(input("Enter the amount of purchase: "))
#
#     state_tax = amount_purchase * 0.05
#     county_tax = amount_purchase * 0.025
#     total_tax = state_tax + county_tax
#     total_sale = amount_purchase + total_tax
#
#     print(f"The amount purchase is {amount_purchase:.2f}")
#     print(f"The state tax is {state_tax:.2f}")
#     print(f"The county tax is {county_tax:.2f}")
#     print(f"The total sales tax is {total_tax:.2f}")
#     print(f"The total of sale is {total_sale:.2f}")
#
# if __name__ == "__main__":
#     calculate_amount()

# ------------------------------------------------------------------

# extra practices 1-7

# 7. Miles-per-Gallon
# A car's miles-per-gallon (MPG) can be calculated with the following formula:
# MPG=Miles driven÷Gallons of gas used
# Write a program that asks the user for the number of miles driven and the gallons of gas
# used. It should calculate the car's MPG and display the result.

# def miles_per_gallon():
#
#     miles = float(input("Enter the number of miles driven: "))
#     gallons_used = float(input("Enter the gallons of gas used: "))
#
#     mpg = miles / gallons_used
#
#     print(f"The car's mile per gallon is {mpg:.2f}")
#
# if __name__ == "__main__":
#     miles_per_gallon()

# ------------------------------------------------------------------

# extra practices 1-8

# 8. Tip, Tax, and Total
# Write a program that calculates the total amount of a meal purchased at a restaurant.
# The program should ask the user to enter the charge for the food, then calculate the
# amounts of a 18 percent tip and 7 percent sales tax. Display each of these amounts and
# the total.

# def total_amount_meal():
#
#     food_cost = float(input("Enter the charge for the food is: "))
#     tips = food_cost * 0.18
#     sales_tax = food_cost * 0.07
#
#     total_cost = food_cost + tips + sales_tax
#
#     print(f"The food cost is {food_cost:.2f}")
#     print(f"The tips of the food is {tips:.2f}")
#     print(f"The sales tax of the food is {sales_tax:.2f}")
#     print(f"The total cost of the food is {total_cost:.2f}")
#
# if __name__ == "__main__":
#     total_amount_meal()

# ------------------------------------------------------------------

# extra practices 1-9

# 9. Celsius to Fahrenheit Temperature Converter
# Write a program that converts Celsius temperatures to Fahrenheit temperatures. The
# formula is as follows:
# F=95C+32
# The program should ask the user to enter a temperature in Celsius, then display the
# temperature converted to Fahrenheit.

# def c_to_f():
#
#     celsius = float(input("Enter the Celsius degree: "))
#     fahrenheit = (celsius * 9) / 5 + 32
#
#     print(f"The Fahrenheit temperature is {fahrenheit:.2f}")
#
# if __name__ == "__main__":
#     c_to_f()

# ------------------------------------------------------------------

# extra practices 1-10

# 10. Ingredient Adjuster
# A cookie recipe calls for the following ingredients:
#  1.5 cups of sugar
#  1 cup of butter
#  2.75 cups of flour
# The recipe produces 48 cookies with this amount of the ingredients. Write a program
# that asks the user how many cookies he or she wants to make, then displays the number
# of cups of each ingredient needed for the specified number of cookies.

# def cookie_recipe():
#
#     cookie_needed = int(input("Enter how many cookies you need: "))
#
#     recipes = cookie_needed / 48
#     sugar_cups = recipes * 1.5
#     butter_cups = recipes * 1
#     flour_cups = recipes * 2.75
#
#     print(f"To make {cookie_needed} cookies,")
#     print((f"you need {sugar_cups:.2f} cups of sugar,"))
#     print(f"{butter_cups:.2f} cups of butter,")
#     print((f"and {flour_cups:.2f} cups of flour."))
#
# if __name__ == "__main__":
#     cookie_recipe()

# ------------------------------------------------------------------

# extra practices 1-11

# 11. Male and Female Percentages
# Write a program that asks the user for the number of males and the number of females registered in a class.
# The program should display the percentage of males and females in the class.
# Hint: Suppose there are 8 males and 12 females in a class. There are 20 students in the
# class. The percentage of males can be calculated as 8 ÷ 20 = 0.4, or 40%. The percentage
# of females can be calculated as 12 ÷ 20 = 0.6, or 60%.

# def class_gender_percentages():
#
#     male = int(input("Enter the male number: "))
#     female = int(input("Enter the female number: "))
#     total = male + female
#
#     male_pctg = (male / total) * 100
#     female_pctg = (female / total) * 100
#
#     print(f"Male percentage is {male_pctg:.2f}%")
#     print((f"Female percentage is {female_pctg:.2f}%"))
#
# if __name__ == "__main__":
#     class_gender_percentages()


# ------------------------------------------------------------------

# extra practices 1-12

# 12. Stock Transaction Program
# Last month, Joe purchased some stock in Acme Software, Inc. Here are the details of the
# purchase:
#  The number of shares that Joe purchased was 2,000.
#  When Joe purchased the stock, he paid $40.00 per share.
#  Joe paid his stockbroker a commission that amounted to 3 percent of the
# amount he paid for the stock.
#  Two weeks later, Joe sold the stock. Here are the details of the sale:
#  The number of shares that Joe sold was 2,000.
#  He sold the stock for $42.75 per share.
#  He paid his stockbroker another commission that amounted to 3 percent
# of the amount he received for the stock.
#  Write a program that displays the following information:
#  The amount of money Joe paid for the stock.
#  The amount of commission Joe paid his broker when he bought the stock.
#  The amount for which Joe sold the stock.
#  The amount of commission Joe paid his broker when he sold the stock.
#  Display the amount of money that Joe had left when he sold the stock
# and paid his broker (both times). If this amount is positive, then Joe made
# a profit. If the amount is negative, then Joe lost money.

# def stock_calculate():
#
#     purchase_total = 2000 * 40
#     commission_buy = purchase_total * 0.03
#     purchase_sold = 42.75 * 2000
#     benefit_sale = purchase_sold - purchase_total - commission_buy
#     commission_sale = purchase_sold * 0.03
#
#     benefit_final = benefit_sale - commission_sale
#
#     print(f"The purchase total cost is {purchase_total}")
#     print(f"The commission paid to broker when bought is {commission_buy:.2f}")
#     print(f"The amount when sold is {purchase_sold}")
#     print(f"The commission paid to broker when sold is {commission_sale:.2f}")
#     print(f"The final money left is {benefit_final}")
#
#     if benefit_final > 0:
#         print(f"Joe made a profit.")
#     elif benefit_final <0:
#         print(f"Joe lost money.")
#     else:
#         print(f"Joe broke even.")
#
# if __name__ == "__main__":
#     stock_calculate()

# ------------------------------------------------------------------

# extra practices 1-13

# 13. Planting Grapevines
# A vineyard owner is planting several new rows of grapevines, and needs to know how
# many grapevines to plant in each row. She has determined that after measuring the
# length of a future row, she can use the following formula to calculate the number of
# vines that will fit in the row, along with the trellis end-post assemblies that will need to
# be constructed at each end of the row:
# V=R-2ES
# The terms in the formula are:
#  V is the number of grapevines that will fit in the row.
#  R is the length of the row, in feet.
#  E is the amount of space, in feet, used by an end-post assembly.
#  S is the space between vines, in feet.
#  Write a program that makes the calculation for the vineyard owner. The program
# should ask the user to input the following:
#  The length of the row, in feet
#  The amount of space used by an end-post assembly, in feet
#  The amount of space between the vines, in feet
#  Once the input data has been entered, the program should calculate and display
# the number of grapevines that will fit in the row.


# ------------------------------------------------------------------



# ------------------------------------------------------------------



# ------------------------------------------------------------------




# 13 Question:
