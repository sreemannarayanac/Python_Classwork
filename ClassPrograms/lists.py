'''
List is a collection of non-homogenous (or not of same type) data.
While array is a collection of homogenous data.
'''
l1 = [1, 1.5, 'Hello', True, 1+2j, [1,2,3], (1,2,3), {1,2,3}]
for i in l1:
  print(type(i))

print("\n\n")
# Append and Insert
l2 = []
l2.append(4)
l2.append(76)
l2.append(546)
print(l2)
l2.insert(1,[12,3])
print(l2)

print('\n\n')
# Extend
la = ['a', 'a', 'a']
l1.extend(la)
print('l1\n',l1,'\n')
l2.extend(l1)
print('l2\n',l2)

print('\n\n')
# remove and pop
l2.remove('a') # Removes First Occurence of 'a' from the list
print('l2 is now :\n',l2)
l1.pop() # Removes last element from the list
print('\nl1 is now :\n',l1)