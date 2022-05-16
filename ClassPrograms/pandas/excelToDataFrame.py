import pandas as pd
file = pd.read_excel('FinancialSample.xlsx')
df = pd.DataFrame(file)
print(df)