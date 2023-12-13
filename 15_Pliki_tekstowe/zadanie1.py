'''Stwórz czytnik plików CSV bez użycia modułu CSV

napisz skrypt który otworzy plik z danymi csv (nazwa podana z CLI)
wypisze jego zawartość oddzielając pola tabulacją \t
Stwórz czytnik plików CSV bez użycia modułu CSV

napisz skrypt który otworzy plik z danymi csv (nazwa podana z CLI)
wypisze jego zawartość jako listę słowników {klucz:wartosc, klucz:wartosc ... }
z kluczami wziętymi z pierwszej linijki pliku CSV'''

#zadanie 1

import os
print(os.getcwd())

with open('data/foods.csv') as f:
    for l in f:
        dane = l.strip().split(',')
        print ("\t".join(dane))

#######zadanie 2

import os
print(os.getcwd())

first_line = None
data = []
with open('data/foods.csv') as f:
    for l in f:
        if first_line is None:
            first_line = l.strip().split(',')
        else:
            dane = l.strip().split(',')

            slownik = dict(zip(first_line, dane))
            print(slownik)