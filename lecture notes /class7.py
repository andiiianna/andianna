# warm up questions

def is_less_than_10_or_greater_than_100(num):
    return num < 10 or num > 100
print(is_less_than_10_or_greater_than_100(109))

def sum_of_squares(n):
    total = 0
    for i in range(1, n +1 ): #range stops at second to last number so if it was range (1,4) it puld br 1,2,3 so we need to add the n plus 1
        total += i ** 2
    return total 
print(sum_of_squares(3))

def multiply_until_1000(n):
    total = n
    while total < 1000:
        total *=2
    return total
print(multiply_until_1000(2))

#dictionaries 
# lists- a collections of items stored in a single variable 
# orders, changeable, and use sqaure brackets 
# pythong starts counting at very, so the frist object in your list, pythong is going to read it as list[0]

list = ["purple", "pink", "black"]
print(list[1])
print(list[-1])
list.insert(0,"blue") #(index, item)to insert and item in the lsit 
list.append("brown") #ads an item to the end of the list 
for colors in list:
    print(colors)

#slicing- grabing a portion of a list 

list = [12,14,16,18,10]
#i want to only get the miffle three numbers 
print(list[1:4])#remember python starts at 0, so the second number is in the 1 spot, the ending index isn't inclusive, so itll give me the 4th index-1, so the third index

nums = [1,2,3,4,5]
sub_nums = nums[1:4]
print(sub_nums)

# striding- to grab a portion of a list with a step pattern
list = [12,14,16,18,20,22]
# i want every other numebr of the list
print(list[::2])
#every other number after the first
print(list[1::2])

nums = [1,2,3,4,5,6,7,8,9,10]
print(nums[0:8:2])#starting at 0 print every other number up until the 8 index, rememebr not gonna give us the eigth one, stops at index 7

letters = ["a","b","c","d","e","f","g"]
print(letters[1:5])#slice from b to e
print(letters[1::2])#gert every second letter
# letters.reverse()#reverses the list 
# print(letters)
print(letters[-3:])#prints the last three 

#dictionaries- a type of list they look like names={"first":"mias", "middle":"maries", "last": "gonzales"}
#the kesy are "first" "middle" and "last"
# the values are "mia", "maries" and "gonzales"

pet = {"name":"Luna", "type":"cat", "age":3}
print(pet.items())#give you all the keys and their associated values in a tuple

print(pet["name"])#print the pet name
pet["age"] = 4 #changing the age to four 
pet["favorite toy"] = "string" #adding a new key-value 

#printing all key value pairs in a loop

for key,value in pet.items():
    print(f"{key}: {value}")

import time
print("Fast action...")
time.sleep(5) #pauses running the codefor five second
print("Done!")