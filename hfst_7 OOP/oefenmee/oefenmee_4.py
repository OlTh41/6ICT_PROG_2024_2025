# Werk verder met de klasse Hond van oefen mee 2.
class Hond():
    def benoem(self, naam):
        Hond.naam = naam
    def wegen(self, massa):
        Hond.massa = massa
    def weegschaal(self):
        print(f"{self.naam} weegt {self.massa} kg")

" Via onderstaande code kan je niveau 1 testen. "
hond = Hond()
hond.benoem("Fleur")
print( hond.naam )


" Via onderstaande code kan je niveau 2 testen. "
dier = Hond()
dier.benoem("Fifi")
dier.wegen(3)
print( dier.massa )
dier.weegschaal()
dier.weegschaal()