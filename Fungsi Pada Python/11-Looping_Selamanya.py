def gabung_nama(nama_awal, nama_akhir):
    """Kembalikan nilai nama secara lengkap."""
    nama_lengkap = '{} {}'.format(nama_awal,nama_akhir)
    return nama_lengkap.title()

'''
Ini adalah looping selamanya, 
kecuali anda menekana CTRL+C 
dan kemudian tekan ENTER 
untuk menghentikannya.
'''
while True:
    print("\n Tolong Sebutkan Nama Anda: ")
    nama_awal = input("Nama Awal: ")
    nama_akhir = input("Nama Akhir: ")
    nama_lengkap = gabung_nama(nama_awal,nama_akhir)
    print("\n Halo, {}".format(nama_lengkap))
    