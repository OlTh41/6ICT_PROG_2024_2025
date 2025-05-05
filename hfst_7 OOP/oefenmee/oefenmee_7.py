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
    def wijzig_naam(self, naam):
        self.naam = naam
        print(self.naam)
    def eten(self, hoeveel):
        self.massa += hoeveel
        print(self.massa)
    #

hond = Hond("Max", "34")

hond.woof()
#niveau 2
hond.weegschaal()




" Via onderstaande code kan je niveau 1 testen. "
hond = Hond("Lucky", 5)
hond.wijzig_naam("Bolly")

" Via onderstaande code kan je niveau 2 testen. "
# hond = Hond("Lucky", 5)
# hond.eten(0.5)
# hond.eten(0.5)
# hond.eten(0.5)

" Stel de test voor niveau 3 zelf op. "