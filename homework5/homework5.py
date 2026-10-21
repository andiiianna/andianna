# 2.1 VOCABULARY REVIEW 

# Git vs GithHub: Git is a local version control software tool that tracks changed to files, while GitHub is the online place where you store and share your Git repositories 
# Terminal vs Commandline: Terminal is the actual app you use to write code to interact wiht your computer directy, the cammand line is where the cose is actually written. Terminal is like the notebook, but cammandline is the actual line sont he pages, is how I think about it. 
# Local vs Remote Repository: local is local to your computer only and remote is somewhere on a server or the internet (in the cloud)
# Version Control: A feature of Git that keeps track of the history fo your work, so instead of having different files with dfferent names, you'll just have different versions of the same file 
# Staging Area: The place where tyou prepapre and select changed that will be included in your next commit 
# git add: adds changged to the staging area before they are commited 
# git commit: saves the changed to the local repository 
# git push: pushed the local repositories that your added ytour files to in the commit step to a remote repositry, like GitHub
# git status: shows the current status of your repository, and any files that had chnages to them that weren't saved 
# git pull: downloads changes from a remote repositry and puts them in your own local repository 
# pwd: "print working directory" will print the directory you're currently in 
# ls: lists all the files in the repository you're currently in 
# cd: "change directory" will change the directory to whichever one you put after cd
# nano: will create a file that you can start editing right away 
# touch: will create a file, but it won't pop up write away fro you to start editing it
# mv: moves a file or directory to a differnt location, or you can use it to rename files and directories 
# rm: removes a file 
# cat: shows the contents of the file


#2.2 A DIRECTORY TREE
# pwd 
# ls 
# cd .. (now I am in "python_decal") cd brianna_repo (now I adm in "brianna_repo") git pull (will pull changes made to homework.py)
# mv homework.py ∼/python_decal/judy_decal/homework
# first direct yourself to the just_decal repository then do cat homoework.py
# git add . (stages the changed) git commit -m "message to yourself" (saves your changes) git push origin main (pushed local repo to remote repo)
# this error means the remote repository has changes that judy hasnt pulled yer, she needs to pull them first then push her work she needs to do "git pull origin main" then "git push origin main"
# cd ~/Recent


#3.1 DATA TYPES

def checkDataType(value):
    return type(value).__name__


#3.2 CONDITIONALS

def evenOrOdd(num):
    if type(num) == int:
        if num % 2 == 0:
            return "Even"
        elif num % 2 != 0:
            return "Odd"



#4 LOOPS 

num = [1,2,3,4,5]
def sumWithLoop(num):
    total = 0 
    for i in num:
           total = total + i 
    return total


# 5.1 LISTS

list = ["a","b","c"]
def duplicateList(list):
    new_list = []
    for i in list:
        new_list.append(i)
        new_list.append(i)
    return new_list 



# 5.2 DEBUGGING

# didn't put colon after "square(num)"

print(duplicateList(list))


