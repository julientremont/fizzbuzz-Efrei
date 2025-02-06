# FizzBuzz Project

## Description
Ce projet implémente le célèbre exercice de programmation **FizzBuzz** en Python. Il contient :

- Une fonction `fizzbuzz_stage1(i)` qui retourne :
  - "Fizz" si `i` est un multiple de 3.
  - "Buzz" si `i` est un multiple de 5.
  - "FizzBuzz" si `i` est un multiple de 3 et de 5.
  - `i` lui-même sinon.
- Un script qui exécute la fonction pour les nombres de 1 à 100.
- Des tests unitaires pour valider le bon fonctionnement avec une couverture de code (`coverage`).
- Une intégration des tests via **GitHub Actions**.
- Une exécution dans un **conteneur Docker**.

## Installation

1. **Cloner le dépôt** :
   ```bash
   git clone https://github.com/votre-utilisateur/fizzbuzz.git
   cd fizzbuzz
   ```
2. **Créer un environnement virtuel (recommandé)** :
   ```bash
   python -m venv venv
   source venv/bin/activate  # Sur Windows : venv\Scripts\activate
   ```
3. **Installer les dépendances** :
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

### Lancer les tests unitaires avec couverture

Exécuter les tests avec `unittest` et `coverage` :
```bash
coverage run -m unittest discover
coverage report -m
```

### Générer un rapport HTML de couverture
```bash
coverage html
```
Le rapport sera disponible dans le dossier `htmlcov/`.

## Intégration continue avec GitHub Actions

Un workflow GitHub Actions est configuré pour exécuter automatiquement les tests et générer un rapport de couverture.

Créer un fichier `.github/workflows/tests.yml` avec :
```yaml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Installer Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Installer les dépendances
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          pip install coverage
      - name: Exécuter les tests avec coverage
        run: |
          coverage run -m unittest discover
          coverage report -m
```

## Exécution avec Docker

Un fichier `Dockerfile` est inclus pour exécuter le programme dans un conteneur.

### Construire l'image Docker
```bash
docker build -t fizzbuzz .
```

### Exécuter le conteneur
```bash
docker run --rm fizzbuzz
```

### Lancer les tests dans Docker
```bash
docker run --rm fizzbuzz python -m unittest discover
```

## Structure du projet
```
.
├── fizzbuzz1.py        # Implémentation de la fonction FizzBuzz respectant PEP 8
├── main.py             # Script principal avec docstrings conformes à PEP 257
├── test_fizzbuzz.py    # Tests unitaires avec unittest
├── Dockerfile          # Fichier de configuration Docker
├── .github/workflows   # Configuration GitHub Actions
├── README.md           # Documentation
├── requirements.txt    # Liste des dépendances
└── htmlcov/            # Rapport de couverture HTML (généré après tests)
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

