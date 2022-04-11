test_list = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)] 
k = 2
toRemove = []
for i in range(len(test_list)-1):
    if len(test_list[i])==k:
        toRemove.append(test_list[i])
for i in range(len(toRemove)):
    test_list.remove(toRemove[i])
print(test_list)