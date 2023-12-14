import sys

class Instrument:
    def mysound(self):
        return "!&$%$^%*"

    def play(self):
        print(f"{self.player}@{self.__class__.__name__}: {self.mysound()}")

    def __init__(self, player):
        self.player = player


class Drums(Instrument):
    def __init__(self, player):
        super().__init__(player)

    def mysound(self):
        return "Booom Booooom"


class Guitar(Instrument):
    def __init__(self, player):
        super().__init__(player)

    def mysound(self):
        return "Pilim pilim"


class Saxophone(Instrument):
    def __init__(self, player):
        super().__init__(player)

    def mysound(self):
        return "Fiufiu"


if __name__ == '__main__':
    orkiestra = []
    for wpis in sys.argv[1:]:
        muzyk, instrument = tuple(wpis.strip().split('@'))
        orkiestra.append(
            globals()[instrument](muzyk)
        )
    for instrument in orkiestra:
        instrument.play()

# w terminalu: python fabryka_zadanie1.py Bill@Guitar John@Guitar Bob@Drums