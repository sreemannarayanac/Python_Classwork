# Example of Lambda Function
def exlambda(a):
  return lambda b : b * a

doubler = exlambda(2)
print(doubler(11))

def squaring(j):
  return lambda k : k ** j

power3 = squaring(3)
power4 = squaring(4)
power5 = squaring(5)
print(power5(5),"\n",power4(5),"\n",power3(5))