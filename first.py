""" set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.union(set2))
print(set1.intersection(set2)) """


""" marks = {}

sub = input("Enter first subject")
mark = float(input("Enter the marks of first subject"))
marks[sub] = mark
sub = input("Enter second subject")
mark = float(input("Enter the marks of second subject"))
marks[sub] = mark
sub = input("Enter third subject")
mark = float(input("Enter the marks of third subject"))
marks[sub] = mark

print(marks) """


""" i = 100

while i >= 1:
    print(i)
    i -= 1 """


""" n = int(input("Enter a number"))

i = 1

while i <= 10:
    print(n, "*", i, "=", n*i)
    i+=1 """


""" elem = (48, 8, 8, 98, 35, 354, 25, 24)

search = int(input("Enter the number you wanna search"))

i = 0

while i < len(elem):
    if(search == elem[i]):
        print("got", elem[i], "at", i, "index")
    i += 1 """


""" n = int(float(input("Enter the range the natural no")))

sum = 0

for i in range(1, n+1):
    sum *= i

print(sum) """


""" num = int(input("Enter a number"))

factorial = 1

for i in range(1, num+1):
    factorial = factorial * i
    
print(factorial) """


""" def sum(a, b):
    a = 2
    b = 2

a = 4
b = 2

sum(a, b)

print(a, b) """


""" def calculate(a,b):
    return a+b

calc = calculate

print(calc(4, 2)) """


""" def average(a, b, c):
    avg = (a + b + c) / 3
    return avg

print(average(3, 3, 4)) """


""" def average(*args):
    initial = 0
    for i in args:
        initial += i
    return initial / len(args)


print(average(4, 1, 5, 8)) """


""" def length(my_list):
    return len(my_list)

def print_elem(my_list):
    for i in my_list:
        print(i)
        
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact
        
def currency_convertor(USD):
    exchange_rate = 277.70
    PKR = USD * exchange_rate
    return PKR

arr = [54,354,543,232,3,132,13,1,31]

print(length(arr))
print_elem(arr)
print(factorial(4))
print(currency_convertor(2)) """


""" def check(n):
    if(n%2 == 0):
        print("Even")
    else:
        print("Odd")
        
check(int(input("Enter the number"))) """


""" def factorial_recursion(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursion(n-1)
    
print(factorial_recursion(0)) """


""" def recursion_sum(n):
    if n == 0:
        return 0
    return n + recursion_sum(n-1)

print(recursion_sum(4)) """


""" def recursion_print(lst, i=0):
    if i == len(lst):
        return
    print(lst[i])
    recursion_print(lst, i + 1)


arr = ["a", "df", "gh", "yj", "u", "ujy"]
recursion_print(arr) """


""" def recursion_print_values(*val):
    if len(val) == 0:
        return
    else:
        print(val[0])
        recursion_print_values(*val[1:])
        
recursion_print_values(1, 2, 3, 4, 5) """


# read() reads the entire file. read(5) reads the first 5 characters. readline() reads one line at a time. Note: Your usage is correct. Remember that after reading, the file pointer moves to the end of what was read, so subsequent reads continue from there.
""" demo_file = open("demo.txt", "r")
print(demo_file.read())
demo_file.close()


demo_file = open("demo.txt", "r")
print(demo_file.read(5))
demo_file.close()


demo_file = open("demo.txt", "r")
print(demo_file.readline())
print(demo_file.readline())
demo_file.close() """


# Opening a file in "w" mode truncates the file (deletes existing content) or creates it if it doesn't exist.
""" demo_file = open("demo.txt", "w")
demo_file.write("I want to learn Python asap. 123") 
demo_file.close() 

# if the file name which we passes didn't exist it will automatically crate a file from that name for us
demo_file = open("demo_create_write.txt", "w")
demo_file.write("I am creating and writing text through python write mode to check if it is created and writing or not")
demo_file.close() """


# Opening a file in "a" mode appends data to the end of the file without deleting existing content. If the file doesn't exist, it creates a new one.
""" demo_file = open("demo.txt", "a")
demo_file.write("\nI am adding new line through python to check if it is added or not")
demo_file.close()

demo_file = open("demo_create_append.txt", "a")
demo_file.write("I am creating and appending text through python append mode to check if it is created and appended or not")
demo_file.close() """


# Opening a file in "r+" mode allows reading and writing without truncating the file. Writing starts from the current file pointer position (default is the beginning). Overwrites existing data based on the length of the new data. for example: If we have already written "I am learning python" in our file and we're writing "abc" to the new file so now in that file we'll gonna have "abcm learning python" (no truncate)
""" demo_file = open("demo.txt", "r+")
demo_file.write("abc")
demo_file.close() """


# Opening a file in "w+" mode truncates the file and allows both reading and writing. The file is cleared upon opening.
""" demo_file = open("demo.txt", "w+")
demo_file.write("Ab khali ye likha hua aayega hamari file mein00")
demo_file.close() """


# Opening a file in "a+" mode allows reading and appending. The file pointer is at the end after opening, so you'll need to use demo_file.seek(0) if you want to read from the beginning.
""" demo_file = open("demo.txt", "a+")
demo_file.write("Ab ye likha hua aayega hamari file k end mein")
demo_file.close() """


# Using the with statement ensures that the file is properly closed after its suite finishes, even if an exception is raised. Note: This is the recommended way to work with files in Python.
""" with open("demo.txt", "r") as demo_file:
    print(demo_file.read()) 

with open("demo.txt", "w") as demo_file:
    demo_file.write("new data") """


# Deleting a file
""" import os
os.remove("delete_file.txt") """
