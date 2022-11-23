from accessor.shopping_accessor import ShoppingAccessor
from model.item import item_status
from flask import Flask, request, jsonify
import datetime
import requests
import json

app = Flask(__name__)
shopping_accessor = ShoppingAccessor()


@app.route('/')
def home():
    return "shopping service home page"

# CreateItemForSale
@app.route('/create_item/<user_id>', methods=['POST'])
def create_item(user_id):
    data = request.get_data()
    data = json.loads(data)
    # call inventory service
    r = requests.post("http://10.1.1.1:5000/create_item", data=data)
    # get item_id from response
    item_id = r.data
    shopping_accessor.add_user_item(user_id=user_id, item_id=item_id)


# AddItemToCart
@app.route('/add_item_to_cart/<user_id>/<item_id>', methods=['PUT'])
def add_item_to_cart(user_id, item_id):
    cart_id = shopping_accessor.get_current_cart(user_id=user_id)
    shopping_accessor.add_item_to_cart(cart_id=cart_id, item_id=item_id)


# CheckoutItem
@app.route('/checkout/<user_id>', methods=['PUT'])
def checkout(user_id):
    cart_id = shopping_accessor.get_current_cart(user_id=user_id)
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    shopping_accessor.checkout_items(cart_id, current_time)


# GetItemsInCartByUser
@app.route('/get_items_in_cart/<user_id>', method=['PUT'])
def get_items_in_cart(user_id):


# RemoveItemFromCart
@app.route('/remove_item_from_cart/<user_id>', method=['DELETE'])
def remove_item_from_cart(user_id):


# RemoveItemForSale
@app.route('/remove_item_for_sale/<user_id>/<item_id>', method=['DELETE'])
def remove_item_for_sale(user_id, item_id):


# UpdateItemForSale
@app.route('/update_item_for_sale', method=['POST'])
def update_item_for_sale():


# GetItemsForSaleByOwner
@app.route('/get_items_for_sale/<user_id>', method=['GET'])
def get_items_for_sale(user_id):


# GetItemsByCategory
@app.route('/get_items_by_category', methods=['GET'])
def get_items_by_category():


@app.route('/get_all_categories', methods=['GET'])
def get_all_categories():