# Practice Problem: Print a text in python .
'''
print("Hello")
print("This is my first program in python")
'''
######################################################################

# Practice Problem: Given two strings, s1 and s2, create a new string by appending s2 in the middle of s1.
'''
str1 = input("Enter first string ")
str2 = input("Enter second string ")
l = len(str1)
m = l//2
print(str1[0:m]+str2+str1[m:l])
'''
######################################################################
# Practice Problem: Create a program to shift 0 at end.
'''
n = [0, 1, 0, 3, 5, 6]

for i in n:
    if i == 0:
        n.remove(0)
        n.append(0)

print(n)
'''
######################################################################

# Practice Problem: Create a function that takes a list and an integer N, and breaks the list into smaller sublists, each of length N. The last chunk may be shorter if the list length isn’t perfectly divisible by N.
'''
n = [1,2,3,4,5,6,7,8,9,10]
N = int(input("Print sublist length "))
l = len(n)

m = []

for i in range(0, l, N):
    m.append(n[i:i+N])

print(m)
'''
######################################################################
# Practice Problem: Create a function that takes an integer and creates a Triangle.
'''
r = int(input("Enter a no. "))

for i in range(1, r + 1):
    s = (" " * (r - i))
    p =  ("*" *(2 * i -1))
    print(s+p)
    
'''
#Practice Problem: Write a program to print the dimond shape pattern :

'''
r = int(input("Enter a no. "))

for i in range(1, r + 1):
    s = " " * (r - i)
    p = "*" * (2 * i - 1)
    print(s + p)

for i in range(r - 1, 0, -1):
    s = " " * (r - i)
    p = "*" * (2 * i - 1)
    print(s + p)
    '''
    #Practice Problem: Write a program to print the Square shape pattern :
'''
r = int(input("Enter a number: "))

for i in range(1, r + 1):
    if i == 1 or i == r:
        print("* " * r)
    else:
        print("* " + "  " * (r - 2) + "*")
        '''
         #Practice Problem: Write a program to check a no. is palindrome or not :
'''
r = int(input("Enter a  no. "))
t = r
rev = 0

while t > 0:
    n = t % 10
    rev = rev * 10 + n
    t = t // 10

if r == rev:
    print("Palindrome number")
else:
    print("Not a palindrome.")
    '''
    #Practice Problem: Write a program to check a no. is Armstrong no. or not :
'''    
r = int(input("Enter a number: "))
l = len(str(r))

t = r
sum = 0

while t > 0:
    n = t % 10
    sum = sum + (n ** l)
    t = t // 10

if r == sum:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
'''


