import tkinter as tk

def aksi_tombol():
    label.config(text="iyahh okh")  

def ubah_judul():
    new_title = entry_judul.get()
    if new_title:
        window.title(new_title)

def keluar():
    window.destroy()

def on_enter(e):
    button.config(bg="#b8860b")

def on_leave(e):
    button.config(bg="#d2b48c", cursor="hand2")

# Membuat jendela utama
window = tk.Tk()
window.title("CoffeeShop GUI")
window.geometry("400x400")
window.configure(bg="#f5f5dc")

# Membuat label
label = tk.Label(window, text="Halo Iping Al Gaib\nSelamat Datang di CMI Coffee", bg="#f5f5dc", font=("Poppins", 14))
label.pack(pady=30)

# Membuat tombol dengan font Poppins bold
button = tk.Button(window, text="Lanjutin web hmpb woy", font=("Poppins", 12, "bold"), bg="#d2b48c", command=aksi_tombol)
button.bind("<Enter>", on_enter)
button.bind("<Leave>", on_leave)
button.pack(pady=5)

# Membuat entry untuk mengubah judul
entry_judul = tk.Entry(window, width=30)
entry_judul.pack(pady=5)

# Membuat tombol untuk mengubah judul
button_judul = tk.Button(window, text="Ubah Judul", font=("Poppins", 12, "bold"), command=ubah_judul)
button_judul.pack(pady=5)

# Membuat tombol untuk keluar
button_keluar = tk.Button(window, text="Keluar", font=("Poppins", 12, "bold"), command=keluar)
button_keluar.pack(pady=5)

# Menjalankan aplikasi
window.mainloop()

