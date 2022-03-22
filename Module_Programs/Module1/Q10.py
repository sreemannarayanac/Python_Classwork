# Check whether the given input is a) palindrome b) strong c) perfect
import math
n = int(input('Enter number : '))
s1, s2= 0, 0
if str(n)==str(n)[::-1]:
    print(f'{n} is palindrome')
else:
    for i in range(len(str(n))):
        s1+=math.factorial(int(str(n)[i]))
    if s1==n:
        print('Strong Number') # 145 is strong number (as 1! + 4! + 5! = 145)
    else:
        for i in range(1,n):
            if n%i==0:
                s2+=i
        if n==s2:
            print('Perfect Number') #28 is perfect number (as it's factor's sum is 28)
        else:
            print('Not perfect, palindrome or strong number')