from tabulate import tabulate
import math

entries = 1000
pi = math.pi
a = (pi * 2)/(entries - 1)
row = []
col = []

row.append(["x", "sin(x)"])
for x in range(0,entries):
    col = []
    col.append(a * x)
    col.append(math.sin(a * x))
    row.append(col)


print(tabulate(row))