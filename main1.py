import tkinter as tk
from functions import hitung_total

def proses():
    harga = harga_entry.get()
    jumlah = jumlah_entry.get()
    total = hitung_total(harga, jumlah)
    hasil_label.config(text=f"Total: Rp {total:,.2f}")

# Membuat jendela utama
window = tk.Tk()
window.title("Kasir CMI")
window.geometry("400x400")
window.configure(bg="#f5f5dc")

# Judul
tk.Label(window, text="Kasir CMI", font=("Poppins", 16, "bold"), bg="#f5f5dc").grid(row=0, column=0, columnspan=2, pady=10)

# Input
tk.Label(window, text="Nama Produk:", bg="#f5f5dc").grid(row=1, column=0, padx=10, pady=5, sticky="e")
produk_entry = tk.Entry(window)
produk_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(window, text="Harga:", bg="#f5f5dc").grid(row=2, column=0, padx=10, pady=5, sticky="e")
harga_entry = tk.Entry(window)
harga_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(window, text="Jumlah:", bg="#f5f5dc").grid(row=3, column=0, padx=10, pady=5, sticky="e")
jumlah_entry = tk.Entry(window)
jumlah_entry.grid(row=3, column=1, padx=10, pady=5)

# Output
hasil_label = tk.Label(window, text="Total: ", bg="#f5f5dc", font=("Poppins", 12))
hasil_label.grid(row=5, column=0, columnspan=2, pady=10)

# Tombol Hitung Total
proses_btn = tk.Button(window, text="Hitung Total", command=proses, bg="#4CAF50", fg="white", font=("Poppins", 12, "bold"))
proses_btn.grid(row=4, column=0, columnspan=2, pady=10)

# Menjalankan aplikasi
window.mainloop()
