import pandas as pd

record = {
    'id':[1,2,3,4,5,6,7,8,9,10],
    'Names':['abc','def','ghi','jkl','mno','pqr','stu','vwx','yza','xyz'],
    'Age':[24,45,43,56,78,32,12,19,54,65]
}

df = pd.DataFrame(record)

sum_age = 0
count = 0

for j in df:
    print([i for i in df[j]])

for i in df['Age']:
    sum_age += i
    count +=1

print(sum_age/count)