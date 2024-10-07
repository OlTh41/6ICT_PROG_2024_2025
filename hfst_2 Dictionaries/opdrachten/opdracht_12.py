# Start de opdracht met onderstaande dictionary.
land_hoofdstad = { 
    "belgie": "brussel",
    "frankrijk": "parijs",
    "nederland": "amsterdam",
    "duitsland": "berlijn",
    "engeland": "londen",
}
print(land_hoofdstad.)
score = 0
vragen = 0
for land in land_hoofdstad:
    antwoord = input(f"wat is de hoofdstad van {land}? ")
    if antwoord == land_hoofdstad[land]:
        print("goed")
        score += 1
        vragen += 1
    else:
        print("fout")
        vragen += 1
print(f"je hebt {score}/{vragen} goed")
#niveau 2
import random
vraag1 = random.randint (0, 5)
vraag2 = random.randint (0, 5)
vraag3 = random.randint (0, 5)
antwoord1 = input(f"wat is de hoofdstad van {land_hoofdstad[vraag1]}? ")
if antwoord1 == land_hoofdstad[land]:
        print("goed")
        score += 1
antwoord2 = input(f"wat is de hoofdstad van {land_hoofdstad[vraag2]}? ")
if antwoord2 == land_hoofdstad[land]:
        print("goed")
        score += 1
antwoord3 = input(f"wat is de hoofdstad van {land_hoofdstad[vraag3]} ")
if antwoord3 == land_hoofdstad[land]:
        print("goed")
        score += 1
