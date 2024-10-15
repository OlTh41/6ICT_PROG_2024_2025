""" TOETS Hoofdstuk 2 -- Gebruik & Doorlopen van Dictionaries (  / 10)
De dictionary 'aandelen' stelt de aandelenportefeuille van een persoon voor.
    - Niveau 1: maak een overzicht van de aandelen.
    - Niveau 2: zorg dat de persoon aandelen kan (ver)kopen.

Het is niet verplicht om commentaar bij te code te schrijven.
Je kan dit wel doen als je de code wat meer wilt toelichten.
"""

aandelen = {
    "S&P 500": 10,
    "IWDA": 2,
}

""" Niveau 1 (   / 2)
Print een overzicht van de aandelen in de dictionary.
Zie het voorbeeld hieronder voor de opbouw van de print.
De code moet blijven werken, ook als de dictionary erna wijzigt.

VOORBEELD
---------
Uw aandelenportefeuille ziet er als volgt uit.
    - 10 shares in S&P 500.
    - 2 shares in IWDA.

"""



""" Niveau 2 (  / 8)
Herhaal het volgende tot in het oneindige.

    Vraag de gebruiker naar een aandeel.
    Vraag de gebruiker naar hoeveel shares van het aandeel deze wilt (ver)kopen.
    Wijzig de dictionary 'aandelen' om aan het verzoek van de gebruiker te voldoen.
    Print hoeveel shares van dit aandeel er nu in de dictionary zitten (zie voorbeeld).

Het herhalen moet stoppen wanneer de gebruiker 'STOP' invult in plaats van een aandeel.
Print tenslotte de gewijzigde dictionary (gebruik evt. de code uit niveau 1).

Hou rekening met volgende zaken.
    - Het aandeel bestaat al in de dictionary? Wijzig het element dan.
    - Het aandeel bestaat niet in de dictionary? Voeg dan een nieuw element toe.
    - In beide gevallen mag er nooit een negatief aantal shares in de dictionary staan.
      Mocht dit het geval zijn, print dan een fout in plaats van de dictionary te wijzigen.

VOORBEELD
---------
>>> Selecteer een aandeel: S&P 500
>>> Hoeveel shares (ver)kopen: -5
Het aandeel 'S&P 500' is gewijzigd. U heeft nu 5 shares in dit aandeel.

>>> Selecteer een aandeel: IWDA
>>> Hoeveel shares (ver)kopen: -5
Fout! U beschikt slechts over 2 shares in 'IWDA'. 5 verkopen is niet mogelijk.

>>> Selecteer een aandeel: EMIM
>>> Hoeveel shares (ver)kopen: 3
Het aandeel 'EMIM' is gewijzigd. U heeft nu 3 shares in dit aandeel.

>>> Selecteer een aandeel: STOP
Uw aandelenportefeuille ziet er als volgt uit.
    - 5 shares in S&P 500.
    - 2 shares in IWDA.
    - 3 shares in S&P 500.

"""
print(aandelen)
for l  in aandelen:
    aantal = aandelen[l]
    print(F"-{aantal} shares in {l}." )

#niveau 2
while True:
    keuze = input("kies een aandeel ")
    hoeveelheid = int(input("hoeveel je wilt kopen of verkopen "))
    if keuze.lower() == "s&p 500":
        test = aandelen["S&P 500"]
        door = test + hoeveelheid
        if door < 0:
            print("FOUT!")
        else:
            aandelen["S&P 500"] = door
    elif keuze.lower() == "iwda":
        test = aandelen["IWDA"]
        door = test + hoeveelheid
        if door < 0:
            print("FOUT!")
        else:
            aandelen["IWDA"] = door
    elif keuze.lower() == "stop":
        break
    else:
        aandelen[keuze] = hoeveelheid

print("Uw aandelenportefeuille ziet er als volgt uit.")
for l in aandelen:
    aantal = aandelen[l]
    print(f"- {aantal} shares in {l}. ")


#2.1 #vrijetijd

while True:
    keuze = input("kies een aandeel ")
    hoeveelheid = int(input("hoeveel je wilt kopen of verkopen "))
    for x in aandelen:
        if x == keuze:
            test = aandelen[keuze]
            door = test + hoeveelheid
            if door < 0:
                print("FOUT!")
            else:
                aandelen[keuze] = door
    if keuze.lower() == "stop":
        break
    if keuze not in aandelen:
        aandelen[keuze] = hoeveelheid

for l in aandelen:
    aantal = aandelen[l]
    print(f"- {aantal} shares in {l}. ")

#2.2 #vrijetijd #inGeschiendenis

while True:
    keuze = input("Kies een aandeel of type 'stop' om te stoppen: ").lower()
    if keuze == "stop":
        break
    hoeveelheid = int(input("Hoeveel wil je kopen of verkopen? "))
    aandelen[keuze] = aandelen.get(keuze, 0) + hoeveelheid
    if aandelen[keuze] < 0:
        print("FOUT!")
        aandelen[keuze] -= hoeveelheid  
for aandeel, aantal in aandelen.items():
    print(f"- {aantal} shares in {aandeel}.")