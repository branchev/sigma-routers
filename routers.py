import os
import requests

WAREHOUSE_URL = os.getenv('WAREHOUSE_URL')
print(WAREHOUSE_URL)

class SigmaEndpoints():

    def login(self, email: str, password: str):
        return requests.post(
            f'{WAREHOUSE_URL}/api-token-auth/',
            data={'email': email, 'password': password}
        )

    def get_items(self, jwt_token: str):
        """
        GET all items
        """
        return requests.get(
            f'{WAREHOUSE_URL}/api/warehouse/items/',
            headers={'Authorization': f'Token {jwt_token}'}
        )

    def buy_item(self, jwt_token: str, item_id: int, quantity: int):
        """
        POST buy item
        """
        return requests.post(
            f'{WAREHOUSE_URL}/api/warehouse/items/',
            data={'item_id': item_id, 'quantity': quantity},
            headers={'Authorization': f'Token {jwt_token}'}
        )
