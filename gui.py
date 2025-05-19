# INI GUI IAA
import tkinter as tk
import functions

def create_gui():
    window = tk.Tk()
    window.title("CMI COFFEE - Kasir")
    window.geometry("430x630")
    window.configure(bg="#f6f7fb")

    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=1)

    label_header = tk.Label(window, text="☕ CMI Coffee Kasir App", font=("Poppins", 16, "bold"), bg="#f6f7fb", fg="#333")
    label_header.grid(row=0, column=0, columnspan=2, pady=(25, 5))

    label_info = tk.Label(window, text="Selamat datang di sistem kasir kami", font=("Poppins", 9), bg="#f6f7fb", fg="#666")
    label_info.grid(row=1, column=0, columnspan=2, pady=(0, 10))

    btn_aksi = tk.Button(window, text="Coba klik", font=("Poppins", 10, "bold"),
                         bg="#ffb347", fg="#000", command=lambda: functions.aksi_tombol(label_info), relief="flat", padx=10, pady=5)
    btn_aksi.grid(row=2, column=0, columnspan=2, pady=5, ipadx=5, sticky="we", padx=50)

    entry_judul = tk.Entry(window, font=("Poppins", 10), bg="white", relief="solid", bd=1)
    entry_judul.grid(row=3, column=0, columnspan=2, padx=50, pady=5, ipadx=5, ipady=5, sticky="we")

    btn_judul = tk.Button(window, text="Ubah Judul", font=("Poppins", 10, "bold"),
                          bg="#6c63ff", fg="white", command=lambda: functions.ubah_judul(window, entry_judul), relief="flat")
    btn_judul.grid(row=4, column=0, columnspan=2, pady=5, ipadx=5, ipady=2)

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

    hasil_label = tk.Label(window, text="Total:", bg="#f6f7fb", font=("Poppins", 11), fg="#333", justify="center")
    hasil_label.grid(row=10, column=0, columnspan=2, pady=10)

    btn_proses = tk.Button(window, text="💰 Hitung Total", font=("Poppins", 11, "bold"),
                           bg="#4CAF50", fg="white", command=lambda: functions.proses(harga_entry, jumlah_entry, diskon_entry, hasil_label, functions.hitung_total), relief="flat")
    btn_proses.grid(row=9, column=0, columnspan=2, pady=10, ipadx=10, ipady=5)

    btn_keluar = tk.Button(window, text="🚪 Keluar", font=("Poppins", 11, "bold"),
                           bg="#e74c3c", fg="white", command=lambda: functions.keluar(window), relief="flat")
    btn_keluar.grid(row=11, column=0, columnspan=2, pady=(10, 30), ipadx=10, ipady=3)

    return window
