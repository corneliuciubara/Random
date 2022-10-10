import random 
n = int(input("Numarul de cifre = "))
spoz = 0
sneg = 0
for i in range(n):
    i = random.randint(-50, 50)
    print(i)
    if i > 0:
        spoz += i
    if i < 0:
        sneg += i
print("Spoz =", spoz)
print("Sneg =",sneg)
