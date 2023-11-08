# src/routes/vendor.py

import logging
from flask import Blueprint, jsonify

vendor_bp = Blueprint('vendor', __name__)

# Dummy list of available vendors
available_vendors = [
    {
        'id': 1,
        'name': 'Vendor A',
        'description': 'A popular vendor offering various products.'
    },
    {
        'id': 2,
        'name': 'Vendor B',
        'description': 'An established vendor with a diverse selection.'
    },
    # Add more vendors as needed
]

@vendor_bp.route('/vendors', methods=['GET'])
def get_vendors():
    try:
        logging.info('Fetching the list of available vendors.')
        return jsonify({'vendors': available_vendors}), 200
    except Exception as e:
        logging.error(f'An error occurred while fetching the list of vendors: {e}')
        return jsonify({'message': 'An error occurred while fetching the list of vendors'}), 500
