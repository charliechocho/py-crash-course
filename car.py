class Car:
    """Defining a car with a class"""
    def __init__(self, tillverkare, modell, year):
        """Initialisera delar som beskriver en bil"""
        self.tillverkare = tillverkare
        self.modell = modell
        self.year = year
        self.mil_tal = 230

    def get_descriptive_name(self):
        """Visa ett beskrivande namn på ett formaterat sätt"""
        car_item = f"{self.year} {self.tillverkare} {self.modell}"
        return car_item.title()

    def mil_tal_in(self):
        """Printa det antal mil en bil gått"""
        print(f"Den här bilen har gått {self.mil_tal} kilometer")

    def mil_update(self, kilometer):
        """Metod för att uppdatera kilometerantalet baserat på okänd input"""

        if kilometer >= self.mil_tal:
            self.mil_tal = kilometer
        else:
            print("Du kan inte rulla tillbaks kilometertalet!!")
        


min_bil = Car('bmw', 'M135i', 2020)

print(f"{min_bil.tillverkare}")

print(min_bil.get_descriptive_name())
min_bil.mil_update(231)
min_bil.mil_tal_in()