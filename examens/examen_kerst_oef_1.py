""" Oefening 1 (   / 8)
Deze oefening bestaat uit 3 niveaus, die je afzonderlijk kan maken. 
Elk niveau gebruikt de dictionary quizvragen, waarin vragen en antwoorden van een quiz staan.

Tip! Als je met een bepaald niveau bezig bent, zet de code van de andere niveaus in commentaar. 
     Dit voorkomt fouten en zorgt dat je alleen aan de code werkt die relevant is.

"""
quizvragen = {
    "2+2": "4",
    "Hoofdstad Belgie": "Brussel",
    "wat is de hoofdstand van canada": "ottawa"

}

""" Niveau 1 (   / 2)
Stel een overzicht op met de vragen/antwoorden in de dictionary.
Het overzicht moet eruit zien zoals onderstaand voorbeeld.

De code moet blijven werken ook als de inhoud van quizvragen wijzigt.
Test dit zelf uit door manueel vragen toe te voegen of te veranderen.

VOORBEELD
---------
Overzicht van vragen in quiz...
    - Vraag '2+2' heeft als antwoord '4'.
    - Vraag 'Hoofdstad Belgie' heeft als antwoord 'Brussel'.
    - (enzoverder voor iedere vraag in quizvragen)
"""

print("overzicht van vragen in quiz...")
for vraag in quizvragen:
    antwoorden = quizvragen[vraag]  
    print(f"- Vraag '{vraag}' heeft als antwoord '{antwoorden}'.")




""" Niveau 2 (   / 3)
Laat de gebruiker zelf vragen & antwoorden toevoegen aan de dictionary.
Enkel nieuwe vragen mogen toegevoegd worden aan de dictionary.
Probeert de gebruiker een reeds bestaande vraag te overschrijven,
geef dan aan dat dit niet mogelijk is.

De gebruiker moet zoveel vragen kunnen toevoegen als deze zelf wilt.
Het proces stopt pas als deze 'STOP' ingeeft.
    Tip! gebruik een loop.

Print tenslotte de aangevulde dictionary.

VOORBEELD
---------
>>> Geef een vraag op: Symbool valversnelling
>>> Geef een antwoord op: g
Nieuwe vraag toegevoegd!

>>> Geef een vraag op: 2+2
>>> Geef een antwoord op: 5
Vraag bestaat reeds, kan deze niet toevoegen!

>>> Geef een vraag op: STOP

Je hebt momenteel volgende vragen...
{'2+2': '4', 'Hoofdstad Belgie': 'Brussel', 'Symbool valversnelling': 'g'}
"""
quizvragen = {
    "2+2": "4",
    "Hoofdstad Belgie": "Brussel",
    "wat is de hoofdstand van canada": "ottawa"

}

while True:
    vraag = input("geef een vraag op: ")
    if vraag == "STOP":
        break
    antwoord = input("antwoord op: ")

    if vraag not in quizvragen:
        quizvragen[vraag] = antwoord
        print("Nieuwe vraag toegevoegd!")
    else:
        print("Vraag bestaat reeds, kan deze niet toevoegen!")

print("Je hebt momenteel volgende vragen...")
for vraag in quizvragen:
    antwoorden = quizvragen[vraag]  
    print(f"- Vraag '{vraag}' heeft als antwoord '{antwoorden}'.")



""" Niveau 3 (   / 3)
Overloop nu alle vragen in de dictionary.
De gebruiker moet voor iedere vraag een antwoord geven.

Laat de gebruiker onmiddelijk weten of het antwoord juist/fout is.
Bij een fout antwoord, verbeter de gebruiker ook (zie voorbeeld).

Na alle vragen te overlopen, vertel de gebruiker wat de score is (zie voorbeeld).

VOORBEELD
---------
We starten de quiz!
    - Wat is '2+2': 5
    Dat is fout! Het correcte antwoord was 4.
    - Wat is 'Hoofdstad Belgie': Brussel
    Dat is correct!

De quiz is afgelopen. Je hebt een score van 1/2.
"""

print("we starten de quiz")
score = 0
maxscore = len(quizvragen)
for vraag in quizvragen:
    antwoorden = quizvragen[vraag]
    antwoord = input(f"wat is {vraag}? ")
    if antwoord == antwoorden:
        print("Dat is correct!")
        score += 1
    elif antwoord != antwoorden:
        print(f"Dat is fout! Het correcte antwoord was {antwoorden}.")
print(f"de quiz is afgelopen. Je hebt een score van {score}/{maxscore}")

