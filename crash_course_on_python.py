'''
# Hello World
print ("Hellp World!")
#------------------------------------------------

friends = ['Taylor', 'Alex', 'Pat', 'Eli']
for friend in friends:
    print ("Hi " + friend)
#------------------------------------------------
# Python
for i in range(10):
    print ("Hello World!")

# Bash"
for in in {1..10 }; do
    echo Hello, World !

Power shell :
for ($1 = 1; $i -le 10; $i++) {
    Write-host "Hello, World!"
}
#------------------------------------------------

ratio = (1+ (5**1/2))/2
print (ratio)
#------------------------------------------------

color = ("Yellow")
thing = ("sunshine")
print(color + " is the color of " + thing)

#------------------------------------------------
disk_size = 16*(1024**3)
sector_size = 512
sector_amount = disk_size * sector_size

print(sector_amount)

#------------------------------------------------

>>> print (type(1234))
<class 'int'>
>>> print (type(1234.123))
<class 'float'>
>>> print (type("1234.123"))
<class 'str'>

#------------------------------------------------

bill = 47.28
tip = bill * .15
total = bill + tip
share = 2
print ("Each person needs to pay: " + str(total / share))
#------------------------------------------------

word1 = "How"
word2 = "do"
word3 = "you"
word4 = "like"
word5 = "Python"
word6 = "so"
word7 = "far?"
print (word1, word2, word3, word4, word5, word6, word7)

#------------------------------------------------

def greeting(name, department):
    print ("Welcome, " + name)
    print("You are part of " + department)

greeting ("Ajay", "it")
#------------------------------------------------
# Flesh out the body of the print_seconds function so that it prints the total amount of seconds given the hours, minutes and seconds function parameters.
# Remember that there are 3600 seconds in an hour and 60 seconds in a minute.
def print_seconds(hours, minutes, seconds):
    print((hours*3600) + (minutes*60) + seconds)

print_seconds(1,2,3)

#------------------------------------------------

# Use the get_seconds function to work out the amount of seconds in 2 hours and 30 minutes, t
# hen add this number to the amount of seconds in 45 minutes and 15 seconds. Then print the result.
def get_seconds(hours, minutes, seconds):
    return (((3600*hours) + (60*minutes) + seconds)

amount_a = get_seconds (2,30,0)
amount_b = get_seconds (0,45,0)
result = get_seconds(amount_a, amount_b)
print(result)

#------------------------------------------------
# you have a duration of time in seconds and you want to convert that to the equivalent number of hours, minutes, and seconds

def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 -minutes * 60
    return hours, minutes, remaining_seconds
hours, minutes, seconds = convert_seconds(7500)
print (hours, minutes, seconds)

hours, minutes, seconds = convert_seconds(5000)
print (hours, minutes, seconds)
#------------------------------------------------

# returning none value
def greeting(name, department):
    print ("Welcome, " + (name), "to " + (department))

results = greeting("Ajay", "IT")
print (results)

# Output :
# Welcome, Ajay to IT
# None
#------------------------------------------------

# Sometimes we don't want a function to simply run and finish. We may want a function to manipulate data we passed it and then return the result to us.
This is where the concept of return values comes in handy. We use the return keyword in a function, which tells the function to pass data back.
When we call the function, we can store the returned value in a variable.
Return values allow our functions to be more flexible and powerful, so they can be reused and called multiple times.

# Functions can even return multiple values. Just don't forget to store all returned values in variables! You could also have a function return nothing, in which case the function simply exits.

def lucky_number (name):
    number = len(name) * 9
    print ("Hello " + name + ", Your lucky number is " + str (number))

lucky_number("Kay")
lucky_number("Cameron")
#------------------------------------------------
# REPLACE THIS STARTER CODE WITH YOUR FUNCTION
# In this code, identify the repeated pattern and replace it with a function called month_days,
# that receives the name of the month and the number of days in that month as parameters.
# Adapt the rest of the code so that the result is the same.
# Confirm your results by making a function call with the correct parameters for both months listed.
#-------------------------------------------------
# Sample-
june_days = 30
print("June has " + str(june_days) + " days.")
july_days = 31
print("July has " + str(july_days) + " days.")
#-------------------------------------------------
# With Functions
def month_days(month, days) :
    print(month, "has " + str(days) + " days.")

month_days("June", 30)
month_days("July", 31)

#------------------------------------------------
# Code Style
# refactoring
# This function to calculate the area of a rectangle is not very readable.
Can you refactor it, and then call the function to calculate the area with base of 5 and height of 6?
# Tip: a function that calculates the area of a rectangle should probably be called rectangle_area,
# and if it's receiving base and height, that's what the parameters should be called.

def f1(x, y):
    z = x*y  # the area is base*height
    print("The area is " + str(z))
#------------------------------------------------
def rectangle(length, breadth):
    area = length * breadth  # the area is base*height
    print("The area is " + str(area))

rectangle (5,6)
#------------------------------------------------
# 1) Complete the function to return the result of the conversion
def convert_distance(miles):
    km = miles * 1.6  # approximately 1.6 km in 1 mile

my_trip_miles = 55

# 2) Convert my_trip_miles to kilometers by calling the function above
my_trip_km = ___

# 3) Fill in the blank to print the result of the conversion
print("The distance in kilometers is " + ___)

# 4) Calculate the round-trip in kilometers by doubling the result,
#    and fill in the blank to print the result
print("The round-trip in kilometers is " + ___)
------------------------------------
# 1) Complete the function to return the result of the conversion
def my_trip_miles(miles):

    # 3) Fill in the blank to print the result of the conversion
    my_trip_km = int(miles * 1.6) # approximately 1.6 km in 1 mile

    print("The distance in kilometers is " + str(my_trip_km))
    # 4) Calculate the round-trip in kilometers by doubling the result,
    print("The round-trip in kilometers is " + str(my_trip_km * 2))
my_trip_miles (55)

#------------------------------------------------

#------------------------------------------------

# 1) Complete the function to return the result of the conversion
def my_trip_miles(miles):
    my_trip_km = float(miles * 1.6) # approximately 1.6 km in 1 mile
    return (my_trip_km)

my_trip_miles = (55)

# 2) Convert my_trip_miles to kilometers by calling the function above
my_trip_km = my_trip_miles = (55)

# 3) Fill in the blank to print the result of the conversion
print("The distance in kilometers is " + str(my_trip_km))

# 4) Calculate the round-trip in kilometers by doubling the result,
#    and fill in the blank to print the result
print("The round-trip in kilometers is " + str(my_trip_km * 2))

#------------------------------------------------

# This function compares two numbers and returns them
# in increasing order.
def order_numbers(number1, number2):
    if number2 > number1:
        return number1, number2
    else:
        return number2, number1

# 1) Fill in the blanks so the print statement displays the result
#    of the function call
smaller, bigger = order_numbers(100, 99)
print(smaller, bigger)

#------------------------------------------------
def lucky_number(name):
    number = len(name) * 9
    lucky_number = ("Hello " + name + ". Your lucky number is " + str(number))
    return lucky_number

print(lucky_number("Kay"))
print(lucky_number("Cameron"))

#------------------------------------------------
# >>> print ("Yellow" > "Cyan")
True
# >>> print ("Brown" > "Magebta")
False
# >>> print ("Yellow" > "Cyan" and "Brown" > "Magenta")
False
# >>> print (25 > 50)
False
# >>> print (1 != 2)
True
# >>> print (25 > 50 or 1 != 2)
True
# >>> "pring" (not 42 == "Answer")
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    pring (not 42 == "Answer")
NameError: name 'pring' is not defined
# >>> print (not 42 == "Answer")
True
#------------------------------------------------
Comparison Operators
In Python, we can use comparison operators to compare values. When a comparison is made, Python returns a boolean result, or simply a True or False.
    To check if two values are the same, we can use the equality operator: ==
    To check if two values are not the same, we can use the not equals operator: !=
We can also check if values are greater than or lesser than each other using > and <.
If you try to compare data types that aren’t compatible, like checking if a string is greater than an integer, Python will throw a TypeError.

We can make very complex comparisons by joining statements together using logical operators with our comparison operators.
These logical operators are and, or, and not. When using the and operator, both sides of the statement being evaluated must be true for the whole statement to be true.
When using the or operator, if either side of the comparison is true, then the whole statement is true.
Lastly, the not operator simply inverts the value of the statement immediately following it.
So if a statement evaluates to True, and we put the not operator in front of it, it would become False.
#------------------------------------------------

def hint_username(username):
    if len(username) < 3:
        print("Invalid username. It must be at least 3 character long")
hint_username("asd")

#------------------------------------------------
def is_positive(number):
  if (number > 0):
    return True
  else:
      return None
print (is_positive (13))
#------------------------------------------------
We can use the concept of branching to have our code alter its execution sequence depending on the values of variables.
We can use an if statement to evaluate a comparison.
We start with the if keyword, followed by our comparison.
We end the line with a colon. The body of the if statement is then indented to the right.
If the comparison is True, the code inside the if body is executed.
If the comparison evaluates to False, then the code block is skipped and will not be run.
#------------------------------------------------

def hint_username(username):
    if len(username) < 3:
        print("Invalid username. It must be at least 3 character long")
    else:
        print("Valid username")
hint_username("asdf")

#------------------------------------------------

def is_even(number):
    if number % 2 == 0:
        return True
    return False
print (is_even(24))

# else Statements and the Modulo Operator
# We just covered the if statement, which executes code if an evaluation is true and skips the code if it’s false.
 But what if we wanted the code to do something different if the evaluation is false? We can do this using the else statement.
  The else statement follows an if block, and is composed of the keyword else followed by a colon.
   The body of the else statement is indented to the right, and will be expected if the above if statement doesn’t execute.

# We also touched on the modulo operator, which is represented by the percent sign: %.
This operator performs integer division, but only returns the remainder of this division operation.
 If we’re dividing 5 by 2, the quotient is 2, and the remainder is 1. Two 2s can go into 5, leaving 1 left over.
 So 5%2 would return 1. Dividing 10 by 5 would give us a quotient of 2 with no remainder, since 5 can go into 10 twice with nothing left over.
  In this case, 10%2 would return 0, as there is no remainder.

# ------------------------------------------------

def hint_username(username):
    if len(username) < 3:
        print("Invalid username. It must be at least 3 character long")
    elif len(username) > 15:
        print("Invalid username. It must be at most 15 character long")
    else:
        print("Valid username")
hint_username("asdfAsdsadsdsfdfdsfdsfdsfdsfdsfdfdsfsdfdfdf")

# ------------------------------------------------
#  Building off of the if and else blocks, which allow us to branch our code depending on the evaluation of one statement,
 the elif statement allows us even more comparisons to perform more complex branching.
 Very similar to the if statements, an elif statement starts with the elif keyword, followed by a comparison to be evaluated.
 This is followed by a colon, and then the code block on the next line, indented to the right.
  An elif statement must follow an if statement, and will only be evaluated if the if statement was evaluated as false.
   You can include multiple elif statements to build complex branching in your code to do all kinds of powerful things!

Conditionals Cheat Sheet
In earlier videos, we took a look at some of the built-in Python operators that allow us to compare values, and some logical operators we can use to combine values.
 We also learned how to use operators in if-else-elif blocks.

It’s a lot to learn but, with practice, it gets easier to remember it all.
In the meantime, this handy cheat sheet gives you all the information you need at a glance.

Comparison operators
a == b: a is equal to b
a != b: a is different than b
a < b: a is smaller than b
a <= b: a is smaller or equal to b
a > b: a is bigger than b
a >= b: a is bigger or equal to b
Logical operators
a and b: True if both a and b are True. False otherwise.
a or b: True if either a or b or both are True. False if both are False.
not a: True if a is False, False if a is True.
Branching blocks

In Python, we branch our code using if, else and elif. This is the branching syntax:

if condition1:
    if-block
elif condition2:
    elif-block
else:
    else-block

Remember:
The if-block will be executed if condition1 is True.
The elif-block will be executed if condition1 is False and condition2 is True.
The else block will be executed when all the specified conditions are false.

# ------------------------------------------------
def greeting(name):
  if name == "Taylor":
    return "Welcome back Taylor!"
  elif name == "John":
    return "Hello there, " + name

print(greeting("Taylor"))
print(greeting("John"))

# ------------------------------------------------
def input(number):
  if number > 11:
    print(0)
  elif number != 10:
    print(1)
  elif number >= 20 or number < 12:
    print(2)
  else:
    print(3)
input (10)
# ------------------------------------------------

# Question 5
# If a filesystem has a block size of 4096 bytes, this means that a file comprised of only one byte will still use 4096 bytes of storage.
# A file made up of 4097 bytes will use 4096*2=8192 bytes of storage.
# Knowing this, can you fill in the gaps in the calculate_storage function below,
# which calculates the total number of bytes needed to store a file of a given size?

def calculate_storage(filesize):
  block_size = 4096
  # Use floor division to calculate how many blocks are fully occupied
  full_blocks = filesize // block_size
  # Use the modulo operator to check whether there's any remainder
  partial_block_remainder = filesize % block_size
  # Depending on whether there's a remainder or not, return
  # the total number of bytes required to allocate enough blocks
  # to store your data.
  if partial_block_remainder > 0:
    return (full_blocks + 1) * block_size
  return (filesize)


print(calculate_storage(1))  # Should be 4096
print(calculate_storage(4096))  # Should be 4096
print(calculate_storage(4097))  # Should be 8192
print(calculate_storage(6000))  # Should be 8192
# ------------------------------------------------

# Complete the function by filling in the missing parts. The color_translator function receives the name of a color, then prints its hexadecimal value.
# Currently, it only supports the three additive primary colors (red, green, blue), so it returns "unknown" for all other colors.
def color_translator(color):
    if color == "red":
      hex_color = "#ff0000"
    elif color == "green":
      hex_color = "#00ff00"
    elif color == "blue":
      hex_color = "#0000ff"
    else:
      hex_color = "unknown"
    return hex_color

print(color_translator("blue")) # Should be #0000ff
print(color_translator("yellow")) # Should be unknown
print(color_translator("red")) # Should be #ff0000
print(color_translator("black")) # Should be unknown
print(color_translator("green")) # Should be #00ff00
print(color_translator("")) # Should be unknown
# ------------------------------------------------

# Students in a class receive their grades as Pass/Fail. Scores of 60 or more (out of 100) mean that the grade is "Pass".
# For lower scores, the grade is "Fail". In addition, scores above 95 (not included) are graded as "Top Score".
# Fill in this function so that it returns the proper grade.

def exam_grade(score):
    if (score > 95):
        grade = "Top Score"
    elif (score >= 60):
        grade = "Pass"
    else:
        grade = "Fail"
    return grade

print(exam_grade(65)) # Should be Pass
print(exam_grade(55)) # Should be Fail
print(exam_grade(60)) # Should be Pass
print(exam_grade(95)) # Should be Pass
print(exam_grade(100)) # Should be Top Score
print(exam_grade(0)) # Should be Fail

# ------------------------------------------------
def format_name(first_name, last_name):
  if len (last_name) >= 0 and len(first_name) >= 0:
    return ("Name: " + last_name + ", " + first_name)
  elif len (last_name) <= 0 or len(first_name) <= 1:
    return ("Name: " + ", " + first_name)
  else :
    return string

print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))
# Should return an empty string
# ------------------------------------------------
def sum(x, y):
        return(x+y)
print(sum(sum(1,2), sum(3,4)))

# ------------------------------------------------

def longest_word(word1, word2, word3):
    if len(word1) >= len(word2) and len(word1) >= len(word3):
        word = word1
    elif len(word2) >= len(word1) and len(word2) >= len(word3):
        word = word2
    else:
        word = word3
    return(word)

print(longest_word("chair", "couch", "table"))
print(longest_word("bed", "bath", "beyond"))
print(longest_word("laptop", "notebook", "desktop"))

# ------------------------------------------------
# The fractional_part function divides the numerator by the denominator, and returns just the fractional part (a number between 0 and 1).
# Complete the body of the function so that it returns the right number.

# Note: Since division by 0 produces an error, if the denominator is 0, the function should return 0 instead of attempting the division.

def fractional_part(numerator, denominator):
  if denominator == 0:
    return 0
  else:
    fp = (numerator % denominator) / denominator
    return fp
# Operate with numerator and denominator to
# keep just the fractional part of the quotient


print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0

# ------------------------------------------------

def format_name(first_name, last_name):
  if len (last_name) >= 0 and len(first_name) == 0:
    return ("Name: " + last_name)
  elif len(last_name) == 0 and len(first_name) >= 0:
    return ("Name: " + first_name)
  elif len (last_name) >= 0 or len(first_name) >= 0:
    return ("Name: " + last_name + ", " + first_name)
  else :
    return string

print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))
# Should return an empty string
# ------------------------------------------------

# Anatomy of a While Loop
# A while loop will continuously execute code depending on the value of a condition. It begins with the keyword while, followed by a comparison to be evaluated, then a colon.
# On the next line is the code block to be executed, indented to the right.
# Similar to an if statement, the code in the body will only be executed if the comparison is evaluated to be true.
# What sets a while loop apart, however, is that this code block will keep executing as long as the evaluation statement is true.
# Once the statement is no longer true, the loop exits and the next line of code will be executed.
x = 0
while x < 5:
  print ("Not there yet, x = " + str(x))
  x = x + 1
print ("x" + str(x))
# ------------------------------------------------
def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")

attempts(5)
# ------------------------------------------------
def hint_username(username):
  if len(username) < 3:
    print("Invalid username. It must be at least 3 character long")

hint_username("asd")

username = get_username()
while not valid_username(username):
    print ("invalid Username")
    user name = get_username
# ------------------------------------------------
# Common Pitfalls With Variable Initialization
# You'll want to watch out for a common mistake: forgetting to initialize variables.
If you try to use a variable without first initializing it, you'll run into a NameError.
This is the Python interpreter catching the mistake and telling you that you’re using an undefined variable.
The fix is pretty simple: initialize the variable by assigning the variable a value before you use it.
#
# Another common mistake to watch out for that can be a little trickier to spot is forgetting to initialize variables with the correct value.
  If you use a variable earlier in your code and then reuse it later in a loop without first setting the value to something you want,
  your code may wind up doing something you didn't expect.
  Don't forget to initialize your variables before using them
# ------------------------------------------------

#Infinite loops and Code Blocks
# Another easy mistake that can happen when using loops is introducing an infinite loop.
# An infinite loop means the code block in the loop will continue to execute and never stop.
# This can happen when the condition being evaluated in a while loop doesn't change.
# Pay close attention to your variables and what possible values they can take. Think about unexpected values, like zero.

# In the Coursera code blocks, you may see an error message that reads "Evaluation took more than 5 seconds to complete."
# This means that the code encountered an infinite loop, and it timed out after 5 seconds.
# You should take a closer look at the code and variables to spot where the infinite loop is.
# ------------------------------------------------
# Fill in the blanks to make the print_prime_factors function print all the prime factors of a number.
# A prime factor is a number that is prime and divides another without a remainder.

def print_prime_factors(number):
  # Start with two, which is the first prime
  factor = 2
  # Keep going until the factor is larger than the number
  while factor <= number:
    # Check if factor is a divisor of number
    if number % factor == 0:
      # If it is, print it and divide the original number
      print(factor)
      number = number / factor
    else:
      # If it's not, increment the factor by one
      factor += 1
  return "Done"

print_prime_factors(100)
# Should print 2,2,5,5
# DO NOT DELETE THIS COMMENT

# ------------------------------------------------
# Fill in the empty function so that it returns the sum of all the divisors of a number, without including it.
# A divisor is a number that divides into another without a remainder.
def sum_divisors(n):
    sum = 0
    x = 1
    while n != 0 and x < n:
        if n % x == 0:
            sum += x
        x += 1
    return sum

print(sum_divisors(0))
# 0
print(sum_divisors(3)) # Should sum of 1
# 1
print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# 114

# ------------------------------------------------

def sum_divisors(num):
    return sum([i if num % i == 0 else 0 for i in range(1, num - 1)])

print(sum_divisors(0))
# 0
print(sum_divisors(3)) # Should sum of 1
# 1
print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# 114
# ------------------------------------------------

# The following code can lead to an infinite loop. Fix the code so that it can finish successfully for all numbers.

# Note: Try running your function with the number 0 as the input, and see what you get!

def is_power_of_two(n):
    # Check if the number can be divided by two without a remainder
    while n % 2 == 0 and n !=0:
        n = n / 2

    # If after dividing by two the number is 1, it's a power of two
    if n == 1:
        return True
    return False


print(is_power_of_two(0))  # Should be False
print(is_power_of_two(1))  # Should be True
print(is_power_of_two(8))  # Should be True
print(is_power_of_two(9))  # Should be False
# ------------------------------------------------
# The multiplication_table function prints the results of a number passed to it multiplied by 1 through 5.
# An additional requirement is that the result is not to exceed 25, which is done with the break statement.
# Fill in the blanks to complete the function to satisfy these conditions.

def multiplication_table(number):
    # Initialize the starting point of the multiplication table
    multiplier = 1
    # Only want to loop through 5
    while multiplier <= 5:
        result = number *  multiplier
        # What is the additional condition to exit out of the loop?
        if result >= 26:
               break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        # Increment the variable for the loop
        multiplier += 1

multiplication_table(3)
# Should print: 3x1=3 3x2=6 3x3=9 3x4=12 3x5=15

multiplication_table(5)
# Should print: 5x1=5 5x2=10 5x3=15 5x4=20 5x5=25

multiplication_table(8)
# Should print: 8x1=8 8x2=16 8x3=24
# ------------------------------------------------
# Fill in the gaps of the sum_squares function, so that it returns the sum of all the squares of numbers between 0 and x (not included).
# Remember that you can use the range(x) function to generate a sequence of numbers from 0 to x (not included).

def square(n):
    return n*n

def sum_squares(x):
    sum = 0
    for n in range (x):
        sum += n*n
    return sum
print (sum_squares(10)) # Should be 285

# ------------------------------------------------
 for x in range(5):
	print (x)

# Output
0
1
2
3
4
# ------------------------------------------------
friends = ['Taylor', 'Alex', 'Pat','Eli']
for friend in friends:
    print ("Hi " + friend)
# ------------------------------------------------
# Use for loops when there's a sequence of elements that you want to iterate.
# Use while loops when you want to repeat an action until a condition changes

values = [23, 52, 59, 37, 48]
sum = 0
length = 0
for value in values:
    sum += value
    length =+ 1

print ("Total sum : " + str(sum) + " - Average: " + str(sum/length))
# ------------------------------------------------
# For loops allow you to iterate over a sequence of values. Let's take the example from the beginning of the video:
#
# for x in range(5):
#
#   print(x)
#
# Similar to if statements and while loops, for loops begin with the keyword for with a colon at the end of the line.
# Just like in function definitions, while loops and if statements, the body of the for loop begins on the next line and is indented to the right.
# But what about the stuff in between the for keyword and the colon? In our example, we’re using the range() function to create a sequence of numbers that our for loop can iterate over.
# In this case, our variable x points to the current element in the sequence as the for loop iterates over the sequence of numbers.
# Keep in mind that in Python and many programming languages, a range of numbers will start at 0, and the list of numbers generated will be one less than the provided value.
# So range(5) will generate a sequence of numbers from 0 to 4, for a total of 5 numbers.
#
# Bringing this all together, the range(5) function will create a sequence of numbers from 0 to 4.
# Our for loop will iterate over this sequence of numbers, one at a time, making the numbers accessible via the variable x and the code within our loop body will execute for each iteration through the sequence.
# So for the first loop, x will contain 0, the next loop, 1, and so on until it reaches 4. Once the end of the sequence comes up, the loop will exit and the code will continue.
#
# The power of for loops comes from the fact that it can iterate over a sequence of any kind of data, not just a range of numbers.
# You can use for loops to iterate over a list of strings, such as usernames or lines in a file.
#
# Not sure whether to use a for loop or a while loop? Remember that a while loop is great for performing an action over and over until a condition has changed.
# A for loop works well when you want to iterate over a sequence of elements.
# ------------------------------------------------

# defining range if start & end
product = 1
for n in range (5,10):
    product = product * n
print(product)
# ------------------------------------------------
# In math, the factorial of a number is defined as the product of an integer and all the integers below it.
# For example, the factorial of four (4!) is equal to 1*2*3*4=24. Fill in the blanks to make the factorial function return the right number.
def factorial(n):
    result = 1
    for i in range (1,(n+1)):
        result = result * i

    return result

print(factorial(4)) # should return 24
print(factorial(5)) # should return 120
# ------------------------------------------------

def to_celsius(x):
    return (x-32)*5/9
for x in range(0,101,10):
    print (x, to_celsius(x))
# ------------------------------------------------
# A Closer Look at the Range() Function
# Previously we had used the range() function by passing it a single parameter, and it generated a sequence of numbers from 0 to one less than we specified.
# But the range() function can do much more than that.
# We can pass in two parameters: the first specifying our starting point, the second specifying the end point.
# Don't forget that the sequence generated won't contain the last element; it will stop one before the parameter specified.

# The range() function can take a third parameter, too.
# This third parameter lets you  alter the size of each step.
# So instead of creating a sequence of numbers incremented by 1, you can generate a sequence of numbers that are incremented by 5.
# To quickly recap the range() function when passing one, two, or three parameters:

# One parameter will create a sequence, one-by-one, from zero to one less than the parameter.
# Two parameters will create a sequence, one-by-one, from the first parameter to one less than the second parameter.
# Three parameters will create a sequence starting with the first parameter and stopping before the second parameter, but this time increasing each step by the third parameter.
# ------------------------------------------------

for left in range(7):
    for right in range(left, 7):
        print ("[" + str(left) + "|" + str(right) + "]", end=" ")
    print()
# ------------------------------------------------

teams = ['Dragons', 'Wolves', 'Pandas', 'Unicorns']
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print (home_team + " vs " + away_team)
# ------------------------------------------------

for x in range(x)
SyntaxError: invalid syntax

for x in range(5):
	print (x)
for x in [25]: # or rang (25)
    print (x)
# ------------------------------------------------
def greet_friends (friends):
    for friend in friends:
        print ("Hi " + friend)

greet_friends (['Taylor', 'Alex', 'Pat','Eli'])


# ------------------------------------------------
def validate_users(users):
    for user in users:
        if len(user) >= 3:
            print(user + " is valid")
        else:
            print(user + " is invalid")

validate_users(["purplecat"])
# ------------------------------------------------
Loops Cheat Sheet
Check out below for a run down of the syntax for while loops and for loops.

while condition:
    body

While Loops
A while loop executes the body of the loop while the condition remains True.

Syntax:
while condition:
    body
Things to watch out for!

Failure to initialize variables. Make sure all the variables used in the loop’s condition  are initialized before the loop.
Unintended infinite loops. Make sure that the body of the loop modifies the variables used in the condition, so that the loop will eventually end for all possible values of the variables.

Typical use:
While loops are mostly used when there’s an unknown number of operations to be performed, and a condition needs to be checked at each iteration.

For Loops
A for loop iterates over a sequence of elements, executing the body of the loop for each element in the sequence.

Syntax:
for variable in sequence
    body

#The range() function:

range() generates a sequence of integer numbers. It can take one, two, or three parameters:

range(n): 0, 1, 2, ... n-1
range(x,y): x, x+1, x+2, ... y-1
range(p,q,r): p, p+r, p+2r, p+3r, ... q-1 (if it's a valid increment)

Common pitfalls:
Forgetting that the upper limit of a range() isn’t included.
Iterating over non-sequences. Integer numbers aren’t iterable. Strings are iterable letter by letter, but that might not be what you want.

Typical use:
For loops are mostly used when there's a pre-defined sequence or range of numbers to iterate.

Break & Continue
You can interrupt both while and for loops using the break keyword. We normally do this to interrupt a cycle due to a separate condition.

You can use the continue keyword to skip the current iteration and continue with the next one. This is typically used to jump ahead when some of the elements of the sequence aren’t relevant.

If you want to learn more, check out this wiki page on for loops.
# ------------------------------------------------
'''
# Question 2
# Fill in the blanks to make the factorial function return the factorial of n.
# Then, print the first 10 factorials (from 0 to 9) with the corresponding number.
# Remember that the factorial of a number is defined as the product of an integer and all integers before it.
# For example, the factorial of five (5!) is equal to 1*2*3*4*5=120. Also recall that the factorial of zero (0!) is equal to 1.

def factorial(n):
    result = 1
    for x in range(1,(n+1)):
        result = result * x
    return result

for n in range(0,10):
    print(n, factorial(n+1))

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------
# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------
# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------
# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------
# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------
