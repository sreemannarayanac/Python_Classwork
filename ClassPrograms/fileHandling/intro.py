with open('intro.txt','a') as u:
  u.write('Sample text \n')


with open('intro.txt','r') as f:
  k=f.readlines()
  print(k)