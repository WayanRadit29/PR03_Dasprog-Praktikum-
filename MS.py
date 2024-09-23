#Input jumlah kata-kata acak yang mewakili ukuran dan sisi sepatu, misalkan n sebagai jumlah kata acak
n = int(input())

#Bikin array buat nampung kata-kata acak
kata_acak = [0] * n

#Input kata-kata acaknya menggunakan for loop
for i in range(0, n):
    kata_acak[i] = input()

#Buat dictionary "jumlah_sepatu" buat hitung jumlah sepatu sesuai ukuran & sisi (L/R)
jumlah_sepatu = {}

#Buat Looping buat misahin antara ukuran (karakter angka) dan sisi (karakter huruf)
for k in kata_acak:
    ukuran = '' #Deklarasi variabel ukuran dan sisi yang nilainya tidak ada
    sisi = ''   #Alias ini disebut string kosong yang nilainya siap diisi
    for char in k:
        if char.isdigit(): #Ngecek apakah dia termasuk karakter angka atau tidak
            ukuran += char  #Mengisi nilai ukuran sepatu dengan karakter angka pada kata acak
        elif char in ['L', 'R']: #Atau bisa pakek: elif char == 'L' or char == 'R'
            sisi = char  #Mengisi nilai sisi dengan karakter "L" atau "R"

    #Kita update jumlah sepatunya di dictionary "jumlah_sepatu"
    if ukuran and sisi:
        if ukuran not in jumlah_sepatu:
            jumlah_sepatu[ukuran] = {'L': 0, 'R': 0}  #Kalau ukuran beluma ada di dictionary, kita input dulu
        jumlah_sepatu[ukuran][sisi] += 1  #nilai sisi "L" atau "R" ditambah satu pada key "ukuran"

#Menghitung total pasangan sepatu
total_pasang = 0
for ukuran, sisi in jumlah_sepatu.items():
    #Cari nilai minimun antara jumlah sisi 'L' atau 'R' pada satu jenis ukuran sepatu
    #Karena dihitung 1 pasang jika ada 1 sisi kiri dan 1 sisi kanan pada jenis ukuran yang sama
    total_pasang += min(sisi['L'], sisi['R'])  
    

#print output total pasangan sepatu
print(total_pasang)
