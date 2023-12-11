l = [3, 5, 6, 7]
l

l[1]
l[0]
len(l)
l[0:2]
l[1:2]
l[1:]
l[:2]
l[-1]
l[1:-1]
l[-4]
l[1:-1] + l[0:-1]

for i in range(len(l)):
    print(l[i])

for i in l:
    print(i)

l * 4

l.index('3')  # Błąd
l.index(3)

l[1] = 17
l
del l[3]
l
l.append(19)
l
l += ['A', 'B']
l
l.pop()
l
l.index('A')

" - ".join(["Ala", "ma", "kota"])
"".join(["Ala", "ma", "kota"])
" ".join(["Ala", "ma", "kota"])
s2 = '.|.'
s2.join(["Ala", "ma", "kota"])

'.' in s2

3 in l

l.insert(2, 100)


'''
zadanie 1
#stwórz pętle pobierającą napisy z wejścia aż do napotkania pustego napisu; 
wypisz listę posortowaną alfabetycznie wczytanych napisów
'''
lista = []
while True:
    i = input("Podaj slowo")
    if (i == ""):
        break
    lista.append(i)

lista.sort(key=str)
print(lista)

'''
zadanie 2
stwórz pętle pobierającą liczby z wejścia aż do napotkania pustego napisu; 
wypisz ostatnią parzystą
'''
lista = []
while True:
    i = int(input("Podaj slowo"))
    if (i == ""):
        break
    lista.append(i)
for l in lista:
    lista.sort(reverse=True)
    if l % 2 == 0:
        break
    print

print(lista)