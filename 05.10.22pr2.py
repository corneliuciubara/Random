import random
n = int(input("Numarul de aruncari = "))
s = 0 
for i in range(n):
    i = random.randint(1, 6)
    print(i)
    if i == 6:
        s += 1
print("Nr 6 a fost de ", s, "ori")

