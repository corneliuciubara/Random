import random 
n = random.randint(1, 999999999)
d = int(input("Cifra"))
print("n =", n)
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
print(noc())

