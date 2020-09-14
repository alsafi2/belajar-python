def gabung_nama(nama_awal, nama_akhir):
    """Kembalikan nilai nama secara lengkap"""
    nama_lengkap = '{} {}'.format(nama_awal,nama_akhir)
    return nama_lengkap.title()
nama_anda = gabung_nama('akhmad','zaki')
print(nama_anda)