def profil_mahasiswa(nama_awal, nama_akhir, **info_mhs):
    """Membuat dictionary python untuk data profil mahasiswa."""
    info_mhs['nama_awal'] = nama_awal
    info_mhs['nama_akhir'] = nama_akhir
    return info_mhs

profil_mhs = profil_mahasiswa('akhmad','zaki',lokasi="palmerah",jurusan='Akuntansi Komputer')
print(profil_mhs)