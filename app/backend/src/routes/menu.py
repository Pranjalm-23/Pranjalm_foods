# src/routes/menu.py

import logging
from flask import Blueprint, jsonify, request

menu_bp = Blueprint('menu', __name__)

# Dummy menu for the selected vendor
dummy_menu = {
    'vendor_id_1': [
        {
            'id': 1,
            'name': 'Dish A',
            'available': True,
            'price': 10.99,
            'rating': 4.5
        },
        {
            'id': 2,
            'name': 'Dish B',
            'available': False,
            'price': 8.99,
            'rating': 4.0
        },
        # Add more menu items as needed
    ],
    'vendor_id_2': [
        {
            'id': 1,
            'name': 'Item A',
            'available': True,
            'price': 5.99,
            'rating': 4.2
        },
        {
            'id': 2,
            'name': 'Item B',
            'available': True,
            'price': 7.99,
            'rating': 4.7
        },
        # Add more menu items as needed
    ]
}

@menu_bp.route('/menu/<vendor_id>', methods=['GET'])
def get_menu(vendor_id):
    try:
        if vendor_id in dummy_menu:
            logging.info(f'Fetching the menu for vendor with ID {vendor_id}.')
            return jsonify({'menu': dummy_menu[vendor_id]}), 200
        else:
            logging.warning(f'No menu found for vendor with ID {vendor_id}.')
            return jsonify({'message': 'No menu found for the specified vendor ID'}), 404
    except Exception as e:
        logging.error(f'An error occurred while fetching the menu: {e}')
        return jsonify({'message': 'An error occurred while fetching the menu'}), 500

@menu_bp.route('/order', methods=['POST'])
def create_order():
    try:
        data = request.get_json()
        user_id = data.get('user_id')
        vendor_id = data.get('vendor_id')
        menu_items = data.get('menu_items')

        logging.info(f'Creating an order for user {user_id} at vendor {vendor_id} with menu items {menu_items}.')

        # TODO: Save the order details to the database and generate an order ID

        order_id = '12345'  # Replace with the generated order ID

        logging.info(f'Order created by user {user_id} at vendor {vendor_id}. Order ID: {order_id}.')
        return jsonify({'order_id': order_id}), 200
    except Exception as e:
        logging.error(f'An error occurred while creating the order: {e}')
        return jsonify({'message': 'An error occurred while creating the order'}), 500

@menu_bp.route('/order/<order_id>/confirm', methods=['POST'])
def confirm_order(order_id):
    try:
        data = request.get_json()
        shipping_address = data.get('shipping_address')
        billing_data = data.get('billing_data')

        # TODO: Implement the payment handling logic

        logging.info(f'Order {order_id} confirmed. Shipping address: {shipping_address}. Payment details received.')
        return jsonify({'message': 'Order confirmed successfully'}), 200
    except Exception as e:
        logging.error(f'An error occurred while confirming the order: {e}')
        return jsonify({'message': 'An error occurred while confirming the order'}), 500