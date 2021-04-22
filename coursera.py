'''
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
'''
