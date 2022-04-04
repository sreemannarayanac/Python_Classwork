# Recursive function to compute GCD of 2 numbers
print('GCD Program')
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b, a%b)
i, j = [int(input(f"Enter number {k+1}: ")) for k in range(2)]
k=gcd(i,j)
print(f'GCD of {i} and {j} is {k}')