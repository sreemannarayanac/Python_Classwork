il = [1,2,3,4,5,6,7,8,9] # input list
ol = [] # output list
for i in range(len(il)):
    ol.append(tuple([il[i],(il[i])**2]))
print(ol)