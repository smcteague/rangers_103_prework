# Question 1:
# Write a function to print "hello_USERNAME!".
# USERNAME is the input of the function.
def hello_username(user_name):
    print(f"hello_{user_name.upper()}!")

# =====================================================================

# Question 2:
# Write a python function, first_odds that prints the odd numbers from 
# 1-100 and returns nothing.
def first_odds():
    for num in range(101):
        if num % 2 == 1:
            print(num) 

# =====================================================================

# Question 3:
# Please write a Python function, max_num_in_list to return the max 
# number of a given list. 
def max_num_in_list(a_list):
    return max(a_list)

# =====================================================================

# Question 4:
# Write a function to return if the given year is a leap year. A leap 
# year is divisible by 4, but not divisible by 100, unless it is also 
# divisible by 400. The return should be boolean Type (true/false).
def is_leap_year(a_year):
    if (a_year % 4 == 0) \
        or ((a_year % 400 == 0) \
        and not (a_year % 100 == 0)):
        return True
    else:
        return False

# =====================================================================

# Question 5:
# Write a function to check to see if all numbers in list are 
# consecutive numbers. For example, [2,3,4,5,6,7] are consecutive 
# numbers, but [1,2,4,5] are not consecutive numbers. The return should 
# be boolean Type.
def is_consecutive(a_list):
    a_list.sort()
    num_pop_last = a_list.pop()
    while a_list:             
        num_pop_first = a_list.pop()
        if num_pop_last - num_pop_first == 1:
            num_pop_last = num_pop_first
            result = True
        else:
            result = False
            break # CORRECTION
    if result == True:
        return True
    else:
        return False

