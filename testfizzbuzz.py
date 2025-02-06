import unittest  # Import du module unittest pour effectuer des tests unitaires
import fizzbuzz1 as fb1  # Import du module fizzbuzz1 contenant la fonction fizzbuzStage1

class TestFizzbuzz(unittest.TestCase):  # Définition d'une classe de test qui hérite de unittest.TestCase
    
    def test_fizzbuzz_5(self):  # Teste si l'entrée 5 retourne "Buzz"
        result = fb1.fizzbuzStage1(5)
        print(f"Test input 5: resultat attendu:'Buzz', resultat:'{result}' - {'Success' if result == 'Buzz' else 'Fail'}")
        self.assertEqual(result, "Buzz")

    def test_fizzbuzz_3(self):  # Teste si l'entrée 3 retourne "Fizz"
        result = fb1.fizzbuzStage1(3)
        print(f"Test input 3: resultat attendu:'Fizz', resultat:'{result}' - {'Success' if result == 'Fizz' else 'Fail'}")
        self.assertEqual(result, "Fizz")
    
    def test_fizzbuzz_15(self):  # Teste si l'entrée 15 retourne "FizzBuzz"
        result = fb1.fizzbuzStage1(15)
        print(f"Test input 15: resultat attendu:'FizzBuzz', resultat:'{result}' - {'Success' if result == 'FizzBuzz' else 'Fail'}")
        self.assertEqual(result, "FizzBuzz")

if __name__ == "__main__":
    unittest.main()
