# Functions + Conditionals + Loops

# functions 
# return statements make the function more reusable
# if- checks if condition is true
#elif-if first if statement is false, do this 
#else- if it doesnt mean if or elif contidion do this 

def is_num_positive(num):
    if num > 0:
        return "positive"
    elif num < 0:
        return "negetive"
    elif num == 0:
        return "zero"

print(is_num_positive(0))

# for loops- when you know exactly how many times you want to repeat something 
    #syntax-    for variable in object:
    #              do something 
# while loops- when you want to repeat something until something changes
    #syntax-    i = 10
    #           while i > 0:
    #               print(i)
    #               i -=1  (same as i = i - 1)

def temp_check(temp):
    if temp > 65 and temp < 85:
        return "It's warm today"
    elif temp > 80:
        return "It's hot today"
    elif temp < 65:
        return "It's cold today"
    #could also do an else statemnt that retunrs its cold today instead of seconf elif
print(temp_check(70))

