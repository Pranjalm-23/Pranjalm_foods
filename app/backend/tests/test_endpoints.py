# tests/test_endpoints.py

import unittest
import requests

class TestEndpoints(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://127.0.0.1:5000'

        self.order_payload = {
            'user_id': '12345',
            'vendor_id': 'vendor_id_1',
            'menu_items': ['Dish A', 'Dish B']
        }
        self.confirm_payload = {
            'shipping_address': '123 Street, City, State, Country',
            'billing_data': {'card_number': '**** **** **** 1234', 'expiry_date': '12/25'}
        }

    def test_get_vendors(self):
        response = requests.get(f'{self.base_url}/vendors')
        self.assertEqual(response.status_code, 200)

    def test_get_menu(self):
        vendor_id = 'vendor_id_1'  # Replace with the desired vendor ID
        response = requests.get(f'{self.base_url}/menu/{vendor_id}')
        self.assertEqual(response.status_code, 200)

    def test_create_order(self):
        url_create_order = f'{self.base_url}/order'
        response_create_order = requests.post(url_create_order, json=self.order_payload)
        self.assertEqual(response_create_order.status_code, 200)

    def test_confirm_order(self):
        order_id = '12345'  # Replace with the actual order ID
        url_confirm_order = f'{self.base_url}/order/{order_id}/confirm'
        response_confirm_order = requests.post(url_confirm_order, json=self.confirm_payload)
        self.assertEqual(response_confirm_order.status_code, 200)

if __name__ == '__main__':
    unittest.main()
