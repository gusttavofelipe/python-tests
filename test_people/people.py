import requests

class People:
    def __init__(self, name, last_name):
        self.name =  name
        self.last_name =  last_name
        self.received_data = False


    def get_all_data(self): # consulta falsa
        response = requests.get('https://docs.python.org/pt-br/3/library/unittest.html')

        if response.ok:
            self.received_data = True
            return 'CONECTADO'
        else:
            self.received_data = False
            return 'ERROR 404'
        