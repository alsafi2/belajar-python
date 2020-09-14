''' 
Biasanya, while digunakan
untuk menunggu masukan
dari pengguna, dan kita
bisa menggunakan satu kata
semisal "keluar" untuk
keluar dari while Loop
'''
welcome = "\nKatakan sesuatu kepada saya, saya akan tulis di layar: \
\nAtau tulis 'keluar' jika anda sudah selesai...\n"
pesan = ""
while pesan != "keluar":
    pesan = input(welcome)
    print('\nAnda Mengetik Pesan : {}'.format(pesan))

