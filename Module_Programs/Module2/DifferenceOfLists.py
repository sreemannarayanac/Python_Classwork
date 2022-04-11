l1 = [1,2,3,4,5,657768,7,8,9,10]
l2 = [10,9,8,7,6,5,4,3,2,1234]
diff = list(set(l1) - set(l2))+list(set(l2) - set(l1))
print(diff)