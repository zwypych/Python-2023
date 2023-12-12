range(10)

list(range(10))

(x * x for x in range(10))

[x for x in range(10)]

[x * x for x in range(10)]

[x for x in range(10) if x % 2 == 0]

[x * x for x in range(10) if x % 2 == 0]

[(x, y, x * y) for x in range(3) for y in range(4)]

{x for x in range(10)}

{x // 2 for x in range(10)}

{x: x * x for x in range(10) if x % 2 == 0}

#zadanie
'''Stworzyć list comprehension tupli składających się z w/w liczb całkowitych i ich reprezentacji jako napis'''


nazwy_jednosci = {0: "", 1: "jeden", 2: "dwa", 3: "trzy", 4: "cztery", 5: "pięć", 6: "sześć", 7: "siedem", 8: "osiem",
                  9: "dziewięć"}
dziesiatki = {0: "", 10: "dziesiec", 20: "dwadziescia", 30: "trzydziesci", 40: "czterdziesci", 50: "piecdziesiat",
              60: "szescdziesiat", 70: "siedemdziesiat", 80: "osiemdziesiat", 90: "dziewiecdziesiat"}

nastki = {11: "jedenascie", 12: "dwanascie", 13: "trzynascie", 14: "czternascie", 15: "pietnascie",
          16: "szesnascie", 17: "siedemnascie", 18: "osiemnascie", 19: "dziewietnascie"}

setki = {0: "", 100: "sto", 200: "dwiescie", 300: "trzysta", 400: "czterysta", 500: "piecset", 600: "szescset",
         700: "siedemset", 800: "osiemset", 900: "dziewiecset", 1000: "tysiac"}

n = int(input("Wpisz liczbe:"))
napis = setki[n-n % 100]
n %= 100
if n in range(11, 20):
    napis += nastki[n]
else:
    napis += setki[n - n % 100] + " " + dziesiatki[n - n % 10] + " " + nazwy_jednosci[n % 10]

print(napis)

[(x,str(x)) for x in range(10)]

#zadanie 3
'''biorąc słownik {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600,
 "Bicycle": 7, "Motorcycle": 110} stworzyć list comprehension nazw pojazdów cięższych niż 5000
Nazwy podać dużymi literami (uppercase) `'''

slownik_sam = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600,
 "Bicycle": 7, "Motorcycle": 110}


lista = [x for x in slownik_sam.keys() if slownik_sam[x] > 5000]
print(lista)
