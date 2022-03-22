#Conversion of one unit to another (such as hours to minutes, miles to km and etc)
value = int(input("Enter number of minutes : "))
converted_value = value/60
print(f'Number of hours = {converted_value}')
value = float(input("Enter number of miles : "))
converted_value = value*1.609344
print(f'Number of Kilometers = {converted_value:.2f}')