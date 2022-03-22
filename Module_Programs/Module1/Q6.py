# Building a mathematical calculator that can perform operations according to user input. Use decision making statement.
num1,num2=float(input("Enter num1 : ")),float(input("Enter num2 : "))
print('''Enter your choice :
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Remainder''')
while True:
  choice=int(input('Enter choice number here : '))
  if choice==1:
      print(f'Answer = {num1+num2:.2f}')
      break
  elif choice==2:
      print(f'Answer = {num1-num2:.2f}')
      break
  elif choice==3:
      print(f'Answer = {num1*num2:.2f}')
      break
  elif choice==4:
      print(f'Answer = {num1/num2:.2f}')
      break
  elif choice==5:
      print(f'Answer = {num1%num2:.2f}')
      break
  else:
    print('Invalid choice')