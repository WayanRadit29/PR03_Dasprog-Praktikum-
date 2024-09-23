#Input jumlah elemen array
n = int(input())

#Membuat dua array A dan B menggunakan input satu baris untuk diisi sesuai jumlah elemen arraynya
A = list(map(int, input().split()))
B = list(map(int, input().split()))

#Input banyak subarray yang akan dibentuk
t = int(input())

#Membuat array baru Menyimpan hasil perbandingan berupa "YA" atau "TIDAK"
results = []

#Membuat fungsi untuk menghitung jumlah elemen dalam subarray dari indeks l hingga r
def sum_subarray(array, l, r):
    total = 0
    for i in range(l, r + 1):
        total += array[i]
    return total

#Looping untuk menginput dan menghitung nilai setiap elemen dari subarray A dan B
for i in range(0, t):
    #Input l dan r
    l, r = map(int, input().split())

    if 0 <= l < r < n:
        #Menghitung jumlah subarray A(l, r) dan B(l, r)
        sum_A = sum_subarray(A, l, r)
        sum_B = sum_subarray(B, l, r)
        
        #Append artinya menambahkan string "YA" atau "TIDAK" ke array bernama result untuk disimpan terlebih dahulu 
        #Lalu di print sekalian nanti di akhir
        if sum_A == sum_B:
            results.append("YA") #Append artinya menambahkan string "YA" ke array bernama result
        else:
            results.append("TIDAK") #Ini juga sama
    else:
        print("Data yang anda masukan tidak valid pastikan cek batasan pada soal")

#Menggunakan for loop untuk mengprint semua nilai dari array bernama results
for result in results:
    print(result)
