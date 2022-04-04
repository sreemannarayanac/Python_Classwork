# Recursive function to find product of two numbers
print('Product of two numbers')
def product(a,b):
    if b==0:
        return 0
    else:
        return a+product(a,b-1)
a, b = [int(input(f'Enter number {i+1}: ')) for i in range(2)]
k=product(a,b)
print(f'Product of {a} and {b} is {k}')