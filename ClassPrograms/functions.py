# Example of Lambda Function
def exlambda(a):
  return lambda b : b * a

doubler = exlambda(2)
print(doubler(11))

def squaring(j):
  return lambda k : k ** j

power3 = squaring(3)
print(power3(5))