import tkinter as tk

# === Functions ===

def aksi_tombol():
    label_info.config(text="iyahh okh")

def ubah_judul():
    new_title = entry_judul.get()
    if new_title:
        window.title(new_title)

def keluar():
    window.destroy()

def hitung_total(harga, jumlah, diskon):
    try:
        total = float(harga) * int(jumlah)
        if diskon:
            total_diskon = total - (total * float(diskon) / 100)
            return total, total_diskon
        return total, total
    except ValueError:
        return 0, 0

def proses():
    harga = harga_entry.get()
    jumlah = jumlah_entry.get()
    diskon = diskon_entry.get()
    total, total_setelah_diskon = hitung_total(harga, jumlah, diskon)
    hasil_label.config(
        text=f"Total Sebelum Diskon:\nRp {total:,.2f}\n\nTotal Setelah Diskon:\nRp {total_setelah_diskon:,.2f}"
    )

# === Window Setup ===

window = tk.Tk()
window.title("CMI Coffee - Kasir")
window.geometry("430x630")
window.configure(bg="#f6f7fb")  # Warna latar lembut

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

# === Header ===
label_header = tk.Label(window, text="☕ CMI Coffee Kasir App", font=("Poppins", 16, "bold"), bg="#f6f7fb", fg="#333")
label_header.grid(row=0, column=0, columnspan=2, pady=(25, 5))

label_info = tk.Label(window, text="Selamat datang di sistem kasir kami", font=("Poppins", 9), bg="#f6f7fb", fg="#666")
label_info.grid(row=1, column=0, columnspan=2, pady=(0, 10))

# === Tombol Aksi Atas ===
btn_aksi = tk.Button(window, text="Lanjutin web HMPBD woy", font=("Poppins", 10, "bold"),
                     bg="#ffb347", fg="#000", command=aksi_tombol, relief="flat", padx=10, pady=5)
btn_aksi.grid(row=2, column=0, columnspan=2, pady=5, ipadx=5, sticky="we", padx=50)

# === Entry Ubah Judul ===
entry_judul = tk.Entry(window, font=("Poppins", 10), bg="white", relief="solid", bd=1)
entry_judul.grid(row=3, column=0, columnspan=2, padx=50, pady=5, ipadx=5, ipady=5, sticky="we")

btn_judul = tk.Button(window, text="Ubah Judul", font=("Poppins", 10, "bold"),
                      bg="#6c63ff", fg="white", command=ubah_judul, relief="flat")
btn_judul.grid(row=4, column=0, columnspan=2, pady=5, ipadx=5, ipady=2)

# === Input Form ===
tk.Label(window, text="Nama Produk:", bg="#f6f7fb", font=("Poppins", 10), anchor="w").grid(row=5, column=0, sticky="e", padx=10, pady=5)
produk_entry = tk.Entry(window, width=25, font=("Poppins", 10), bg="white", relief="solid", bd=1)
produk_entry.grid(row=5, column=1, sticky="w", padx=10, pady=5)

tk.Label(window, text="Harga:", bg="#f6f7fb", font=("Poppins", 10), anchor="w").grid(row=6, column=0, sticky="e", padx=10, pady=5)
harga_entry = tk.Entry(window, width=25, font=("Poppins", 10), bg="white", relief="solid", bd=1)
harga_entry.grid(row=6, column=1, sticky="w", padx=10, pady=5)

tk.Label(window, text="Jumlah:", bg="#f6f7fb", font=("Poppins", 10), anchor="w").grid(row=7, column=0, sticky="e", padx=10, pady=5)
jumlah_entry = tk.Entry(window, width=25, font=("Poppins", 10), bg="white", relief="solid", bd=1)
jumlah_entry.grid(row=7, column=1, sticky="w", padx=10, pady=5)

tk.Label(window, text="Diskon (%):", bg="#f6f7fb", font=("Poppins", 10), anchor="w").grid(row=8, column=0, sticky="e", padx=10, pady=5)
diskon_entry = tk.Entry(window, width=25, font=("Poppins", 10), bg="white", relief="solid", bd=1)
diskon_entry.grid(row=8, column=1, sticky="w", padx=10, pady=5)

# === Tombol Proses ===
btn_proses = tk.Button(window, text="💰 Hitung Total", font=("Poppins", 11, "bold"),
                       bg="#4CAF50", fg="white", command=proses, relief="flat")
btn_proses.grid(row=9, column=0, columnspan=2, pady=10, ipadx=10, ipady=5)

# === Output Total ===
hasil_label = tk.Label(window, text="Total:", bg="#f6f7fb", font=("Poppins", 11), fg="#333", justify="center")
hasil_label.grid(row=10, column=0, columnspan=2, pady=10)

# === Tombol Keluar ===
btn_keluar = tk.Button(window, text="🚪 Keluar", font=("Poppins", 11, "bold"),
                       bg="#e74c3c", fg="white", command=keluar, relief="flat")
btn_keluar.grid(row=11, column=0, columnspan=2, pady=(10, 30), ipadx=10, ipady=3)

window.mainloop()
