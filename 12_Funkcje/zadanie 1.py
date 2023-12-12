'''stworzyc słownik { 'first': funkcja1, 'second': funkcja2 }, wczytać przez input klucz, wywołać funkcję'''

def funkcja1():
    print("dzien dobry")

def funckja2():
    print("do widzenia")

def comowie():
    funkcja = input("przywitanie czy pozegnanie?")
    lista = {'przywitanie': funkcja1, 'pozegnanie': funckja2}
    return lista[funkcja]

a = comowie()
a()