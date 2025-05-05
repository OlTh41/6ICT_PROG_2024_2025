# Werk verder met de klasse Hond van oefen mee 1.

class Hond():
    def __init__(self, naam, massa, ):
        self.naam = naam
        self.massa = massa
    def hond(self):
        print("De hond heet", self.naam, "en de massa", self.massa, "kg")
    def woof(self):
        print(f"{self.naam} zegt Woof")
    #niveau 2
    def weegschaal(zichzelf):
        print(f"{zichzelf.naam} weegt {zichzelf.massa} kg")
    #

hond = Hond("Max", "34")

hond.woof()
#niveau 2
hond.weegschaal()

