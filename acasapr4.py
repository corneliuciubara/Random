print("Vreau să fiu milionar")
nume = str(input("Care este numele tău?: "))
print("Salut, ", nume)
import random
print("Dimeniul matematic:  ")
m = 0
t = 0
rs1 = input("Cu cât este egal 2 + 2: ")
if rs1 == "4":
    t+=1
    m+=1
    print("Corect!")
else:
    print("Greșit!")
rs2 = input("4 la puterea 2 este egal cu: ")
if rs2 == "16":
    t+=1
    m+=1
    print("Corect!")
else:
    print("Greșit!")
rs3 = input("a + a + 3a = ")
if rs3 == "5a":
    t+=1
    m+=1
    print("Corect!")
else:
    print("Greșit!")
rs4 = input("100*100 = ")
if rs4 == "10000":
    t+=1
    m+=1
    print("Corect!")
else:
    print("Greșit!")
rs5 = input("67-7+3 = ")
if rs5 == "63":
    t+=1
    m+=1
    print("Corect!")
else:
    print("Greșit!")

rs6 = input("10 la puterea 9 este = ")
if rs6 == "1000000000":
    t+=1
    m+=1
    print("Corect!")
else:
    print("Greșit!")

rs7 = input("5 + 1000000000 = ")
if rs7 == "1000000005":
    t+=1
    m+=1
    print("Corect!")
else:
    print("Greșit!")

rs8 = input("sinus de 90° = ")
if rs8 == "1":
    t+=1
    m+=1
    print("Corect!")
else:
    print("Greșit!")

rs9 = input("50*10=")
if rs9 == "500":
    t+=1
    m+=1
    print("Corect!")
else:
    print("Greșit!")

rs10 = input("5% din 200 este = ")
if rs10 == "10":
    t+=1
    m+=1
    print("Corect!")
else:
    print("Greșit")

print("Nota la matematică:", m)


print("Domeniul Python")
i = 0
ir1 = input("Caracterul care este necesar de a scri un comenatiu este: ")
if ir1=="#":
    t+=1
    i+=1
    print("Corect!")
else:
    print("Greșit!")

ir2 = input("Extensia corectă a unui fișier python este: ")
if ir2==".py":
    t+=1
    i+=1
    print("Corect!")
else:
    print("Greșit!")

ir3 = input("Scrie sintaxa corectă care afișeaza tipul variabilei x: ")
if ir3=="print(type(x))":
    t+=1
    i+=1
    print("Corect!")
else:
    print("Greșit!")

ir4 = input("Creaza o functie cu denumirea func, care nu are parametri: ")
if ir4=="def func():":
    t+=1
    i+=1
    print("Corect!")
else:
    print("Greșit!")

ir5 = input("Operatorul care determina lungimea unei liste este: ")
if ir5=="len()":
    t+=1
    i+=1
    print("Corect!")
else:
    print("Greșit!")

ir6 = input("Operatorul care transforma toate literele mici dintr-un string in litere mari: ")
if ir6=="upper()":
    t+=1
    i+=1
    print("Corect!")
else:
    print("Greșit!")

ir7 = input("Operatorul care înlocuiește părți dintr-un string: ")
if ir7=="replace()":
    t+=1
    i+=1
    print("Corect!")
else:
    print("Greșit!")

ir8 = input("Operatorul care returneaza restul împărtirii unui nr la altul: ")
if ir8=="%":
    t+=1
    i+=1
    print("Corect!")
else:
    print("Greșit!")

ir9 = input("Care colecție e aranjată, schimbabilă, și poate multiplica membri? ")
if ir9=="list":
    t+=1
    i+=1
    print("Corect!")
else:
    print("Greșit!")

ir10 = input("Functia care oprește un ciclu: ")
if ir10=="break":
    t+=1
    i+=1
    print("Corect!")
else:
    print("Greșit!")

print("Nota la Python: ", i)

print("Domeniul fizicii:")
fi1 = input("Cu ce simbol se notaza căldura: ")
f = 0
if fi1=="Q":
    t+=1
    f+=1
    print("Corect!")
else:
    print("Greșit!")


fi2 = input("Cu ce simbol se noteaza rezistenția totală: ")
if fi2=="R":
    t+=1
    f+=1
    print("Corect!")
else:
    print("Greșit!")

fi3 = input("Cu ce simbol se noteaza impulsul: ")
if fi3=="p":
    t+=1
    f+=1
    print("Corect!")
else:
    print("Greșit!")

fi4 = input("Cu ce simbol se notează intensitatea curentului: ")
if fi4=="U":
    t+=1
    f+=1
    print("Corect!")
else:
    print("Greșit!")

fi5 = input("Cu ce simbol se notează t.e.m.: ")
if fi5=="E":
    t+=1
    f+=1
    print("Corect!")
else:
    print("Greșit!")

