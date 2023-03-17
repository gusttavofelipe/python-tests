import unittest
from unittest.mock import patch
from people import People   


class TestPeople(unittest.TestCase):
    def setUp(self):
        self.p1 = People('Gustavo', 'Silva')
        self.p2 = People('Felipe', 'Costa')

    # setUp é chamado imediatamente após chamar o método de teste
    # logo: self.p1 é instanciado logo após o inicio de cada teste   
    

    def test_people_attr_name_has_a_correct_value(self):
        self.assertEqual(self.p1.name, 'Gustavo')
        self.assertEqual(self.p2.name, 'Felipe')
    

    def test_people_attr_name_is_str(self):
        self.assertIsInstance(self.p1.name, str)
        self.assertIsInstance(self.p2.name, str)


    def test_people_attr_last_name_has_a_correct_value(self):
        self.assertEqual(self.p1.last_name, 'Silva')
        self.assertEqual(self.p2.last_name, 'Costa')


    def test_people_attr_last_name_is_str(self):
        self.assertIsInstance(self.p1.last_name, str)
        self.assertIsInstance(self.p2.last_name, str)


    def test_people_attr_received_data_starts_false(self):
        self.assertFalse(self.p1.received_data)
        self.assertFalse(self.p2.received_data)

    
    def test_get_all_data_sucsses_ok(self):
        with patch('requests.get') as fake_request: # simulando get em uma API
            fake_request.return_value.ok = True # criando atributo para obter retorno da condicao

            self.assertEqual(self.p1.get_all_data(), 'CONECTADO')
            self.assertTrue(self.p1.received_data) # self.assertTrue checa se o parametro é True

            self.assertEqual(self.p2.get_all_data(), 'CONECTADO')
            self.assertTrue(self.p2.received_data) 
    
    def test_get_all_data_fail_404(self):
        with patch('requests.get') as fake_request: 
            fake_request.return_value.ok = False 

            self.assertEqual(self.p1.get_all_data(), 'ERROR 404')
            self.assertFalse(self.p1.received_data) # self.assertFalse checa se o parametro é False

            self.assertEqual(self.p2.get_all_data(), 'ERROR 404')
            self.assertFalse(self.p2.received_data) 
    

    def test_get_all_data_sucsses_and_fail_sequential(self):
        with patch('requests.get') as fake_request: 
            fake_request.return_value.ok = True

            self.assertEqual(self.p1.get_all_data(), 'CONECTADO')
            self.assertTrue(self.p1.received_data) 
            
            self.assertEqual(self.p2.get_all_data(), 'CONECTADO')
            self.assertTrue(self.p2.received_data) 

            fake_request.return_value.ok = False 

            self.assertEqual(self.p1.get_all_data(), 'ERROR 404')
            self.assertFalse(self.p1.received_data)

            self.assertEqual(self.p2.get_all_data(), 'ERROR 404')
            self.assertFalse(self.p2.received_data)


if __name__ == '__main__':
    unittest.main(verbosity=2)