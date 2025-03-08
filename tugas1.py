def hitung_biaya_pengiriman(berat, jarak, express=False, member=False):
    # Biaya dasar
    biaya = 10000
    
    # Tambahan biaya jika berat lebih dari 5 kg
    if berat > 5:
        biaya += 5000
    
    # Tambahan biaya jika jarak lebih dari 10 km
    if jarak > 10:
        biaya += 8000
    
    # Tambahan biaya untuk layanan express
    if express:
        biaya += 20000
    
    # Diskon untuk member
    if member:
        biaya *= 0.9  # Diskon 10%
    
    return biaya

# Contoh penggunaan
print(hitung_biaya_pengiriman(6, 15, express=True, member=True))  # Contoh dengan semua opsi aktif
