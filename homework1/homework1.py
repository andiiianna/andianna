# File: hoemwork1.py 

# --- Variables and Data Types ---

a = 10 
print(a)
print(type(a)) # a is an integer, a whole number with no deicmals 

b = 1.5
print(b)
print(type(b)) # b is a float, a number with decimals

c = 3j
print(c)
print(type(c)) # c is a complex number, a number with a real and imaginary part (j)

d = "hello"
print(d)
print(type(d)) # d is a string, a sequence of characters/words/texts 

e = [1, 2, 3]
print(e)
print(type(e)) # e is a list (with a colelction of integers), a collection of items stored in a container (the brackets) and can be of any variation of types 

f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f)) # f is a dict (dictionary), acts like an actual dictionary, if you look up a word (key) you will get the definition (value)

g = (1, 2)
print(g)
print(type(g)) # g is a tuple, a list that cannot be changed after you create it (immutable- cannot add, remove, or change items once the tuple is made) 

h = ["apple", "banana", "strawberry"]
print(h)
print(type(h)) # h is a list, with a collection of strings 

i = True
print(i)
print(type(i)) # i is a bool (boolean), a data type that can only be True or False

j = None
print(j)
print(type(j)) # j is a NoneType, says that there is no vlaue associated with the variable

k = [True, "blue", 12]
print(k)
print(type(k)) # k is a list (with a colelction of a boolean, string,and an integer)

l = str(14)
print(l)
print(type(l)) # l is a string, using "str()" to change the integer, 14, into a string 

m = 1e4
print(m)
print(type(m)) # m is a float, the "e" represents "ten to the power of" so in this case it would be 10^4 

#1 I found 9 different data types 

#2 int, float, complex, str, list, dict, tuple, bool, NoneType

#3 b and m are both floats, d and l are both strings, e, h and k are all lists 

#4 l is a string, it is not an integer because it was converted to a string by doing str()

#5 I'm choosing the dats type range 

n = range(1, 5)
print(*n) # when i tried without *, it just printed "range(1, 5)", need the * or "list(n))" to actually print the sequence of numbers between 1 and 5
print(type(n)) # n is a range, represents a sequences of integers between the starting number (first number) and final number(last number). if you only give it one number, it will start at zero and end with the number you gave it.

# --- Booleans ---

10 > 9
print(10 > 9) # true, becuase 10 is greater than 9 

10 == 9 
print(10 == 9) # false, because 10 does not equal 9 

10 <= 9
print(10 <= 9) # false, becuase 10 is not less than or equal to 9

bool("abc")
print(bool("abc")) # true, because the string is not empty, python considers any non-empty string to be true

bool(123)
print(bool(123)) # true, because the integer is not zero, python considers any non-zero integer to be true

bool(["apple", "cherry", "banana"])
print(bool(["apple", "cherry", "banana"])) #true, because the list is not empty, python considers any non-empty list to be true
            
bool(True)
print(bool(True)) #true, because the boolean is True

bool(False)
print(bool(False)) # false, because the boolean is False

bool(0)
print(bool(0)) # false, because the integer is zero 

bool("")
print(bool("")) # false, becuase the string is empty 

bool(" ")
print(bool(" ")) # true, because the string has a space in it, so its not empty 
      
bool(())
print(bool(())) # false, because the tuple is empty  

bool([])
print(bool([])) # false, because the list is empty

bool({})
print(bool({})) # false, because the dictionary is empty

bool(True and False)
print(bool(True and False)) # false, because when there is "and", that means both statements have to be true, but in this case one of them is false, so the whole statement is false 

bool(True and True)
print(bool(True and True)) # true, becuase there is an and, and sicce both statements are true, the whole statement is true 

bool(False and False)
print(bool(False and False)) # false, because there is an and, and since both statements are false, the whole statement is false

bool(True or False)
print(bool(True or False)) # true, because when there is "or", that means at least one statement has to be true, and since one of them is true, the whole statemenbt is true 

bool(True or True)
print(bool(True or True)) # true, because there is an "or", and since at least one statement is true (in this case both are), the whole statement is true

