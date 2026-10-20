
#3.1 LIST OPERATIONS 

list1 = ["pasta", "tomato", "avacado", "banana", "blueberries"] 

print(list1[1])

print(list1[-1])

list1.append("chicken")

list1.insert(0, "apple")

del list1[2]

print(len(list1))

for i in list1:
    i = i.upper()
    print(i)

first_and_last = list1[::len(list1)-1]

if "potato" in first_and_last:
    print("A potato!")
else:
    print("No potato!")



#3.2 SLICING AND STRIDING 

numbers = list(range(0, 21))

def get_first_fifteen(numbers):
    return numbers[:15] 
lst = get_first_fifteen(numbers)


def get_every_5th(lst):
    return lst[::5]
lst2 = get_every_5th(lst)
print(get_every_5th(lst))


def reverse_and_stride(lst2):
    lst2.reverse()
    return lst2[::3]

print(reverse_and_stride(lst2))


#3.3 NESTED LISTS 

numbers = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
print(numbers[2]) 
print(numbers[1][1]) 
numbers.append([10, 11, 12])

def sum_nested(numbers):
    total = 0
    for row in numbers:
        total = sum(row)
        print(total)
print(sum_nested(numbers))


#3.4 CREATE A 5X5 LIST  

def create_5x5_list():
    list_5x5 = []
    for i in range(5):
        row = []
        for j in range (1,6):
            row.append(i * 5 + j)
        list_5x5.append(row)
    return list_5x5
list_5x5 = create_5x5_list()
print(create_5x5_list())




def multiple_of_three(list_5x5):
    for row in list_5x5:
        for i in range(5):
            if row[i] % 3 == 0:
                row[i] = "?"
    return list_5x5
updated_list = multiple_of_three(list_5x5)
print(updated_list)

def adding_elements(updated_list):
    total = 0
    for row in updated_list:
        for num in row:
            if num != "?":
                total += num 
    return total            
            
print (adding_elements(updated_list))


# 4 DICTIONARIES

ages = {"Katie": 30,
        "Mariam": 42,
        "Safia": 24, 
        "Mira": 48}
print(ages["Katie"])
ages["Mira"] = 100
ages["Milana"] = 52 
del ages["Mariam"]
print(ages)

for key, value in ages.items():
    print(f"{key},{value}")


