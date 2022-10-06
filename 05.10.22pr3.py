import random 
n = random.randint(1, 999999999)
d = 1
f = 2
g = 3
h = 4
j = 5
k = 6 
l = 8
m = 9
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
def noc1():
    global n 
    global f
    count = 0
    while (n > 0):  
        if(n % 10 == f):
            count = count + 1
        n = n // 10
    return count
def noc2():
    global n
    global g
    count = 0
    while (n > 0):  
        if(n % 10 == g):
            count = count + 1
        n = n // 10
    return count
def noc3():
    global n 
    global h
    count = 0
    while (n > 0):  
        if(n % 10 == h):
            count = count + 1
        n = n // 10
    return count
def noc4():
    global n 
    global j
    count = 0
    while (n > 0):  
        if(n % 10 == j):
            count = count + 1
        n = n // 10
    return count
def noc5():
    global n 
    global k
    count = 0
    while (n > 0):  
        if(n % 10 == k):
            count = count + 1
        n = n // 10
    return count
def noc6():
    global n 
    global l
    count = 0
    while (n > 0):  
        if(n % 10 == l):
            count = count + 1
        n = n // 10
    return count
def noc7():
    global n 
    global m
    count = 0
    while (n > 0):  
        if(n % 10 == m):
            count = count + 1
        n = n // 10
    return count
print("Numarul de aparitii a lui", d, "sunt:", noc())
print("Numarul de aparitii a lui", f, "sunt:", noc1())
print("Numarul de aparitii a lui", g, "sunt:", noc2())
print("Numarul de aparitii a lui", h, "sunt:", noc3())
print("Numarul de aparitii a lui", j, "sunt:", noc4())
print("Numarul de aparitii a lui", k, "sunt:", noc5())
print("Numarul de aparitii a lui", l, "sunt:", noc6())
print("Numarul de aparitii a lui", m, "sunt:", noc7())
