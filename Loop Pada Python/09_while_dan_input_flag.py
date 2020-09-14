''' 
Biasanya, while digunakan
untuk menunggu masukan
dari pengguna, dan kita
bisa menggunakan satu flag
semisal active flag dengan 
nilai boolean true atau false,
tapi tetap menggunakan kata
'keluar' sebagai penanda keluar
program
'''
active = True
welcome = "\nKatakan sesuatu kepada saya, saya akan tulis di layar: \
\nAtau tulis 'keluar' jika anda sudah selesai...\n"
pesan = ""
while active:
    pesan = input(welcome)
    if pesan.strip().lower() in ('keluar','quit','exit'):
        active = False # Selain flag , anda juga bisa menggunakan operator break.
    else:
        print('\nAnda Mengetik Pesan : {}'.format(pesan))
