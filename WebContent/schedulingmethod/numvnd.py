import matplotlib.pyplot as plt
import numpy as np

POP_SIZE = 50
POP_VND_SIZE_l = []
for g in range(200):
    ps_vnd = 0.2
    Ps = ps_vnd * (g / 100) ** 2
    POP_VND_SIZE = int(POP_SIZE * Ps)
    POP_VND_SIZE_l.append(POP_VND_SIZE)
print(POP_VND_SIZE_l)

plt.figure()
x = range(200)
y = POP_VND_SIZE_l
plt.scatter(x, y)
plt.title("figure of the number of vnd executed")
plt.xlabel("iteration")
plt.ylabel("number of vnd executed")
plt.show()
