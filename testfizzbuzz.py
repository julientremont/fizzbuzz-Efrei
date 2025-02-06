import unittest  # Import du module unittest pour effectuer des tests unitaires
import fizzbuzz1 as fb1  # Import du module fizzbuzz1 contenant la fonction fizzbuzStage1

class TestFizzbuzz(unittest.TestCase):  # Définition d'une classe de test qui hérite de unittest.TestCase
    
    def test_fizzbuzz_5(self):  # Teste si l'entrée 5 retourne "Buzz"
        self.assertEqual(fb1.fizzbuzStage1(5), "Buzz")

    def test_fizzbuzz_3(self):  # Teste si l'entrée 3 retourne "Fizz"
        self.assertEqual(fb1.fizzbuzStage1(3), "Fizz")
    
    def test_fizzbuzz_15(self):  # Teste si l'entrée 15 retourne "FizzBuzz"
        self.assertEqual(fb1.fizzbuzStage1(15), "FizzBuzz")
