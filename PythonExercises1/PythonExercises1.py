
# 1 Question: There are four numbers: 1, 2, 3, 4. How many different three-digit numbers can be formed without repeated numbers? What are the numbers?

# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if (i != k) and (i != j) and (j != k):
#                 print (i,j,k)

#------------------------------------------------------------------

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

#------------------------------------------------------------------

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

#------------------------------------------------------------------

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

#------------------------------------------------------------------

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

#------------------------------------------------------------------

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

#------------------------------------------------------------------

# 7 Question: Output 9*9 multiplication table.

# for i in range(1, 10):
#     print() #new line = \n
#     for j in range(1, i+1):
#         print ("%d*%d=%d" % (i, j, i*j), end=" " )
                
#------------------------------------------------------------------

# 8 Question: Pause output for one second

# import time

# myD = {1: 'a', 2: 'b'}
# for key, value in dict.items(myD):
#     print(key, value)
#     time.sleep(1)
                
#------------------------------------------------------------------

# 9 Question: Input three integers x, y, z, and output them from small to large.

# numbers = []
# for i in range (3):
#     x = int(input('Integers: \n'))
#     numbers.append(x)

# numbers.sort()
# print (numbers)
               
#------------------------------------------------------------------

# 10 Question: Pause the output for 5 seconds and format the current time.

# import time

# print (time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
# time.sleep(10)
# print (time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
               
#------------------------------------------------------------------

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

# 13 Question:














