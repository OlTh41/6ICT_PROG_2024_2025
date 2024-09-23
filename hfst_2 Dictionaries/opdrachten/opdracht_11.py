# Gebruik onderstaande code om deze opdracht op te lossen.

# Pad naar het bestand (Plak in variabele het relatieve pad)
pad = "6ICT_PROG_2024_2025/hfst_2 Dictionaries/opdrachten/opdracht_11_lied.txt"

# Open het tekstbestand met lied & zet inhoud van lied in string.
with open(pad, "r") as fp:
    lied = fp.read()

# Haal witregels weg uit string & zet string om naar lijst.
lied = lied.replace("\n","")
lied = lied.split()

# Print lied (om te testen dat het werkt)
liedwoorden = {}

for woord in lied:
    nummer = lied.count(woord)
    liedwoorden[woord] = nummer

print(liedwoorden)

#niveau 2


lied = {key:value for key, value in sorted(liedwoorden.items(), key=lambda my_dict: my_dict[1], reverse=True)}

print(lied)


