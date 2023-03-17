try:
    import sys
    import os
    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../src'
            )
        )
    )
except:
    raise


"""
TDD - Desenvolvimento Orientado por Testes

Parte 1 - Criar teste e ver falhar (Red)
Parte 2 - Criar o codigo e ver o teste passar (Green)
Parte 3 - Melhorar o codigo
"""
import unittest
from ricewithbean import rice_with_bean


class TestRicewithBean(unittest.TestCase):
    def test_ricewithbean_raise_exception_if_not_recived_int(self):
        with self.assertRaises(AssertionError):
            rice_with_bean('')


    def test_ricewithbean_return_rice_with_beans_if_recived_a_multiple_of_3_and_5(self):
        entries = (15, 30, 45, 60)
        out = 'Rice with beans'
        
        for entrie in entries:
            with self.subTest(entrie=entrie, out=out):
                self.assertEqual(
                    rice_with_bean(entrie), out,
                    msg=f'"{entrie}" didnt return "{out}"'
                    )

    def test_ricewithbean_recived_multiple_of_3_return_rice(self):
        entries = (3, 6, 9, 12, 18, 21)
        out = 'Rice'
        
        for entrie in entries:
            with self.subTest(entrie=entrie, out=out):
                self.assertEqual(
                    rice_with_bean(entrie), out,
                    msg=f'"{entrie}" didnt return "{out}"'
                    )
                

    def test_ricewithbean_recived_multiple_of_5_return_bean(self):
        entries = (5, 10, 25, 35, 40, 50)
        out = 'Bean'
        
        for entrie in entries:
            with self.subTest(entrie=entrie, out=out):
                self.assertEqual(
                    rice_with_bean(entrie), out,
                    msg=f'"{entrie}" didnt return "{out}"'
                    )
    

    def test_ricewithbean_not_recived_multiple_of_3_and_5_return_starve(self):
        entries = (1, 2, 4, 7, 8)
        out = 'Starve'
        
        for entrie in entries:
            with self.subTest(entrie=entrie, out=out):
                self.assertEqual(
                    rice_with_bean(entrie), out,
                    msg=f'"{entrie}" didnt return "{out}"'
                    )
                
 
if __name__ == '__main__':
    unittest.main(verbosity=2)