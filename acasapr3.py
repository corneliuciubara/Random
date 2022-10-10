import random
n = random.randint(100,999)
print("n =",n)
if n>0 and n%6==0 and n%8==0:
    print("Numarul n este divizibil cu 6 si cu 8")
else:
    print("Numarul n nu este divizibil cu 6 si cu 8")
