
# Shopping Cart Project

Proyek ini adalah aplikasi web sederhana yang berfungsi sebagai simulasi keranjang belanja. Aplikasi ini memungkinkan pengguna untuk menambahkan, menghapus, dan melihat item dalam keranjang mereka serta menghitung total belanja secara dinamis. Proyek ini dikembangkan dengan pendekatan kolaboratif menggunakan Python dan Flask sebagai backend serta HTML dan CSS untuk frontend.

## Teknologi yang Digunakan
- **Python**: Bahasa pemrograman utama untuk backend.
- **Flask**: Framework web minimalis untuk menangani logika server.
- **HTML & CSS**: Untuk tampilan frontend yang responsif.
- **Bootstrap**: Untuk gaya antarmuka yang lebih baik.
- **JavaScript**: Untuk fitur dinamis seperti perhitungan total.

## Fitur Utama
1. **Tambah Item ke Keranjang**: Pengguna dapat menambahkan produk ke dalam keranjang dengan nama, jumlah, dan harga.
2. **Hapus Item**: Item tertentu dapat dihapus dari keranjang belanja.
3. **Perhitungan Total Otomatis**: Total harga diperbarui setiap kali ada perubahan dalam keranjang.
4. **Checkout**: Menyelesaikan proses pembelian dengan meringkas total belanja.
5. **Desain Responsif**: Aplikasi dapat diakses dengan baik di berbagai perangkat, termasuk desktop dan mobile.

## Instalasi
Ikuti langkah-langkah berikut untuk menjalankan aplikasi di lingkungan lokal:

1. **Clone repositori ini**:
   ```bash
   git clone https://github.com/username/shopping_cart_project.git
   ```
2. **Pindah ke direktori proyek**:
   ```bash
   cd shopping_cart_project
   ```
3. **Buat virtual environment dan aktifkan**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate   # Windows
   ```
4. **Instal semua dependensi**:
   ```bash
   pip install -r requirements.txt
   ```

## Menjalankan Aplikasi
1. Jalankan server aplikasi:
   ```bash
   python app.py
   ```
2. Buka browser dan akses: [http://localhost:5000](http://localhost:5000)

## API Endpoint Utama
Berikut adalah daftar endpoint utama yang tersedia di aplikasi ini:
1. **`/` (GET)**: Menampilkan halaman utama keranjang belanja.
2. **`/add` (POST)**: Menambahkan item ke keranjang belanja.
3. **`/remove` (POST)**: Menghapus item tertentu dari keranjang.
4. **`/checkout` (GET)**: Menampilkan ringkasan belanja pengguna.

### Contoh Request `POST /add`
```python
import requests

url = "http://localhost:5000/add"
data = {"item_name": "Buku", "quantity": 2, "price": 50000}
response = requests.post(url, data=data)
print(response.text)
```

## Struktur Proyek
```
shopping_cart_project/
│
├── app.py              # Logika backend utama
├── requirements.txt    # Daftar dependensi Python
├── static/             # File statis (CSS, JS, gambar)
│   └── style.css       # Gaya utama aplikasi
├── templates/          # Template HTML
│   └── index.html      # Halaman utama aplikasi
└── README.md           # Dokumentasi proyek
```


