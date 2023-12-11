for i in range(12):
    print(i)

for i in range(3, 12):
    print(i)

for i in range(3, 12, 2):
    print(i)

for c in "Ala ma kota":
    print(c)

for i in range(10):
    print(i)
else:
    print("Koniec")

for i in range(10):
    print(i)
    if i > 6:
        break
else:
    print("Koniec")

#zadanie 1
for a in range(1, 100):
    b = int(a // 10)
    c = int(a % 10)
    i = b + c
    if (i % 7 == 0 and a % 2 == 0):
        print(f" {a} liczba jest dobra")
    # else:
    #     print(f" {a} liczba jest zla")

#zadanie 2
number = input()
suma = 0
    for char in str(number):
        print(f' to jest znak {char}, to jest suma {suma}')
        suma += int(char)
    print(suma)