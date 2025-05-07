import tkinter as tk

#ini functions anjayy

def aksi_tombol():
    label.config(text="iyahh okh")

def ubah_judul():
    new_title = entry_judul.get()
    if new_title:
        window.title(new_title)

def keluar():
    window.destroy()

def hitung_total(harga, jumlah):
    try:
        return float(harga) * int(jumlah)
    except ValueError:
        return 0

def proses():
    harga = harga_entry.get()
    jumlah = jumlah_entry.get()
    total = hitung_total(harga, jumlah)
    hasil_label.config(text=f"Total: Rp {total:,.2f}")

def on_enter(e):
    button.config(bg="#b8860b")

def on_leave(e):
    button.config(bg="#d2b48c", cursor="hand2")

#=== ini GUI nya iaa === ini GUI iaa ===

window = tk.Tk()
window.title("CoffeeShop GUI")
window.geometry("400x550")
window.configure(bg="#f5f5dc")

#Konfigurasi grid kolom biar lebarnya bagus
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

#Judul
label = tk.Label(window, text="Halo Iping Al Gaib\nSelamat Datang di CMI Coffee", bg="#f5f5dc", font=("Poppins", 14))
label.grid(row=0, column=0, columnspan=2, pady=(20, 10))

#Tombol Aksi
button = tk.Button(window, text="Lanjutin web hmpb woy", font=("Poppins", 12, "bold"), bg="#d2b48c", command=aksi_tombol)
button.bind("<Enter>", on_enter)
button.bind("<Leave>", on_leave)
button.grid(row=1, column=0, columnspan=2, pady=5, ipadx=10, ipady=3)

#Entry Judul
entry_judul = tk.Entry(window, width=30)
entry_judul.grid(row=2, column=0, columnspan=2, pady=5)

#Tombol Ubah Judul
button_judul = tk.Button(window, text="Ubah Judul", font=("Poppins", 12, "bold"), command=ubah_judul)
button_judul.grid(row=3, column=0, columnspan=2, pady=5, ipadx=10, ipady=3)

#Nama Produk
tk.Label(window, text="Nama Produk:", bg="#f5f5dc", anchor="e").grid(row=4, column=0, sticky="e", padx=10, pady=5)
produk_entry = tk.Entry(window, width=20)
produk_entry.grid(row=4, column=1, sticky="w", padx=10, pady=5)

#Harga
tk.Label(window, text="Harga:", bg="#f5f5dc", anchor="e").grid(row=5, column=0, sticky="e", padx=10, pady=5)
harga_entry = tk.Entry(window, width=20)
harga_entry.grid(row=5, column=1, sticky="w", padx=10, pady=5)

#Jumlah
tk.Label(window, text="Jumlah:", bg="#f5f5dc", anchor="e").grid(row=6, column=0, sticky="e", padx=10, pady=5)
jumlah_entry = tk.Entry(window, width=20)
jumlah_entry.grid(row=6, column=1, sticky="w", padx=10, pady=5)

# Tombol Hitung Total
proses_btn = tk.Button(window, text="Hitung Total", command=proses, bg="#4CAF50", fg="white", font=("Poppins", 12, "bold"))
proses_btn.grid(row=7, column=0, columnspan=2, pady=10, ipadx=10, ipady=3)

#Output Total
hasil_label = tk.Label(window, text="Total:", bg="#f5f5dc", font=("Poppins", 12))
hasil_label.grid(row=8, column=0, columnspan=2, pady=10)

#Tombol Keluar
button_keluar = tk.Button(window, text="Keluar", font=("Poppins", 12, "bold"), command=keluar)
button_keluar.grid(row=9, column=0, columnspan=2, pady=(10, 30), ipadx=10, ipady=3)

window.mainloop()
