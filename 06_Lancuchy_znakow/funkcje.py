napis = "ala ma kota"
napis = napis.upper()
napis
napis = napis.lower()
napis
napis = napis.title()
napis.replace('Ala', 'Tomek')
napis
napis = napis.replace('Ala', 'Tomek')
napis

napis = 'AAAAKupię kota    '
napis.count('A')
napis = napis.strip()
napis
napis = napis.strip('A')
napis



napis = 'AAAAKupię kota    '
napis.find('z')
napis.find('kot')
napis[napis.find('kot')]
n = napis.find('k')
napis[n:n+3]

napis = "ala ma kota"
napis = napis.title().replace('Ala', 'Tomek')
napis

#zadanie - choinka
liczba = int(input("Podaj liczbe"))
for i in range(1, liczba):
    print(f'{-i*" "}{i*"*"}{i*" "}')
for j in range(1, 3):
        print(f'{-j * " "}{j * "*"}')

#rozwiazanie wspolne
n = int(input("Podaj wysokosc:"))
for i in range(n):
    print(f'{" "*(n-i)}{(2*i+1)*"*"}')
for i in range(n):
    if i == 2:
        break
    print(f'{" " * (n - i)}{(2 * i + 1) * "*"}')



