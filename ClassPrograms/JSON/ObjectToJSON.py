import json

class CAT():
    def __init__(self, name, age, color):
        self.Name = name
        self.Age = age
        self.Color = color

k = CAT("Cheems", 4, "Creame")

jsonK = json.dumps(k.__dict__)
print(jsonK)
i = json.loads(jsonK)
print(i)