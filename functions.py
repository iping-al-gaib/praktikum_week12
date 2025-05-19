def aksi_tombol(label_info):
    label_info.config(text="anjayy bisa gitu bro")

def ubah_judul(window, entry_judul):
    new_title = entry_judul.get()
    if new_title:
        window.title(new_title)

def keluar(window):
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

def proses(harga_entry, jumlah_entry, diskon_entry, hasil_label, hitung_total_func):
    harga = harga_entry.get()
    jumlah = jumlah_entry.get()
    diskon = diskon_entry.get()
    total, total_setelah_diskon = hitung_total_func(harga, jumlah, diskon)
    hasil_label.config(
        text=f"Total Sebelum Diskon:\nRp {total:,.2f}\n\nTotal Setelah Diskon:\nRp {total_setelah_diskon:,.2f}"
    )
