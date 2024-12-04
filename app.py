from flask import Flask, render_template, request, redirect, url_for, jsonify, session
import mysql.connector
import requests
import json
from flask_cors import CORS
import logging
import secrets
from functools import wraps
from werkzeug.exceptions import BadRequest
import os
from dotenv import load_dotenv
from flask_cors import CORS
from datetime import datetime

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)
# Fungsi untuk koneksi ke database
app.secret_key = 'your_secret_key'

# Konfigurasi database MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_DATABASE'] = 'shopping_cart_db'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''

# Fungsi untuk koneksi ke database
def get_db_connection():
    connection = mysql.connector.connect(
        host=app.config['MYSQL_HOST'],
        database=app.config['MYSQL_DATABASE'],
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD']
    )
    return connection

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)



app = Flask(name)
app.json_encoder = CustomJSONEncoder
CORS(app, resources={
    r"/*": {
        "origins": "*",
        "methods": ["GET", "POST", "PUT", "DELETE"],
        "allow_headers": ["Content-Type", "X-API-Key"]
    }
})

            return response.json() if response.status_code == 200 else {'error': 'Unable to fetch products'}
        except requests.exceptions.RequestException as e:
            return {'error': f'Connection error: {str(e)}'}

# Route untuk halaman utama
@app.route('/')
def index():
   # API untuk mengambil produk
class ProductAPI:
    def init(self, server_ip, api_key):
        self.base_url = f'http://{server_ip}:5000'
        self.headers = {
            'Content-Type': 'application/json',
            'X-API-Key': api_key
        }

    def get_products(self):
        try:
            response = requests.get(
                f'{self.base_url}/api/products',
                headers=self.headers
            )
            return response.json() if response.status_code == 200 else {'error': 'Unable to fetch products'}
        except requests.exceptions.RequestException as e:
            return {'error': f'Connection error: {str(e)}'}
    # Mengambil data keranjang dari session
    cart = session.get('cart', [])
    total_price = sum(item['price'] * item['quantity'] for item in cart)

    # Menampilkan data transaksi yang ada di database
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM transactions")
    transactions = cursor.fetchall()
    cursor.close()
    connection.close()

    return render_template('index.html', products=products.get('products', []), cart=cart, total_price=total_price, transactions=transactions)

# Route untuk menambah produk ke keranjang
@app.route('/add_to_cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    # Mengambil data produk dari API
    product_api = ProductAPI(server_ip='192.168.0.110', api_key='44c64a2dd91188892dc7a07bf7d671025be04747f9c3fcac28b1c0f7894a8321')
    products = product_api.get_products()

    product = next((p for p in products.get('products', []) if p['id'] == product_id), None)
    
app.secret_key = 'your_secret_key'

# Konfigurasi database MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_DATABASE'] = 'shopping_cart_db'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''

# Fungsi untuk koneksi ke database
def get_db_connection():
    connection = mysql.connector.connect(
        host=app.config['MYSQL_HOST'],
        database=app.config['MYSQL_DATABASE'],
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD']
    )
    return connection


# Route untuk menghapus produk dari keranjang
@app.route('/remove_from_cart/<int:product_id>', methods=['POST'])
def remove_from_cart(product_id):
    cart = session.get('cart', [])
    cart = [item for item in cart if item['id'] != product_id]

    session['cart'] = cart
    return redirect(url_for('index'))



        session['cart'] = cart
    return redirect(url_for('index'))

# Route untuk mengupdate jumlah produk dalam keranjang
return render_template('index.html', products=products.get('products', []), cart=cart, total_price=total_price, transactions=transactions)

# Route untuk menambah produk ke keranjang
@app.route('/add_to_cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    product_api = ProductAPI(server_ip='192.168.0.110', api_key='44c64a2dd91188892dc7a07bf7d671025be04747f9c3fcac28b1c0f7894a8321')
    products = product_api.get_products()

    product = next((p for p in products.get('products', []) if p['id'] == product_id), None)

    if product:
        cart = session.get('cart', [])
        item = next((i for i in cart if i['id'] == product_id), None)


aku
# Route untuk menghapus produk dari keranjang
@app.route('/remove_from_cart/<int:product_id>', methods=['POST'])
def remove_from_cart(product_id):
    # Ambil keranjang dari session
    cart = session.get('cart', [])
    cart = [item for item in cart if item['id'] != product_id]
# Membuat response JSON yang menunjukkan status transaksi
    return jsonify({
        'message': 'Transaction successful',
        'transaction': {
            'total_price': total_price,
            'status': 'completed'
        }
    }), 201

return render_template('index.html', products=products.get('products', []), cart=cart, total_price=total_price, transactions=transactions)

# Route untuk menambah produk ke keranjang
@app.route('/add_to_cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    product_api = ProductAPI(server_ip='192.168.0.110', api_key='44c64a2dd91188892dc7a07bf7d671025be04747f9c3fcac28b1c0f7894a8321')
    products = product_api.get_products()

    product = next((p for p in products.get('products', []) if p['id'] == product_id), None)

    if product:
        cart = session.get('cart', [])
        item = next((i for i in cart if i['id'] == product_id), None)


aku

if name == 'main':
    app.run(host='0.0.0.0', port=5000, debug=True)



