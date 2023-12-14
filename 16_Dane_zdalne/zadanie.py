'''Pobrać dane z https://restcountries.com/v3.1/name/Poland?fullText=true;
Wyświetlić podstawowe informacje (np. il. mieszkańców, waluta itp.)
Stworzyć skrypt który z linii poleceń przyjmie nazwę kraju i dal niego wyświetli w/w dane'''

import requests
from pprint import pprint
import sys

url = "https://restcountries.com/v3.1/name/Poland?fullText=true"
response = requests.request(method="GET", url=url)

# pprint(response.json())
#
data = response.json()[0]
# pprint(data.keys())

#keys jest generatorem wiec trzeba list uzyc

# pprint(data.keys())
print(f'Ludnosc:\t\t{data["population"]}')
print(f'Powierzchnia:\t{data["area"]}')
print(f'Waluta:\t\t\t{list(data["currencies"].keys())[0]}')
print(f'Stolica:\t\t{data["capital"][0]}')

if __name__ == '__main__':
    print(sys.argv)
    klucz = (sys.argv[1])
    funkcja3 = s[klucz]
    funkcja3()
    print(klucz)