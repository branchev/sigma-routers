import requests


class SigmaEndpoints():

    def __init__(self, warehouse_url) -> None:
        self.warehouse_url = warehouse_url

    def login(self, email: str, password: str):
        return requests.post(
            f'{self.warehouse_url}/api-token-auth/',
            data={'email': email, 'password': password}
        )

    def get_items(self, jwt_token: str):
        """
        GET all items
        """
        return requests.get(
            f'{self.warehouse_url}/api/warehouse/items/',
            headers={'Authorization': f'Token {jwt_token}'}
        )

    def buy_item(self, jwt_token: str, item_id: int, quantity: int):
        """
        POST buy item
        """
        return requests.post(
            f'{self.warehouse_url}/api/buy-item/',
            data={'item_id': item_id, 'quantity': quantity},
            headers={'Authorization': f'Token {jwt_token}'}
        )
