def buat_objek_nama(nama_awal, nama_akhir, umur=None):
    """ Membelikan nilai kembalian/return value dalam bentuk struktur data dictionary """
    anda = {'nama_awal' : nama_awal, 'nama_akhir' : nama_akhir, 'umur': umur}
    return anda

data_anda = buat_objek_nama('akhmad','zaki', 36)
print(data_anda)
data_anda = buat_objek_nama('akhmad','zaki')
print(data_anda)