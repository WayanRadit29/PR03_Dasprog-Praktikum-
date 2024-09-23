#Proses Inputasi titik-titik 
x1, y1 = map(int,input().split()) #Titik pusat lingkaran
xs,ys = map(int,input().split()) #Titik awal king
xf, yf = map(int,input().split()) #Titik akhir king

#Menghitung jarak antara titik awal dan titik akhir king :
jarak_kuadratA = (xf - xs)**2 + (yf - ys)**2

#Menghitung jarak antara titik pusat lingkaran dan titik akhir king:
jarak_kuadratL = (xf - x1)**2 + (yf - y1)**2


if jarak_kuadratA >= jarak_kuadratL:
    print("No")
else:
    print("Yes")