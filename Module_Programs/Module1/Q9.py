# Compute the factorial of a given number
i = int(input("Enter a number(for factorial) : "))
answer=1
for i in range(1,i+1):
    answer*=i
print(f'Factorial : {answer}')
#Alternate method
# import math
# i = int(input("Enter a number : "))
# print(f"Factorial of {i} is {math.factorial(i)}")


#Compute GCD of two given numbers
print("Enter two numbers for GCD : ")
i, j = [int(input()) for k in range(2)]
temp, res = 0, 0
if j>i:
    temp=i
    i=j
    j=temp
for a in range(1,i):
    if i%a==0 and j%a==0:
        res=a
print(f'GCD of numbers {i} and {j} is {res}')
#alternate
#Compute GCD of two given numbers
# print("Enter two numbers")
# i, j = [int(input()) for k in range(2)]
# temp, res = 0, 0
# if j>i:
#     temp=i
#     i=j
#     j=temp
# print(f'GCD of {i} and {j} is {math.gcd(i,j)}')

#Generating Fibonacci upto N terms
N = int(input("Enter N (for fibonaci): "))
p1, p2 = 0, 1
p3 = p1+p2
if N==0 or N<0:
    print('Enter valid N')
elif N==1:
    print(1)
elif N==2:
    print(f'{1} {p3}')
elif N>3:
    print(p2, end=' ')
    for k in range(1,N):
        print(p3, end=' ')
        p1, p2 = p2, p3
        p3 = p1+p2