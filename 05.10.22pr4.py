import random
z1 = random.randint(1,6)
z2 = random.randint(1,6)
z11 = random.choice(z1)
z22 = random.choice(z2)
print("Zarul 1 are fata:", z11)
print("Zarul 2 are fata:", z22)
if z11 == z22:
    print(z11+z22)
else:
    print("Zarurile nu au fete comune")

