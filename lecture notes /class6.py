list = [2,3,4,5]
for num in list:
    print(num)

def countdown(num):
    while num > 0:
        print(num)
        num -=1
    print("lift off!")
print(countdown(5))

def count_letters(text):
    count = 0
    for char in text:
        if char.isalpha():
            count +=1 
    return count
print(count_letters("andiannawashere"))

def count_to_ten():
    num = 1
    while num <= 10:
        print(num)
        num += 1
print(count_to_ten())

def mult_of_3_or_5(num):
    if num % 5 == 0:
        print("multiple of five")
    elif num % 3 == 0:
        print("multiple of three")
    else:
        print("neither a multiple of three or five")
print(mult_of_3_or_5(17))

def is_multiple_of_3_or_5(num):
    return num % 3 == 0 or num % 5 == 0
print(is_multiple_of_3_or_5(10))