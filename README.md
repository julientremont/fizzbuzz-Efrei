# FizzBuzz Project

## Description
Ce projet implémente le célèbre exercice de programmation **FizzBuzz** en Python. Il contient :

- Une fonction `fizzbuzz_stage1(i)` qui retourne :
  - "Fizz" si `i` est un multiple de 3.
  - "Buzz" si `i` est un multiple de 5.
  - "FizzBuzz" si `i` est un multiple de 3 et de 5.
  - `i` lui-même sinon.
- Un script qui exécute la fonction pour les nombres de 1 à 100.
- Des tests unitaires pour valider le bon fonctionnement.

## Installation

1. **Cloner le dépôt** :
   ```bash
   git clone https://github.com/votre-utilisateur/fizzbuzz.git
   cd fizzbuzz
   ```
2. **Créer un environnement virtuel (optionnel mais recommandé)** :
   ```bash
   python -m venv venv
   source venv/bin/activate  # Sur Windows : venv\Scripts\activate
   ```
3. **Installer les dépendances** (si nécessaire) :
   ```bash
   pip install -r requirements.txt
   ```

## Utilisation

### Exécuter le programme FizzBuzz

Lancer le script principal :
```bash
python main.py
```
Cela affichera la séquence FizzBuzz de 1 à 100.

### Lancer les tests unitaires

Exécuter les tests avec :
```bash
python -m unittest test_fizzbuzz.py
```

## Structure du projet
```
.
├── fizzbuzz1.py        # Implémentation de la fonction FizzBuzz
├── main.py             # Script principal
├── test_fizzbuzz.py    # Tests unitaires avec unittest
├── README.md           # Documentation
└── requirements.txt    # (Si nécessaire, pour les dépendances)
```

## Contribuer
Les contributions sont les bienvenues !
- Forkez le projet 🍴
- Créez une branche 🔀
- Faites vos modifications 🛠️
- Ouvrez une Pull Request 📥

## Licence
Ce projet est sous licence MIT. Vous êtes libre de l'utiliser et de le modifier.

---

✨ Bon codage ! 🚀
