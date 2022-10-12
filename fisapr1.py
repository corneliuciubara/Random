import random 
lst = []
n = int(input("n = "))
if n >= 1 and n <= 20:    
    for i in range(n):
        lst.append(random.randint(1, 20))
    print(lst)
    print("Cea mai mare valoare: ", max(lst))
else:
    print("Bilele pot fi notate doar de la 1 la 20")