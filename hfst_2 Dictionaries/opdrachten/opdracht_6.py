# Start de opdracht met onderstaande lijst.
fruitlijst = ["appel","doerian","banaan","doerian","appel","kers",
"kers","mango","appel","appel","kers","doerian","banaan",
"appel","appel","appel","appel","banaan","appel"]

fruitdic = {}

for fruit in fruitlijst:
    nummer = fruitlijst.count(fruit)
    fruitdic[fruit] = nummer

print(fruitdic)