fi6 = input("Cu ce simbol se noteaza concentrația: ")
if fi6=="n":
    t+=1
    f+=1
    print("Corect!")
else:
    print("Greșit!")

fi7 = input("Cu ce simbol se notează pulsația: ")
if fi7=="w":
    t+=1
    f+=1
    print("Corect!")
else:
    print("Greșit!")


fi8 = input("Cu ce simbol se notează timpul: ")
if fi8=="t":
    t+=1
    f+=1
    print("Corect!")
else:
    print("Greșit!")

fi9 = input("Cu ce simbol se notează viteza: ")
if fi9=="v":
    t+=1
    f+=1
    print("Corect!")
else:
    print("Greșit!")


fi10 = input("Cu ce simbol se notează distanța: ")
if fi10=="d":
    t+=1
    f+=1
    print("Corect!")
else:
    print("Greșit!")
print("La fizică ai nota", f)

print("Domeniul biologic")
b = 0
bi1 = input("Cea mai mică unitate structurală este: ")
if bi1 == "celula":
    b+=1
    t+=1
    print("Corect!")
else:
    print("Greșit!")

bi2 = input("Procesul de producere a spermatozoizilor: ")
if bi2 == "spermatogeneza":
    b+=1
    t+=1
    print("Corect!")
else:
    print("Greșit!")

bi3 = input("Procesul care urmeaza sa formeze cromozomi: ")
if bi3 == "mitoza":
    b+=1
    t+=1
    print("Corect!")
else:
    print("Greșit!")

bi4 = input("Unitati structurale compacte, alcatuite din acizi nucleici si proteine: ")
if bi4 == "cromozomii":
    b+=1
    t+=1
    print("Corect!")
else:
    print("Greșit!")

bi5 = input("Proprietatea organismelor de a transmite caractere: ")
if bi5 == "ereditatea":
    b+=1
    t+=1
    print("Corect!")
else:
    print("Greșit!")

bi6 = input("Locul in care se pastreza informatia ereditara: ")
if bi6 == "Gene":
    b+=1
    t+=1
    print("Corect!")
else:
    print("Greșit!")

bi7 = input("Mod, rapid de diviziune a celulelor: ")
if bi7 == "amitoza":
    b+=1
    t+=1
    print("Corect!")
else:
    print("Greșit!")

bi8 = input("Proces de formare a ovarelor: ")
if bi8 == "ovogeneza":
    b+=1
    t+=1
    print("Corect!")
else:
    print("Greșit!")

bi9 = input("Gamet masculin: ")
if bi9 == "spermatozoid":
    b+=1
    t+=1
    print("Corect!")
else:
    print("Greșit!")

bi10 = input("Gamet feminin: ")
if bi10 == "ovul":
    b+=1
    t+=1
    print("Corect!")
else:
    print("Greșit!")

print("La biologie ai nota:", b)

print("Domeniul C++:")

c = 0
c1 = input("Scrie sinaxa care afiseaza Hello World: ")
if c1 == "cout<<'Hello World';":
    c+=1
    t+=1
    print("Corect!")
else:
    print("Greșit!")

c2 = input("Operatorul de inserare a comentariilor: ")
if c2 == "//":
    c+=1
    t+=1
    print("Corect!")
else:
    print("Greșit!")

c3 = input("Tipul de date in care stochezi text: ")
if c3 == "string":
    c+=1
    t+=1
    print("Corect!")
else:
    print("Greșit!")

c4 = input("Creaza o variabila x cu valoarea numerica intreaga 5: ")
if c4 == "int x=5;":
    c+=1
    t+=1
    print("Corect!")
else:
    print("Greșit!")

c5 = input("Operatorul care aduna 2 numere: ")
if c5 == "+":
    c+=1
    t+=1
    print("Corect!")
else:
    print("Greșit!")

c6 = input("Care fisier ne permite sa lucram cu obiecte de introducere si afisare? ")
if c6 == "#include <iostream>":
    c+=1
    t+=1
    print("Corect!")
else:
    print("Greșit!")

c7 = input("Indexul unui array incepe cu: ")
if c7 == "0":
    c+=1
    t+=1
    print("Corect!")
else:
    print("Greșit!")

c8 = input("Apeleaza functia func: ")
if c8 == "func();":
    c+=1
    t+=1
    print("Corect!")
else:
    print("Greșit!")

c9 = input("Cuvantul cheie de creare unei clase: ")
if c9 == "class":
    c+=1
    t+=1
    print("Corect!")
else:
    print("Greșit!")

c10 = input("Creaza un obiect myObj din clasa myClass: ")
if c10 == "myClass myObj;":
    c+=1
    t+=1
    print("Corect!")
else:
    print("Greșit!")
print("Nota la C++:", c)

print("Punctaj total:", t, "din 50")
if t==50:
    print("Ai punctaj maximal, vei fi milionar!")
else:
    print("Normal")




















