'''
small_so_far = None
print('Before', small_so_far)
for value in (9, 14, 41, 12, 3, 74, 15) :
    if small_so_far is None :
        small_so_far = value
    elif value > small_so_far :
        small_so_far = value
    print (small_so_far, value)
print ('After', small_so_far)

'''

# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
# Once 'done' is entered, print out the largest and smallest of the numbers.
# If the user enters anything other than a valid number catch it with a try/except and
# put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.
#largest = None
#smallest = None
#while True:
#    num = input("Enter a number: ")
#    if num == "done" : break
#    print(num)
#
# print("Maximum", largest)

#Invalid input
#Maximum is 10
#Minimum is 2

largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try :
        num1 = float (num)
    except:
        print ('Invalid input')
        continue
    if smallest is None :
        smallest = num
        print("Minimum is ", smallest)
    elif num > smallest :
        largest = num
        print("Maximum is ", largest)

#    if smallest is None :
#        largest = num
#    elif num > smallest
#        smallest = num
#    print("Minimum is ", smallest)
print ()
print("Maximum is ", largest)
print("Minimum is ", smallest)
