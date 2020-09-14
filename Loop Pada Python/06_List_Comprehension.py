'''
Menggunakan List untuk
melakukan looping sehingga
menghasilkan list baru
'''
BilanganInteger = [1,2,3,4,5,6,7,8,9,10]
'''
Dalam contoh ini kita akan
mengambil bilangan genap
dari list diatas ke dalam 
list baru menggunakan list
comprehension
'''
BilanganGenap = [i for i in BilanganInteger if i%2 == 0]

print(BilanganGenap)

