# Printing all even numbers, odd numbers, count of even numbers, count of odd numbers within a given range.
print('Enter start and end')
start, end = [int(input()) for i in range(2)]
even, odd= [], []
for j in range(start,end+1):
    if j%2==0:
        even.append(j)
    elif j%2!=0:
        odd.append(j)
print("Even numbers : ",end=" ")
for j in range(len(even)):
    print(even[j],end=' ')
print('\nOdd numbers  : ',end=' ')
for j in range(len(odd)):
    print(odd[j],end=' ')
print(f'\nCount of even = {len(even)}\nCount of odd = {len(odd)}')
