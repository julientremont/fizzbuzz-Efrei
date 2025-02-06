import fizzbuzz1 as fb1  # Importation du module fizzbuzz1 contenant la fonction fizzbuzStage1

def main():
    # Boucle de 1 à 100 (inclus)
    for i in range(1, 101):  
        resultat = fb1.fizzbuzStage1(i)  # Appel de la fonction fizzbuzStage1 avec la valeur i
        print(resultat)  # Affichage du résultat retourné par la fonction

# Vérification que le script est exécuté directement (et non importé comme module)
if __name__ == '__main__':
    main()  # Exécution de la fonction main
