int_ = 31 #ist ein Integer
float_ = 31.2 #ist eine Float
str_ = "Hallo" #ist ein String
bool_ = True #ist ein Boolean
list_ = ["Hallo", "Tschüss"] #ist eine Liste
numlist = [32, 69, 15, 722]

if int_ > 30: #Namensräume
    print("die Zahl ist größer als 30")
int_ = 29
if int_ < 30:
    print("die Zahl ist kleiner als 30")

def äußere_funktion(): #äußere Funktion
    zahl = 29

    def innere_funktion(): #innere Funktion
        nonlocal zahl
        if zahl > 30:
            print("Die Zahl ist größer als 30")
        elif zahl < 30:
            print("Die Zahl ist kleiner als 30")
        else:
            print("Die Zahl ist genau 30")
        zahl += 1

    print("Wert der Zahl vor dem Aufruf der inneren Funktion:", zahl)
    innere_funktion()
    print("Wert der Zahl nach dem Aufruf der inneren Funktion:", zahl)
äußere_funktion()

x = len(list_)
print(x)

y = type(float_)
print (y)

a = sum(numlist)
print(a)

b = max(numlist)
print(b)

c = min(numlist)
print(c)

d = sorted(numlist)
print(d)
#input
e = input("Bitte gebe eine Zahl ein: ")
f = int(e) #umwandlung von str input in int
if isinstance(f, int):
    print("Die Zahl wurde erfolgreich umgewandelt")