# Accepting 5 different subject marks from user and displaying the grade of the student
print("Marks of Five Subjects")
marks, total = [], 0
for i in range(5):
    k=int(input(f'Subject {i+1} marks : '))
    if k in range(0,100):
        marks.append(k)
    else:
        print('Error')
        break
for j in range(5):
    total+=marks[i]
average=total/5
grade=average/9.5
if grade>10:
    print('Grade = ',10)
else:
    print(f'Grade = {grade:.1f}')