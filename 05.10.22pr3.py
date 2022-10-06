import random 
n = random.randint(1, 999999999)
print("n =", n)
d = int(input("Introduce cifra: "))
s = 0
def noc():
    global n 
    global d
    count = 0
    while (n > 0):  
        if(n % 10 == d):
            count = count + 1
        n = n // 10
    return count
if d>0 and d<10:
    print("Numarul de aparitii al lui", d, "este:", noc())
else:
    print("Cifra", d, "nu este inte 1 si 9")
