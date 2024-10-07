# Start de opdracht met onderstaande code.
deelnemers = ["Lucas", "Emma", "Jan", "Piet", "Maud"]

deelnemers_talen = {    
    "Lucas": "python",    
    "Piet": "assembly",    
    "Maud": "ruby"
}

for deelnemer in deelnemers:
    if deelnemer in deelnemers_talen:
        print(f"bedankt {deelnemer}")


    else:
        print(f"je zit niet in de lijst {deelnemer}")
        print(f"vul de poll in")
        antwoord = input("Wat is je favoriete taal: ")
        if antwoord == "":
            pass
        else:
            deelnemers_talen[deelnemer]= antwoord
print(deelnemers_talen)