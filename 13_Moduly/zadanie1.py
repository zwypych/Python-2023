import sys

def funkcja1():
    print("dzien dobry")

#zadanie
def funckja2():
    print("do widzenia")

def comowie():
    funkcja = input("przywitanie czy pozegnanie?")
    lista = {'przywitanie': funkcja1, 'pozegnanie': funckja2}
    return lista[funkcja]

s = {'przywitanie': funkcja1, 'pozegnanie': funckja2}

if __name__ == '__main__':
    print(sys.argv)
    klucz = (sys.argv[1])
    funkcja3 = s[klucz]
    funkcja3()
    print(klucz)

#wpisac w terminalu np przywitanie


