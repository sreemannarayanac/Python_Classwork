# Recursive function to generate Fibonacci series
print('Fibonacci Program')
def fibo(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
def generateFibo(k):
    for i in range(k):
        print(fibo(i), end=' ')
    print()

in_put=int(input('Enter a number(n) to get fibonacci series upto n terms : '))
generateFibo(in_put)