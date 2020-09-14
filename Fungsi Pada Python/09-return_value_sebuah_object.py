def buat_objek_nama(nama_awal, nama_akhir):
    """ Membelikan nilai kembalian/return value dalam bentuk struktur data dictionary """
    anda = {'nama_awal' : nama_awal, 'nama_akhir' : nama_akhir}
    return anda

data_anda = buat_objek_nama('akhmad','zaki')
print(data_anda)