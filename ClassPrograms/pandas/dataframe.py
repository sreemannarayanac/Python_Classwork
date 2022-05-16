import pandas as pd

data = {
  'Names' : ['Sreemannarayana','Akshit','Abhishek','Suraj'],
  'Specialisation' : ['Database, Algorithm, and Support in other departments', 'Framework and Management', 'Frontend God', 'Algo Guy'],
  'Age' : [19, 18, 18, 18]
}

df = pd.DataFrame(data, index = ['a','b','c','d'], columns = ['Names','Age'])
# altDf = df.loc[lambda df : df['Age'] > 18]
altDf = df[df['Age']>18]
print(altDf)