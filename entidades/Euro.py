import requests

from entidades.Moneda import Moneda


class Euro(Moneda):
    def obtener_valor_moneda(self):
        response = requests.get("https://csrng.net/csrng/csrng.php?min=3500&max=4500")
        return float(response.json().pop().get('random') + 200)
