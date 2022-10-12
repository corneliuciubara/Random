sirnume = ["Ion", "Vlaimir", "Vadim", "Maxim", "Ovidiu", "Ana", "Mihaiela", "Cornelia"]
def Cautare(parametru):
    for i in sirnume:
        i = input("Numele elevului: ")
        if i in sirnume:
            return print("Numele este in lista")
        else:
            return print("Numele nu este in lista")
print(Cautare(sirnume))