bool(False or False)
print(bool(False or False)) # false, because there is an "or", and neither statements are true, so the whole statement is false

bool(not(False))
print(bool(not(False))) # true, because the "not" is like th eopposite of whats inside, the oposite of false, is true 

bool(not(True))
print(bool(not(True))) # false, becauase there is a "not", if its not true, then it is false 

# I noticed that there in order to be true there needs to some sort of statement, for example, you can't have an emoty string or dictionary ect.

# the bool(" ") suprised me, i thought it would come out false, but i guess it amkes sence because the string technacally isnt empty, it has a space in it 

# bool(not(True and False)) is true, because the "not" is like the opposite of whats inside, and since True and False is false, the opposite of that is true
bool(not(True and False))
print(bool(not(True and False))) 

# bool(not(" ")) is false, because bool(" ") is true, and not true is false
bool(not(" "))
print(bool(not(" "))) 

# --- Operators ---

# ---arithmetic operators--- 

print(10 + 5) # 15, + performs addition 

print(10 - 5) # 5, - performs subtraction

print(2 * 4) # 8, * performs multiplication

print(6 / 3) # 2.0, / performs division with the remainders after the ".", so for this example it gives back 2.0, because 3 goes into 6 exactly 2 times

print(5 % 2) # 1, % gives you the remainder after dividing the frist tnumber by the second, int his example 2 goes itno 5 twice with a remainder of 1, so it will just print 1

print(3 ** 2) # 9, ** is what tou use for exponents, so in this case it printes 3^2, which was nine

