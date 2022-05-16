import pandas as pd

data = {
  'Names' : ['Sreemannarayana','Akshit','Abhishek','Suraj'],
  'Specialisation' : ['Database, Algorithm, and Support in other departments', 'Framework and Management', 'Frontend God', 'Algo Guy'],
  'Age' : [18]*4
}

df = pd.DataFrame(data)
print(df.dtypes)