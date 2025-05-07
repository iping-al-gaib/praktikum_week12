def hitung_total(harga, jumlah):
    try:
        return float(harga) * int(jumlah)
    except ValueError:
        return 