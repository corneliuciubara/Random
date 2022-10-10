import random
n = int(input("Numarul de aruncari = "))
s = 0 
for i in range(n):
    y = random.randint(1, 6)
    print(y)
    if i == 6:
        s += 1
print("Numarul 6 a aparut de ", s, "ori")

