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


import unittest
from calculator import calc_sum


# a classe deve conter a palavra "Test;"
# a funcao deve começar com "test" e o nome ser autoexplicativo;

class TestCalculator(unittest.TestCase):
    def test_sum_5_and_5_should_return_10(self):
        self.assertEqual(calc_sum(5, 5), 10.0) # assertEqual(a, b) checa se a == b   
    

    def test_sum_negative_5_and_5_should_return_0(self):
        self.assertEqual(calc_sum(-5, 5), 0.0)


    def test_sum_multiple_entries(self):
        x_y_outs = (
            (10, 10, 20.0),
            (0, 10, 10.0),
            (-15, 10, -5.0),    
            (3.33, 6.66, 9.99),
        )

        for x_y_out in x_y_outs:
            with self.subTest(x_y_out=x_y_out): # self.SubTest executa como um subteste
                x, y, out = x_y_out
                self.assertEqual(calc_sum(x, y), out)

        # self.SubTest retorna msg e params, valores 
        # opcionais que são exibidos sempre que um subteste falha


    def test_sum_y_not_int_and_not_float_return_assertionerror(self):
        with self.assertRaises(AssertionError):
            calc_sum('1', 1)

    
    def test_sum_x_not_int_and_not_float_return_assertionerror(self):
        with self.assertRaises(AssertionError):
            self.assertRaises(AssertionError, calc_sum(1, '1'))

    # testa se uma exceção é gerada quando callable é chamado
    

if __name__ == '__main__':
    unittest.main(verbosity=2)