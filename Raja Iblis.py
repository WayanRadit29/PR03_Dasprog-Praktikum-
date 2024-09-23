U = int(input())
K = int(input())
M = int(input())

Sisa_Minion = M//2
Sisa_Knight = K//2


Gerbang1 = U - (Sisa_Minion*2)
Gerbang2 = Gerbang1 - ((Sisa_Knight * 5))*5
Gerbang3 = Gerbang2 - (1000)

if Gerbang3 > 0:
    print(f"Yey! Ucup Menang! HP tersisa: {Gerbang3}")

else:
    print("Yah! Ucup Meninggoy.")