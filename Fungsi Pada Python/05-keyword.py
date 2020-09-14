def contoh_kata(nama_bahasa,kata):
    """ Menampilkan Informasi mengenai kata dalam bahasa """
    print("\n Di dalam bahasa {}.".format(nama_bahasa))
    print("Kata dalam bahasa {} adalah {}.".format(nama_bahasa,kata.title()))
contoh_kata(nama_bahasa='Indonesia', kata='Piring')
contoh_kata(kata="garpu", nama_bahasa="Indonesia")