'''
psajay@psajay-ubuntu:~$ python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...

psajay@psajay-ubuntu:~$ curl -o /dev/null -s -w "%{http_code}\n" http://localhost:8000
200
psajay@psajay-ubuntu:~$ curl -o /dev/null -s -w "%{http_code}\n" http://localhost:8000
000
-------------------------------
x = 1
x = x+1
print (x)
-------------------------------
x = 50
if x < 10:
  print('Smaller')
if x > 20:
  print ('Bigger')

print ('Finis')
-------------------------------
n = 5
while n > 0:
  print (n)
  n = n - 1
print('BlastOFF')
-------------------------------
a = 35
b = 22.5
c = a * b
print (c)
-------------------------------
x = .51
x = 3.9 * x * (1 - x)
print (x)
-------------------------------
>> xx = 2
>>> xx = xx + 2
>>> print (xx)
4

>>> yy = 440 * xx
>>> print (yy)
1760

>>> zz = yy / 1000
>>> print (zz)
1.76

>>> jj = 23
>>> kk = jj % 5
>>> print (kk)
3

>>> print (4 ** 3)
64

>>> print (1 + 2 ** 3 / 4 *5)
11.0

>>> print (1 + 2 ** 3 / (4 *5))
1.4

>>> print (1 + 2 ** (3 / 4) *5)
9.408964152537145

>>> print ((1 + 2) ** 3 / 4 *5)
33.75
-------------------------------
# parentheses override everything. Exponentiation is the most powerful, multiplication and division and remainder are equal. They're the next most powerful. And addition and subtraction. And then when in doubt, you just go left to right.

# parentheses first, power second, multiplication third, addition, and then left to right
-------------------------------
>>> type (1)
<class 'int'>
>>> type ("eee")
<class 'str'>
>>> type ('eee')
<class 'str'>
>>> type ('1')
<class 'str'>
>>> type (1.3)
<class 'float'>
-------------------------------
# Chaging String to Int
>>> sval = '123'
>>> type (sval)
<class 'str'>

>>> print (sval + 1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str

>>> sval = int(sval)
>>> print (sval + 1)
124
-------------------------------
# Chaging String to Float
>>> sval = '123'
>>> print (sval + 1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> sval = float(sval)
>>> print (sval + 1)
124.0
-------------------------------
# Usig Input to take value
name = input ('Who are you ?')
print ('Welcome' , name)
-------------------------------
# Convert elevator Floors
inp = input ('Enter Europe Floor')
usf = int (inp) + 1
print ('US Floor', + usf)

-------------------------------
# This first line is provided for you

hrs = input("Enter Hours:")
rate = input ("Enter Pay rate:")
pay = float(hrs) * float(rate)
print ('Pay:', pay)
-------------------------------
# Conditional Steps - if
x = 50
if x < 10:
    print('Smaller')
if x > 20:
    print ('Bigger')

print ('Finis')
-------------------------------
# Conditional Steps - While
n = 5
while n > 0:
  print (n)
  n = n - 1
print('BlastOFF')
-------------------------------
#Comparison Operator :
x = 5
if x == 5 :
    print ('Equals 5')
if x > 4 :
    print ('Greater than 4')
if x < 6 :
    print ('lesser than 6')
if x <= 5 :
    print ('less than or equal to 5')
if x != 6 :
    print ('not equal to 6')
-------------------------------
# how to use intends
x = input ('input value of x:')
print ('Before 5')
if x == 5 :
    print ('is 5')
    print ('is still 5')
    print ('is third 5')
print ('Afterwards 6')
print ('Before 6')
if x == 6 :
    print ('is 6')
    print ('is still 6')
    print ('it is still 6')
print ('Afterwards 6')

# If else
x = input ('input value of x:',)
if int(x) > 2:
    print ('Bigger')
else :
    print ('smaller')

print ('All done')
-------------------------------
# Using try & except for avoiding traceback.
astr = input ('input value of astr to check :')
try :
    istr = int(astr)
except :
    istr = -1
print ('first', istr)
astr1 = input('input value of astr1 to check :')
try :
    istr = int(astr1)
except :
    istr = -1
print ('second', istr)
-------------------------------

rawstr = input ('Enter a number: ')
try :
    ival = int(rawstr)
except :
    ival = -1

if ival > 0 :
    print ('Nice work', rawstr, 'is a number')
else :
    print (rawstr, 'is not an intiger')


x = 0
if x < 2 :
    print('Small')
elif x < 10 :
    print('Medium')
else :
    print('LARGE')
print('All done')
---------------------------
x = input ('value')
if float() < 2 :
    print('Below 2')
elif float() >= 2 :
     print('Two or more')
else :
    print('Something else')
---------------------------
astr = 'Hello Bob'
istr = 0
try:
    istr = int(astr)
except:
    istr = -1
---------------------------

hrs = input("Enter Hours:")
rate = input("Enter rate:")
try:
    h = float(hrs)
    r = float (rate)
except:
    print ("Error, Please enter numeric input")
    quit ()
print ('Hours =', h, 'Rate =',  r)
if h <= 40:
    pay = (h *r)
else :
    #pay = ((r * 1.5) * (h - 40)) + (r * 40)
    reg = (40 * r)
    ot = ((r * 1.5) * (h - 40))
    pay = (reg + ot)
print (pay)
 ---------------------------
 Score = input ("Enter Score: ")
score = float(Score)
try :
    if score <= 1.0:
except:
    print ('Error, scopre out of range')
    quit ()
print (score)

---------------------------
score = input ('Enter Score: ')
score = float (score)
if score >= 1.0:
    print ('Error : Exiting')
    quit ()
elif score >= 0.9 :
    print ('A')
elif score >= 0.8 :
    print ('B')
elif score >= 0.7 :
    print ('C')
elif score >= 0.6 :
    print ('D')
elif score < 0.6 :
    print ('F')
---------------------------
# Functions -
def thing():
    print ("Hello")
    print ('Fun')

thing()
print ('Zip')
thing()
---------------------------
Type "help", "copyright", "credits" or "license" for more information.
# first it will be all lowercase letters & then it will be uppercase of values

>>> big = max ('Hello w World')
>>> print (big)
w
>>> big = max ('Hello World')
>>> print (big)
r
>>> big = max ('Hello world')
>>> print (big)
w

>>> tiny = min ('Hello world')
>>> print (tiny)

# space is the lowest lowercase letter.
------------------------------
# defining a function
x = 5
print ('Hello')

def print_lyrics ():
    print ('i ''am a limberjack, and i''m okay.')
    print ('i sleep all night & I work all day.')

print ('Yo'), print_lyrics()
x = x + 2
print (x)
------------------------------
>>> def greet (lang) :
...     if lang == 'es' :
...         print ('Hola')
...     elif lang == 'fr' :
...         print ('bonjour')
...     else :
...         print ('Hello')
...
>>> greet ('en')
Hello
>>> greet ('es')
Hola
>>> greet ('fr')
bonjour
>>>
>>> greet ('ab') # any random would be else
Hello
------------------------------

def greet (lang) :
    if lang == 'es' :
        return 'Hola'
    elif lang == 'fr' :
        return 'bonjour'
    else :
        return 'Hello'
# Output :
>>> print (greet ('en'), 'glen')
Hello glen
>>> print (greet ('es'), 'sally')
Hola sally
>>> print (greet ('fr'), 'Michalel')
bonjour Michalel
# ------------------------------
big = max ('Hello World')
print (big)

>>> big = max ('Hello World')
>>> print (big)
r
>>> small = min ('Hello World')
>>> print (small)

>>> small = min ('Hello_World')
>>> print (small)
H
------------------------------
# Functions Sample
def addtwo (a, b)
    added = a + b
    return added

x = addtwo (3, 5)
print (x)
------------------------------

# Addition using functions
def func(a,b):
    return a + b
print (func (10, 20))

# write a programs to find rectange araa
def func(l,b):
    result = l*b
    return result

c= (func (10, 20))
print (c)

# Write a programme to chose opration  (+, -, *, / ) & return results
def oper (num1,num2):
        while(True):
            choice = input ("Please select your Operation:")
            if (choice == '+'):
                print (num1 + num2)
                break
            elif (choice == '-'):
                print(num1 - num2)
                break
            elif (choice == '*'):
                print(num1 * num2)
                break
            elif (choice == '/'):
                print(num1 / num2)
                break
            else:
                print('Wrong choice')
a = float (input("Please enter your First number: "))
b = float (input("Please enter your Second number: "))
# a = int(a)
# b = int (b)
oper (a,b)
--------------------------
#Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
#Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours.
#Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation.
# The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
# You should use input to read a string and float() to convert the string to a number.
# Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly.
# Do not name your variable sum or use the sum() function
def computepay (h, r):
    if h == 40:
        tpay = (h *r)
        return tpay
    elif h >= 40:
        reg = (40 * r)
        ot = ((r * 1.5) * (h - 40))
        tpay = (reg + ot)
        # tpay = ((r * 1.5) * (h - 40)) + (r * 40)
        return tpay
    else:
        print = ("Less than 40 hrs this week")

hrs = float (input ("number of hours : "))
rate = float (input ("rate per hour : "))
p = computepay(hrs, rate)
print ("Pay ", p)
-----------------------
def computepay(h,r):
    return 42.37

hrs = input("Enter Hours:")
p = computepay(10,20)
print("Pay",p)
----------------------
# While loop with conditional statement.
n = 5
while n > 0 :
    print (n)
    n = n-1
print ('Blast Off')
print (n)
--------------------------------------
# While loop with break
while True:
    line = input ('> ')
    if line == 'done' :
        break
    print (line)
print ('done!')

# Definit Loops
--------------------------------------
while True:
    line = input ('> ')
    if line == '#' : # if input is #, dont print this
        continue # contine to first line
    if line == 'done':
        break
    print (line)
print ('Done !')

--------------------------------------
# definite Loops
for i in [5, 4, 3, 2, 1] :
    print (i)
print ('Blast off !')

friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends :
    print ('Happy new year :', friend)
print ('Done')
--------------------------------------
largest_so_far = -1
print('Before', largest_so_far)
for the_num in (9, 14, 41, 12, 3, 74, 15) :
    if the_num > largest_so_far :
        largest_so_far = the_num
    print (largest_so_far, the_num)
print ('After', largest_so_far)

--------------------------------------
# Counting in loop like line numbers
zork = 0
print ('Before', zork)
for thing in (9, 14, 41, 12, 3, 74, 15) :
    zork = zork + 1
    print (zork, thing)
print ('After', zork)
--------------------------------------
# Counting in loop like line numbers
zork = 0
print ('Before', zork)
for thing in (9, 14, 41, 12, 3, 74, 15) :
    zork = zork + thing
    print (thing, zork)
print ('After', zork)
--------------------------------------
# Finding average in loop
count = 0
sum = 0
print ('Before', count, sum)
for value in (9, 14, 41, 12, 3, 74, 15) :
    count = count + 1
    sum = sum + value
    print (count, sum, value)
print ('After', sum, sum/count)
--------------------------------------
# Filtering in loop

print ('Before')
for value in (9, 14, 41, 12, 3, 74, 15) :
    if value > 20:
        print ('greater than 20', value)
print ('After')
--------------------------------------
# Changing value of a variable - Search using Boolean variable.

found = False
print ('Before', found)
for value in (9, 14, 41, 12, 3, 74, 15) :
    if value == 3 :
        found = True
    print(found, value)
print ('After', found)
--------------------------------------
# Smallest fo far non working sample
# small_so_far = 100
print('Before', small_so_far)
for the_num in (9, 14, 41, 12, 3, 74, 15) :
    if the_num < small_so_far :
        small_so_far = the_num
    print (small_so_far, the_num)
print ('After', small_so_far)

--------------------------------------
small_so_far = None
print('Before', small_so_far)
for value in (9, 14, 41, 12, 3, 74, 15) :
    if small_so_far is None :
        small_so_far = value
    elif value < small_so_far :
        small_so_far = value
    print (small_so_far, value)
print ('After', small_so_far)

--------------------------------------
n = 0
while n >= 0 :
    print('Lather')
    print('Rinse')
print('Dry off!')

--------------------------------------
zork = 0
for thing in [9, 41, 12, 3, 74, 15] :
    zork = zork + thing
print('After', zork)

--------------------------------------
n = 0
while n > 0 :
    print('Lather')
    print('Rinse')
print('Dry off!')

--------------------------------------
num = 0
tot = 0.0
while True :
    sval = input('enter a number: ')
    if sval == 'done' :
        break
    try:
        fval = float(sval)
    except:
        print ('Invalid Input')
        continue
    print(fval)
    num = num + 1
    tot = tot + fval

print ('All Done')
print (tot, num, tot/num)

--------------------------------------
# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
# Once 'done' is entered, print out the largest and smallest of the numbers.
# If the user enters anything other than a valid number catch it with a try/except and
# put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.

largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    print(num)

print("Maximum", largest)

'''
