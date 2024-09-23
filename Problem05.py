#Yuk gaes, mulai dengan input banyak jenis barang yang ada di toko
N_item = int(input())
    
#Saatnya kita input daftar item di toko dan jumlahnya
store_items = {}
for i in range(0, N_item):
    line = input().split()
    item_name = line[0]
    item_quantity = int(line[1])
    store_items[item_name] = item_quantity
    
#Sekarang, input banyak item di keranjang Charlie
N_c_item = int(input())
    
#Saatnya catat apa aja yang ada di keranjang Charlie
charlie_cart = {}
for j in range(0, N_c_item):
    line = input().split()
    item_name = line[0]
    item_quantity = int(line[1])
    charlie_cart[item_name] = item_quantity
    
#Tampilkan item-item yang ada di keranjang Charlie
print("CHARLIE")
print(" ".join(charlie_cart.keys())) #untuk mengprint semua kunci dalam dictionary charlie_cart dalam satu baris yang dipisahkan spasi " "
    
#Tampilkan item-item di toko dan sisa kuantitasnya
print("STORAGE")
for item_name in store_items:
    if item_name in charlie_cart:
        remaining_quantity = store_items[item_name] - charlie_cart[item_name]
        print(f"{item_name}: {remaining_quantity}")
    else:
        print(f"{item_name}: {store_items[item_name]}")