print(15 // 2) # 7, // performs division, but wont give you a remainder, and will round down to the nearest integer 

# ---comparison operators---

print(5 == 2) # false, == compares two values to see if they are equal, will give you true if they are equal, or false if they are not equal

print( 10 != 10) # false, != says "not equal to", in this case it was false bcasue 10 is equal to 10, but would be true if we wrote 11 != 10 

print(2 < 5) # true, < "less than", in this case it was treu becasue 2 is less than 5

print(12 > 5) # true, > "greater than", this was also true becasue 12 is greater than 5

print(5 <= 6) # true, <= "less than or equal to", this was treu becasue 5 is less than 6, would also be true if you did 6<=6

print(1 >= 10) # false, >= "greater than or equal to", this was false bcause 1 is not grater than or equal to 10

# ---assignment operators---

x = 5
x += 5 
x -= 4
x *= 3
print(x) # printed 18, because it goes down the line, frist x was just 5, but thne it added 5 to the last x, which now made x=10, then it subtracted 4, now x=6, then multiplied by 3, and finally x=18, and printed that last x 

# ---logical operators---

#1 the and operator says the statement is true if both the left and rigth sides are true 
x = 6
bool(5 < x and 6 <= x)
print(bool(5 < x and 6 <= x)) # results in true 
print(bool(5 > x and 6 <= x)) # results in false

#2 the or operator says the statement is true if at least one side is true

print(5 == 5 or 4 == 5) # results in true 
print(5 < 4 or 3 > 4) # results in false

#3 the not operator says to print of opposite of the statement inside the ()

print(not(5 < 4 or 3 > 4)) # results in true 
print(not(5 == 5 or 4 == 5)) # results in false

#1 / is division that will give you the quotient and the remainder in this fomr q.r, // is also a form of divison, but it only gives you the quotient 

#2 % gives you just the remainder afetr dividing the two numbers, while // gives you jus the quotent after dividing 

#3 i would use %

print(10 % 3) #prints back 1, the remainder 

#4 assingment operators initially assing a value to a varible, and it will replace the valure of the varible after each step

# ---strings---

my_string = "hello"

print(my_string) # prints: hello

print(my_string[0]) # prints: h

print(my_string[1]) # prints: e

print(my_string[2]) # prints: l

print(my_string[3]) # prints: l

print(my_string[4]) # prints: o 

print(my_string[-1]) # prints: o

print(my_string[1:3]) # prints: el

print(my_string[0:5:2]) # prints: hlo

print(len(my_string))

print(my_string + " goodbye") # prints: hello goodbye 

print (7 * my_string) # prints: hellohellohellohellohellohellohello

#1 slicing is when you want to return a range or part of the string. the 9th manipulation sliced the string to give us every second letter form 0 to 5 

#2 printed: Hello, my name is Oski

name = "Oski"
print("Hello, my name is", name)

#3 Printes: Hello, my anme is Oski 

name = "Oski"
print(f"Hello, my name is {name}")

#4 the result in the same outcome, but the f string allows you so join the varibales and text, you just need to out {} aorund the varibale   

# ---Terminal Commands---

# 1) cd
# change directories, use it to move from one folder to another 
# example: cd Desktop

# 2) ls
# lists out the files and folders in your currect directory 
# example(already in Desktop): ls  (just type ls and itll give you the list)

# 3) ls -a
# a list of everything including the hidden files 
# example( already in Desktop): ls -a (just type ls -a and itll give you the list of hiddne and unhidden files)

# 4) mkdir
# make directory: makes a new directory/folder
# example: mkdir homework2 (will create a folder called "homework")

# 5) cat 
# displayd what is inside the file 
# example: cat astro98_notes (displays what you have wrrittne in astro_notes file)

# 6) pwd
# print working directory: tells you which directory you are currently in 
# example: pwd (might give back something like /andiiianna/python_decal_fa26/homework1)

# 7) cd..
# will mvoe you up one directory from the current one 
#example: if you are in /andiiianna/python_decal_fa26/homeowork1/ and you cd.., you will noe be in /andiiianna/python_decal_fa26/

# 8) cd. 
# moved stuff intot he directly you are currently in 
# example: if you are in desktop folder and you cd file.txt ., it will copy that file and move it into your desktop directory 

# 9) cd ∼
# this will take you back to your home directory 
# example: if your not in your home directory use cd ∼ and it will take you to your home directory

# 10) cp
# copies a file or directory 
# example: cp homeowkr1.py Documents/ (this will make a copy of my hoemwork1 file into my documents file, while the original file inside python_decal_fa26 still exists )

# 11) mv
# moves a folder or file somewhere else 
# example: mv homework1.py Documents/ (this will mvoe my homewokr1 file from its original location (python_decal_fa26) into my Documents directory)
# it can also be used to rename files
# example: mv homework1.py homeworkone.py (this will rename the files to the second name)

# 12) rm
# removes: deletes a file, be careful because it doesn't jut move them to trash bin, it actually completely removes them
# rm homeowkr1.py (this would completely erase the entire file and all my work :(( )

# 13) clear 
# clears the text currently displayed in the terminal 
#  used thsi alot during this homeowkr because I had to run the code so many times, you just type clear into the terminal and press enter and itll clear the preivous outputs  

# 14) grep
# this will search for a pattern in the texts 
# example: if you had a file named "ages.txt" with a list of peoples names and ages and you did grep 21 ages.txt, it would give you a list with eveyone in that file who had the age 21 

#1 touch 
# this creates a new empty file 
# example: touch homework2.txt (will create an empty text file wiht the name hoemwork2)

#1 head 
# this shows the frist few lines of a file
# example: head homeowork1.py (instead of showing me all 330 liens, it'll only show me the frist few)

#1 man
# shows the manual/help page for a command
# example man ls (this will give oyu information about how ls works and how to use it)

#2 the difference between ls and ls -a is that ls will only show you the unhidden files and folders in your directory, but ls -a will show you all the hidden and unhidden files/folders in the directory 

#3 a file that you don't really need to interact with directly it is normaly for settings or conifugration information, it is considered hiddne if there is a "." in front of it

#4 "-l" used after ls to show more detailed information about each file such as the owner, size and date mdified 
#4 "-i" used after rm to ask for permission to delete something, if you do rm -i homeoworkone.py itll ask frist "remove hoemworkone.py?" and you can type yes or no
#4 "-n" used after cat, and it adds a number to every line in the file 
