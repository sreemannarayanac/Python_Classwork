string1 = 'this is sample1'
string2 = 'tHiiiS\tIs SaMpLe2'
print(f'Sample strings used : \n{string1}\n{string2}')
print('Capitalized : '+string1.capitalize())
print('Casefolded : '+string2.casefold())
print('Centered : '+string1.center(30))
print('Count : ',string2.count('i'))
print('Encoded : ',string2.encode())
print('Setting tab size : ',string2.expandtabs(32))
print('Endswith : ',string2.endswith('2'))
print('Find : ', string1.find('sample'))