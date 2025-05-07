import tkinter as tk
from tkinter import messagebox
from functions import hitung_total

window = tk.Tk()
window.title("CMI Kasir")
window.geometry("320x240")

# Layout dan Input
tk.Label(window, text="Nama Produk").grid(row=0, column=0, padx=10, pady=5)
produk_entry = tk.Entry(window)
produk_entry.grid(row=0, column=1)

tk.Label(window, text="Harga (Rp)").grid(row=1, column=0, padx=10, pady=5)
harga_entry = tk.Entry(window)
harga_entry.grid(row=1, column=1)

tk.Label(window, text="Jumlah").grid(row=2, column=0, padx=10, pady=5)
jumlah_entry = tk.Entry(window)
jumlah_entry.grid(row=2, column=1)

# Output
hasil_label = tk.Label(window, text="Total: -")
hasil_label.grid(row=4, column=0, columnspan=2, pady=10)

# Proses

def hitung():
    harga = harga_entry.get()
    jumlah = jumlah_entry.get()
    total = hitung_total(harga, jumlah)
    if total == 0:
        messagebox.showerror("Error", "Input tidak valid!")
    else:
        produk = produk_entry.get()
        hasil_label.config(text=f"Pesanan: {produk}\nTotal: Rp {total:,.2f}")

# Tombol
btn = tk.Button(window, text="Hitung Pembayaran", command=hitung)
btn.grid(row=3, column=0, columnspan=2, pady=10)

window.mainloop()
