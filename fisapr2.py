from random import choice
bile = ["Alb", "Negru"]
n = int(input('Numarul de bile extrase: '))
alb = 0
negru = 0
for i in range (n):
    x=choice(bile)
    print (x)
    if x == "Alb":
        alb += 1
    elif x == "Negru":
        negru += 1
print("Numarul de bile albe este:", alb , "; si numarul de bile negre este:", negru) 