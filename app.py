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



app = Flask(__name__)
app.json_encoder = CustomJSONEncoder
CORS(app, resources={
    r"/*": {
        "origins": "*",
        "methods": ["GET", "POST", "PUT", "DELETE"],
        "allow_headers": ["Content-Type", "X-API-Key"]
    }
})
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

# API untuk mengambil produk
class ProductAPI:
    def __init__(self, server_ip, api_key):
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

# Route untuk halaman utama
@app.route('/')
def index():
    product_api = ProductAPI(server_ip='192.168.0.110', api_key='44c64a2dd91188892dc7a07bf7d671025be04747f9c3fcac28b1c0f7894a8321')
    products = product_api.get_products()

    cart = session.get('cart', [])
    total_price = sum(item['price'] * item['quantity'] for item in cart)

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
    product_api = ProductAPI(server_ip='192.168.0.110', api_key='44c64a2dd91188892dc7a07bf7d671025be04747f9c3fcac28b1c0f7894a8321')
    products = product_api.get_products()

    product = next((p for p in products.get('products', []) if p['id'] == product_id), None)

    if product:
        cart = session.get('cart', [])
        item = next((i for i in cart if i['id'] == product_id), None)

        if item:
            item['quantity'] += 1
        else:
            cart.append({'id': product_id, 'name': product['name'], 'price': product['price'], 'quantity': 1})

        session['cart'] = cart
    return redirect(url_for('index'))

# Route untuk mengupdate jumlah produk dalam keranjang
@app.route('/update_quantity/<int:product_id>', methods=['POST'])
def update_quantity(product_id):
    new_quantity = int(request.form['quantity'])
    if new_quantity < 1:
        return redirect(url_for('index'))
    
    cart = session.get('cart', [])
    item = next((i for i in cart if i['id'] == product_id), None)

    if item:
        item['quantity'] = new_quantity
        session['cart'] = cart
    return redirect(url_for('index'))

# Route untuk menghapus produk dari keranjang
@app.route('/remove_from_cart/<int:product_id>', methods=['POST'])
def remove_from_cart(product_id):
    cart = session.get('cart', [])
    cart = [item for item in cart if item['id'] != product_id]

    session['cart'] = cart
    return redirect(url_for('index'))

# Route untuk halaman Checkout
@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        cart = session.get('cart', [])
        total_price = sum(item['price'] * item['quantity'] for item in cart)

        # Kirim data ke API checkout untuk menyimpan transaksi
        response = requests.post('http://localhost:5000/api/checkout', json={'total_price': total_price})
        
        if response.status_code == 201:
            session['cart'] = []  # Bersihkan keranjang setelah checkout berhasil
            return redirect(url_for('index'))  # Redirect kembali ke halaman utama setelah transaksi berhasil
        else:
            return jsonify({'error': 'Checkout failed'}), 500

    return render_template('index.html')

# Route untuk API Checkout yang digunakan oleh perangkat lain

# Route untuk API yang menampilkan seluruh transaksi dalam format JSON
@app.route('/api/transactions', methods=['GET'])
def api_get_transactions():
    # Koneksi ke database
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    # Menjalankan query untuk mengambil semua transaksi
    cursor.execute("SELECT * FROM transactions")
    transactions = cursor.fetchall()
    
    # Menutup koneksi
    cursor.close()
    connection.close()
    
    # Mengembalikan data transaksi dalam format JSON
    return jsonify(transactions)



@app.route('/api/checkout', methods=['POST'])
def api_checkout():
    data = request.json
    total_price = data.get('total_price')
    

    if not total_price:
        return jsonify({'error': 'Total price is required'}), 400

    # Menyimpan transaksi ke database
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO transactions (total_price) VALUES (%s)", (total_price,))
    connection.commit()
    cursor.close()
    connection.close()

    # Membuat response JSON yang menunjukkan status transaksi
    return jsonify({
        'message': 'Transaction successful',
        'transaction': {
            'total_price': total_price,
            'status': 'completed'
        }
    }), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
