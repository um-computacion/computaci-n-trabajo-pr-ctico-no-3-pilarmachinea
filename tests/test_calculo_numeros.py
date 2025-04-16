import sys
import os
import unittest
from unittest.mock import patch
from src.mis_exceptions import ingrese_numero, NumeroDebeSerPositivo

class TestCalculoNumeros(unittest.TestCase):

    @patch('builtins.input', return_value='100')
    def test_ingreso_feliz(self, patch_input):
        numero = ingrese_numero()
        self.assertEqual(numero, 100)

    @patch('builtins.input', return_value='-100')
    def test_ingreso_negativo(self, patch_input):
        with self.assertRaises(Exception):  
            ingrese_numero()

    @patch('builtins.input', return_value='AAA')
    def test_ingreso_letras(self, patch_input):
        with self.assertRaises(Exception):  
            ingrese_numero()


if __name__ == "__main__":
    unittest.main()
