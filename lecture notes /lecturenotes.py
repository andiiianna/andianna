#how to write a function that will find the max and min of a list
list = [40,80,10,30,50,20]
list2 = [12,24,64,25]

def minimum(list):
    return min(list)

print(min(list))

def maximum(list):
    return max(list)

print(max(list))

# create a function to determine if a positive integer is a prime number 

def isprime(num)
    if num >= 0 and num != type(int):
        return "try again. choose a new number"
    

# LECTURE 09/30/26

#Practice questions 

#with the function range(), create a list of numbers from 0 to 10 called list1.

list1 = list(range(0,11))
print(list1)

#printing first five 
print(list1[0:5])

#printing every other 
print(list1[::2])

#if you want to print every other but not starting at 0
print(list1[1::2])

nested_list = [[2,4,6], 
               [8,10,12], 
               [14,16,18]]

nested_list[2][1] #would give 16, becasue its the third row and second column, rememeber starts at zero 

stars_data={
    "name":["Sirius", "Vega", "Altair"],
    "magnitude":[-1.46, 0.03, 0.77],
    "distance_ly":[8.9, 25,0, 16.7],
    "constellation":["Canis Major", "Lyra", "Aquila"]
}
for name in stars_data["name"]:
    print(name)
