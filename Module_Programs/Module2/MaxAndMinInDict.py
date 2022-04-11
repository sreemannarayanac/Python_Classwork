dicta = {'1': 1, '2': 4, '3': 9, '4': 16, '5': 25, '6': 36, '7': 49, '8': 64, '9': 181, '10': 100}
values = list(dicta.values())
values.sort()
print(f'Min {values[0]}\nMax {values[len(values)-1]}')