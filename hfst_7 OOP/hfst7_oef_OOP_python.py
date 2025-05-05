""" STOPWATCH UITLEG (  / 10)
Je krijgt hieronder een korte beschrijving van wat een stopwatch moet kunnen.
Maak op basis van deze beschrijving een klasse met correcte eigenschappen en methoden.
Maak ook een object aan van deze klasse waarin je alle onderdelen van de stopwatch test.

Een stopwatch is een apparaat waarmee men zaken kan timen. Deze kan het volgende:
    - Een gebruiker kan de stopwatch starten (tenzij deze al gestart is).
    - Een gebruiker kan de stopwatch stoppen (tenzij deze al gestopt is).
    - Een gebruiker kan de stopwatch resetten (tijd terug op nul zetten).
    - De gebruiker kan opvragen hoeveel seconden er op de stopwatch staat.

De stopwatch moet dus kunnen bijhouden wanneer deze gestart/gestopt is, 
en kunnen berekenen hoeveel tijd er tussen deze twee gepasseerd is.
Als de stopwatch nog loopt tijdens het opvragen,
berekent deze het verschil tussen de start tijd en de huidige tijd. 

Gebruik de time-module van Python om met tijd te werken.
Via de functie 'time.time()' kan je de huidige tijd opvragen in seconden.
Via de functie 'time.sleep()' kan je testen of de stopwatch correct werkt.
"""

""" STOPWATCH VOORBEELD
Gebruiker start de stopwatch, en stopt deze 2 seconden later.
De tijd opvragen geeft 2 terug.

Gebruiker start stopwatch opnieuw, en stopt deze 3 seconden later.
De tijd opvragen geeft 5 terug.

Gebruiker reset de stopwatch.
De tijd opvragen geeft 0 terug.

Gebruiker start stopwatch en vraagt na 4 seconden de tijd op.
De tijd opvragen geeft 4 terug. (maar de stopwatch loopt wel nog altijd!)
"""
import time

class Stopwatch:
    start_time = 0
    time = 0
    running = False
    def start(self):
        if not self.running:
            self.start_time = time.time()
            self.running = True
            print("Stopwatch gestart.")
        else:
            print("Stopwatch is al gestart.")
    def stop(self):
        if self.running:
            self.time += time.time() - self.start_time
            self.running = False
            print("stopwatch is gestopt")
    def reset(self):
        self.time = 0
    def tijdopvragen(self):
        if self.running:
            self.time = time.time() - self.start_time + self.time
            print(self.time)
        else:
            print(self.time)

stopwatch = Stopwatch()


stopwatch.start()
time.sleep(2)
stopwatch.stop()
stopwatch.tijdopvragen()
print("klaar")
stopwatch.start()
time.sleep(2)
stopwatch.stop()
stopwatch.start()
time.sleep(3)
stopwatch.stop()
stopwatch.reset()
stopwatch.tijdopvragen()
print("klaar")
stopwatch.start()
time.sleep(2)
stopwatch.stop()
stopwatch.reset()
stopwatch.tijdopvragen()
print("klaar")
stopwatch.start()
time.sleep(4)
stopwatch.tijdopvragen()
print("klaar")
