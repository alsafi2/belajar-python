def nama_lengkap_plus(nama_awal,nama_akhir,nama_tengah=''):
    """ kembalikan nilai nama lengkap plus nama tengah
    atau
    jika tidak ada kembalikan nama lengkap tanpa nama tengah"""

    if nama_tengah:
        nama_lengkap_plus = "{} {} {}".format(nama_awal,nama_tengah,nama_akhir)
    else:
        nama_lengkap_plus = "{} {}".format(nama_awal,nama_akhir)
    
    return nama_lengkap_plus
nama_anda = nama_lengkap_plus('akhmad','alsafi')
print(nama_anda)
nama_anda = nama_lengkap_plus('akhmad','alsafi','zaki')
print(nama_anda)