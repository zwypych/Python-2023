'''stworzyc funckcję alphabet_range działająca jak range ale dla liter
(z trzema parametrami - start, end, step)
przykład: alphabet_range('E') -> ['A', 'B', 'C', 'D'] - albo jeszcze lepiej generator
użyć
ord - podaje kod calkowity danego znaku
chr - podaje znak odpowiadający danemu kodowi całkowitemu'''

def alphabet_range(start, end, step):
    return [chr(x) for x in range(ord(start), ord(end), step)] #list comprehension

alphabet_range("a", "f", 1)

#generator
def alphabet_range(start, end, step):
    return (chr(x) for x in range(ord(start), ord(end), step)) #okragle nawiasy bo generator a nie list comprehension

alphabet_range("a", "f", 1)

list(alphabet_range("a", "f", 1))
