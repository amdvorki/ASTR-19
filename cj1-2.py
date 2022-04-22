import sys

def printMath(a, b):
    sum = a + b
    diff = a - b
    prod = a * b
    print(f"Sum of {a} and {b} is: {sum}, and the type is: {type(sum)}")
    print(f"Sum of {a} and {b} is: {diff}, and the type is: {type(diff)}")
    print(f"Sum of {a} and {b} is: {prod}, and the type is: {type(prod)}")



printMath(1,10)
printMath(1.0,10.0)
printMath(100.2323, 298.2323)