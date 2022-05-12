'''Program to remove specific elements from the list'''
_list = ['Red','Green','White','Black','Green','Yellow']
to_remove_indexes = [0,4,5]
to_remove_values = []

for i in to_remove_indexes:
  to_remove_values.append(_list[i])

for i in to_remove_values:
  _list.remove(i)

print(_list)

print('\n\n')


'''Program to get the difference of two lists'''
def differenceOfLists(i,j):
  k = []
  for a in j:
    if a not in i:
      k.append(a)
    else:
      continue
  return k


l1 = [1,2,3,4]
l2 = [4,54,23,2]

# Calling function
diff = differenceOfLists(l1,l2)
print(diff)

print('\n\n')

'''Finding the smallest and the greatest second number in a list'''
num_list = [12, 13, 57, 56, 92, 12, 46, 85, 83]
num_list.sort()
num_listSet = set(num_list)
num_list = list(num_listSet)
print(f'''Second Greatest Number : {num_list[1]}
Second Smallest Number : {num_list[-2]}''')