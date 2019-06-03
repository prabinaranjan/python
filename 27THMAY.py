globalVar=1

def sum(a,b):
      return a+b
def mult(a,b):
      globalVar=a*b
      return globalVar
def div(b,a):
      globalVar=b/a
      return globalVar

print(sum(mult(2,2),div(2,2)))




