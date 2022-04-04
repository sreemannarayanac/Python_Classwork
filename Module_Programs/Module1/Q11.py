p = float(input('Enter principal amount : '))
i = float(input('Enter interest (in terms of percentage) : '))
t = int(input('Enter number of years : '))
n = int(input('Enter number of compoundings per year : '))
amount = 0
for j in range(1,t+1):
  amount = p*(1+(i/100)/n)**(n*(j+1))
print(f'Amount to be paid at the end = {amount:.2f}')