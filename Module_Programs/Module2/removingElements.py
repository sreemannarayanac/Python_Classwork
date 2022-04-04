# Program to print a specified list after removing the 0th, 4th and 5th elements. Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'] Expected Output : ['Green', 'White', 'Black']
sample = ['Red','Green','White','Black','Pink','Yellow']
del_indexes = [0,4,5]
remove = []
for i in range(len(del_indexes)):
    remove.append(sample[del_indexes[i]])
for i in range(len(remove)):
    sample.remove(remove[i])
print(sample)