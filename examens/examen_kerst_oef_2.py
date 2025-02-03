""" Oefening 2 (   / 4)
Onderstaande geneste dictionary toont een weervoorspelling voor Brussel. 
Onder de geneste dictionary zijn de opgaves van deze oefening te vinden.
"""

weer_data = {
    "locatie": "Brussel",
    "huidig_weer": {
        "temp": 220, "vochtigheid": 110, "omstandigheden": "Deels bewolkt",
    },
    "voorspelling": {
        "vandaag": {
            "hoge_temp": 24, "lage_temp": 16, "overig": ["10% kans op regen", "Wind: 5 km/u"],
        },
        "morgen": {
            "hoge_temp": 25, "lage_temp": 17, "oveurig": ["Geen neerslag verwacht", "Wind: 7 km/u"],
        },
        "overmorgen": {
            "hoge_temp": 23, "lage_temp": 15, "overig": ["40% kans op regen", "Wind: 10 km/u"],
        },
    },
    "waarschuwingen": ["Hitteadvies", "Smog-gevaar", "tropische bui"],
}

""" Niveau 1 (   / 1)
Print de zin "Wind: 5 km/u" door deze op te halen uit de dictionary.
    Tip! Zoek de zin met behulp van CTRL + F.
"""

print(weer_data["voorspelling"]["vandaag"]["overig"][1])

""" Niveau 2 (   / 1)
Het element "vochtigheid" bevat een fout. 
Ze geven hier een vochtigheid van 110. Verander deze waarde naar 65.
"""
weer_data["huidig_weer"[1]] = "65"
print(weer_data["huidig_weerp"[1]])

""" Niveau 3 (   / 1)
De sleutel "oveurig" in "morgen" is verkeerd gespeld. Corrigeer dit naar "overig".
Zorg ervoor dat de waarde verbonden aan deze sleutel wel hetzelfde blijft.
Print daarna de dictionary ter controle.
"""
weer_data["voorspelling"]["morgen"]["overige"] = weer_data["voorspelling"]["morgen"].pop("oveurig")
print(weer_data["voorspelling"]["morgen"])


""" Niveau 4 (   / 1)
Print voor iedere dag in "voorspellingen" de laagste temp.
De print moet er als volgt uitzien.

Warmste temp voor de komende dagen:
    - vandaag: 16°C
    - morgen: 17°C
    - overmorgen: 15°C

De code moet blijven werken, ook als men erna extra dagen toevoegt.
Tip! Maak eerst een nieuwe variabele met de waarde van sleutel "voorspellingen".
     Overloop deze met een for-loop.
"""

for dag in weer_data["voorspelling"]:
    print(f"laagst temp voor de komende dagen: - {dag}: {weer_data['voorspelling'][dag]['lage_temp']}°C")                                                   
