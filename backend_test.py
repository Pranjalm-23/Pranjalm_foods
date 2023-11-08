# import requests

# # Define the API endpoint
# url = 'http://127.0.0.1:5000/login'

# # Define the request payload with the phone number and password
# payload1 = {
#     'identifier': '9999999999',  # Replace with your dummy phone number
#     'password': '1234'  # Replace with your password
# }

# # Define the request payload with the username and password
# payload2 = {
#     'identifier': 'pkm',  # Replace with your dummy username
#     'password': '1234'  # Replace with your password
# }

# # Send the POST request to the API endpoint
# response = requests.post(url, json=payload1)

# # Print the response
# print("Login using phone number"+"\n",response.json())


# response = requests.post(url, json=payload2)
# print("Login using username"+"\n",response.json())



# # test to fetch list of available food vendor's / restaurants
# # Define the API endpoint
# url = 'http://127.0.0.1:5000/vendor'

# # Send the GET request to the API endpoint
# response = requests.get(url)

# # Print the response
# print(response.json()) 



# # test to fetch menu of a specific vendor /menu/<vendor_id>
# Define the API endpoint with the vendor ID
# import requests
# vendor_id = 'vendor_id_1'  # Replace with the desired vendor ID
# url = f'http://127.0.0.1:5000/menu/{vendor_id}'

# # Send the GET request to the API endpoint
# response = requests.get(url)

# # Print the response
# print(response.json())



# test to add items to the cart order
import requests

# Define the API endpoint and the request payload for creating an order
url_create_order = 'http://127.0.0.1:5000/order'
payload_create_order = {
    'user_id': '12345',  # Replace with the desired user ID
    'vendor_id': 'vendor_id_1',  # Replace with the desired vendor ID
    'menu_items': ['Dish A', 'Dish B']  # Replace with the desired menu items
}

# Send the POST request to the create order endpoint
response_create_order = requests.post(url_create_order, json=payload_create_order)

# Print the response
print(response_create_order.json())


# Define the API endpoint and the request payload for confirming the order
url_confirm_order = 'http://127.0.0.1:5000/order/12345/confirm'  # Replace '12345' with the actual order ID
payload_confirm_order = {
    'shipping_address': '123 Street, City, State, Country',  # Replace with the desired shipping address
    'billing_data': {'card_number': '**** **** **** 1234', 'expiry_date': '12/25'}  # Replace with the billing data
}

# Send the POST request to the confirm order endpoint
response_confirm_order = requests.post(url_confirm_order, json=payload_confirm_order)

# Print the response
print(response_confirm_order.json())




