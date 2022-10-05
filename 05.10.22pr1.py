import random 
n = int(input("Numarul de cifre = "))
sp = 0
sn = 0
for i in range(n):
    i = random.randint(-50, 50)
    print(i)
    if i < 0:
        sp += i
    if i > 0:
        sn += i
print("Spoz =", sn)
print("Sneg =",sp)
