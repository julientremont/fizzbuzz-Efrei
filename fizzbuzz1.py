def fizzbuzStage1(i):
    # Vérifie si i est un multiple de 3 et de 5 (priorité à ce cas pour éviter des conflits)
    if i % 3 == 0 and i % 5 == 0:
        return "FizzBuzz"
    # Vérifie si i est un multiple de 3 uniquement
    elif i % 3 == 0:
        return "Fizz"
    # Vérifie si i est un multiple de 5 uniquement
    elif i % 5 == 0:
        return "Buzz"
    # Si i n'est ni un multiple de 3 ni de 5, retourne i
    else:
        return i
