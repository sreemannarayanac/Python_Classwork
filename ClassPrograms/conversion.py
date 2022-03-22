print('''Choices : 
1. Convert hours to minutes
2. Convert miles to km''')
print('Enter Choice here -> ', end="")
choice=int(input())
if choice!=None:
  try:
    if choice==1:
      i=float(input('Enter number of hours : '))
      print(f'Number of minutes are {i*60:.0f}')
    elif choice==2:
      i=float(input('Enter number of miles : '))
      print(f'Number of Kilometres are {i*1.60934:.2f}')
    else:
      print('Oops!! You had only two options.')
  except:
    pass