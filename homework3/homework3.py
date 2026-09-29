# 3.1 Say Goodbye 

def say_goodbye(name):
    print("Goodbye,", name)

# 3.1 Area of a Circle 

def area_of_circle(radius):
    radius = int(radius)
    print(3.14 * radius ** 2)
    return  3.14 * radius ** 2  # i had to add the return in order for it to print the result in the outcome, before i added this it was saying "The result of the Area of a Circle 3.2 with radius = 3 is None"

# 4.2 Subtract, Multiple and Divide 

def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


# 5.1 What Should I Wear? 

temp = [60,63,54,56,68,74,70]
def high_low(temp):
    return min(temp), max(temp)
print(high_low(temp))

# 5.2 Check if it's the Weekend

def is_weekend(day):
    if day == 6 or day == 7:
        return True 
    else: 
        return False


# 5.3 Fuel Efficiency Calculator 

def fuel_efficiency(m, g):
    return m / g


# 5.4 Secret Code

def secret_code(int):
    last_number = int % 10
    beginning_numbers = int // 10
    return str(last_number) + str(beginning_numbers)


# 6.1 Oski Stole Your Power 

def powers(x, y):
    result = 1
    for i in range(y):
        result = x * result 
    return result 


# 6.2.1 For Loops

list1 = [2, 1, 6, 8, 10]
def minimum_for(list1):
    minimum = list1[0]

    for number in list1:
        if number < minimum: 
            minimum = number 
    return minimum 


def maximum_for(list1):
    maximum = list1[0]

    for number in list1: 
        if number > maximum:
            maximum = number 
    return maximum 


# 6.2.2 While Loops

list2 = [2,1,3,6,5]
def minimum_while(list2):
    minimum = list2[0]
    i = 0
    while i < len(list2):
        if list2[i] < minimum:
            minimum = list2[i]
        i = i +1
    return minimum

def maximum_while(list2):
    maximum = list2[0]
    i = 0
    while i < len(list2):
        if list2[i] > maximum:
            maximum = list2[i]
        i = i +1 
    return maximum


# 6.2 Calculate the sum 

def digits_sum(num):
    sum = 0 
    while num > 0:
        num2 = num % 10 
        sum = sum + num2 
        num = num // 10
    return sum 

radius = int(3) 
result = area_of_circle(radius)

print(f"The result of the Area of a Circle 3.2 with radius = {radius} is {result}.")
