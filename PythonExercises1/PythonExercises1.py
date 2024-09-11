
#Question: There are four numbers: 1, 2, 3, 4. How many different three-digit numbers can be formed without repeated numbers? What are the numbers?

# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if (i != k) and (i != j) and (j != k):
#                 print (i,j,k)

#------------------------------------------------------------------

#Question: The bonuses issued by the company are based on profit commission. When the profit (I) is less than or equal to 100,000, the bonus can be increased by 10%; when the profit is higher than 100,000 and lower than 200,000, the portion below 100,000 is increased by 10% and the portion above 100,000 is increased by 7.5%; when the profit is between 200,000 and 400,000, the portion above 200,000 is increased by 5%; when the profit is between 400,000 and 600,000, the portion above 400,000 is increased by 3%; when the profit is between 600,000 and 1 million, the portion above 600,000 is increased by 1.5% and when the profit is higher than 1 million, the portion above 1 million is increased by 1%. Enter the profit I of the month from the keyboard and calculate the total amount of bonuses that should be issued?

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

#------------------------------------------------------------------

#Question: An integer, when adding 100, it is a perfect square number, and when adding 168, it is another perfect square number. What is the integer?

# Program analysis:

# Assume that the integer is x.

# 1. Then: x + 100 = n^2, x + 100 + 168 = m^2

# 2. Calculate the equation: m^2 - n^2 = (m + n)(m - n) = 168

# 3. Set: m + n = i, m - n = j, i * j = 168, at least one of i and j is an even number

# 4. It can be obtained: m = (i + j) / 2, n = (i - j) / 2, i and j are either both even numbers or both odd numbers.

# 5. From 3 and 4, we can know that i and j are both even numbers greater than or equal to 2.

# 6. Since i * j = 168, j>=2, then 1 < i < 168 / 2 + 1.

# 7. Next, loop through all the numbers of i.

# Floating point numbers (i.e. decimals) are not always represented exactly in Python. Because computers store numbers in binary, some decimal fractions cannot be stored exactly as binary numbers, which can cause precision issues. Floating point operations may produce approximate values ​​rather than exact values, especially when performing operations such as square roots.

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

#------------------------------------------------------------------

#Question: Input a certain year, month and day, and determine which day of the year it is?

def calculate_days():
    year = int(input('year: '))
    month = int(input('month: '))
    day = int(input('day: '))
    month_day = (0,31,59,90,120,151,181,212,243,273,304,334)

    if 0 < month <= 12:
        which_day = month_day[month - 1]
    else:
        print ('Month must be between 1 and 12')
        return

    which_day += day

    if (year % 400 == 0) or (year % 4 == 0) and (year %100 != 0):
        if month > 2:
          which_day += 1
    
    print(f"It is the {which_day}th day of the year.")
    return which_day

calculate_days()