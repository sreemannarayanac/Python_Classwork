import pandas as pd

data = {
  'Segment' : 'Government',
  'Country' : 'Russia',
  'Product' : 'S400',
  'Discount Band' : 'Medium',
  'Units Sold' : [100],
  'Manufacturing Price' : [1000000000],
  'Sale Price' : [9000],
  'Gross Sales' : [100000000000],
  'Discounts' :   [900000],
  ' Sales' : [99999100000]
}
df2 = pd.DataFrame(data)


with pd.ExcelWriter('FinancialSample1.xlsx') as writer:
  df2.to_excel(writer, sheet_name='new_sheet2')
print(df2.dtypes)