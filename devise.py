def convertir(montant, taux):
    return montant * taux

def convertisseur():
    print("Bienvenue dans le convertisseur de devises !")

    taux_de_change = {
        "USD": 1.18,  # Taux de change USD vers EUR
        "GBP": 0.85,  # Taux de change GBP vers EUR
        "JPY": 132.12,  # Taux de change JPY vers EUR
        "CAD": 1.46,  # Taux de change CAD vers EUR
        "AUD": 1.62  # Taux de change AUD vers EUR
    }

    montant = float(input("Entrez le montant à convertir : "))
    devise_source = input("Entrez la devise source (ex : USD, GBP, JPY) : ")
    devise_cible = input("Entrez la devise cible (ex : USD, GBP, JPY) : ")

    if devise_source in taux_de_change and devise_cible in taux_de_change:
        taux_source = taux_de_change[devise_source]
        taux_cible = taux_de_change[devise_cible]

        # Conversion de la devise source vers EUR
        montant_eur = convertir(montant, 1/taux_source)

        # Conversion d'EUR vers la devise cible
        montant_cible = convertir(montant_eur, taux_cible)

        print(f"{montant} {devise_source} équivaut à {montant_cible} {devise_cible}")
    else:
        print("Devise non prise en charge")

if __name__ == "__main__":
    convertisseur()