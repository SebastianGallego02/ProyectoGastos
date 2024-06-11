import time

import requests

from entidades.Moneda import Moneda

link_API: str = "https://csrng.net/csrng/csrng.php?min=3500&max=4500"

class Dollar(Moneda):
    def obtener_valor_moneda(self):
        try:
            response = requests.get(link_API)
            return float(response.json().pop().get('random'))
        except TypeError:
            try:
                time.sleep(1)
                response = requests.get(link_API)
                return float(response.json().pop().get('random'))
            except TypeError:
                time.sleep(1)
                response = requests.get(link_API)
                return float(response.json().pop().get('random'))
