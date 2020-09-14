def nama_buku(*buku):
    """ Nama-nama buku Anda """
    print("\n Sebutkan nama-nama buku anda dirumah : ")
    for item in buku:
        print("- {} ".format(item))
print(nama_buku('Kubernetes', 'Blockchain', 'Machine Learning'))