import unittest
import fizzbuzz1 as fb1

class TestFizzbuzz(unittest.TestCase):
    def test_fizzbuzz_5(self):
        self.assertEqual(fb1.fizzbuzStage1(5), "Buzz")

    def test_fizzbuzz_3(self):
        self.assertEqual(fb1.fizzbuzStage1(3), "Fizz")
    
    def test_fizzbuzz_15(self):
        self.assertEqual(fb1.fizzbuzStage1(15), "FizzBuzz")
