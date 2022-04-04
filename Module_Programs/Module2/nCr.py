# Create a function which accepts two inputs from the user and compute nCr
import math as m
def ncr(n,r):
    if n<r:
        print('n should be greater than r')
    else:
        print(f'{n}C{r} = {m.factorial(n)/(m.factorial(r)*(m.factorial(n-r))):.0f}')
print('Enter inputs for nCr')
a, b= int(input('Enter n : ')), int(input('Enter r : '))
ncr(a,b)