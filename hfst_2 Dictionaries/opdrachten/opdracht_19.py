# Gebruik onderstaande gemengde structuur om de opdracht op te lossen.
vlucht_reservering_systeem = {
    'vluchten': {
        'VL001': {
            'van': 'New York',
            'naar': 'Los Angeles',
            'vertrektijd': '2023-09-01 10:00',
        },
        'VL002': {
            'van': 'Chicago',
            'naar': 'Miami',
            'vertrektijd': '2023-09-02 12:00',
        },
        # Meer vluchtvermeldingen...
    },
    'passagiers': {
        'P001': {
            'naam': 'Alice Smith',
            'geboekte_vluchten': ['VL001'],
        },
        'P002': {
            'naam': 'Bob Johnson',
            'geboekte_vluchten': ['VL002'],
        },
        # Meer passagiersvermeldingen...
    }
}

print("dag beste gebruiker, Waarmee kan ik u helpen?")
print("1) boeken van een vlucht? ")#niveau 1
print("2) Lijst van passagiers op de vlutch tonen.")#niveau 2
keuze = input("welke optie selecteren")