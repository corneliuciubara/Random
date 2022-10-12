import random
a = str(random.randint(0, 99))
b = str(random.randint(1, 999))
c = str(0)
if len(a) == len(b):
    for i in range(0, len(b)):  
        if int(a)%2==0 and int(b)%2>0:  
            c[i] = a[i] - b[i]
        if int(a)%2>0 and int(b)%2==0:  
            c[i] = a[i] + b[i]
        if (int(a)%2==0 and int(b)%2==0) or (int(a)%2>0 and int(b)%2>0):  
            c[i] = a[i] * b[i]
else:
    print("Lungimea sirului A este diferita de lungimea sirului B")
print("A =", a)
print("B =", b)
print("C =", c)

