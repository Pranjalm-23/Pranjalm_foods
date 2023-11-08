# src/routes/auth.py

import re
from flask import Blueprint, request, jsonify
import logging

auth_bp = Blueprint('auth', __name__)

dummy_username = 'pkm'
dummy_password = '1234'
dummy_phone_number = '9999999999'  # Example dummy phone number for testing

@auth_bp.route('/login', methods=['POST'])
def login_user():
    try:
        data = request.get_json()
        identifier = data.get('identifier')  # This can be either the username or the phone number
        password = data.get('password')

        if re.match(r'^[6-9]\d{9}$', identifier):  # Check if the input is a valid 10-digit Indian phone number
            # Your logic for handling phone number authentication
            if password == dummy_password:
                logging.info(f'User with phone number {identifier} logged in successfully')
                return jsonify({'message': 'Logged in successfully', 'user_identifier': identifier}), 200
            else:
                logging.warning(f'Invalid credentials for user with phone number {identifier}')
                return jsonify({'message': 'Invalid credentials'}), 401
        else:
            # Your logic for handling username authentication
            if identifier == dummy_username and password == dummy_password:
                logging.info(f'User with username {identifier} logged in successfully')
                return jsonify({'message': 'Logged in successfully', 'user_identifier': identifier}), 200
            else:
                logging.warning(f'Invalid credentials for user with username {identifier}')
                return jsonify({'message': 'Invalid credentials'}), 401
    except Exception as e:
        logging.error(f'An error occurred: {e}')
        return jsonify({'message': 'An error occurred'}), 500

