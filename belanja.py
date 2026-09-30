# a) Membuat list kosong bernama belanja
belanja = []

# b) Meminta pengguna memasukkan 5 nama barang menggunakan loop
print("Silakan masukkan 5 nama barang:")
for i in range(5):
    barang = input(f"Masukkan barang ke-{i+1}: ")
    belanja.append(barang)

print("\n=== OUTPUT PROGRAM ===")

# c) Menampilkan daftar belanja bernomor
print("Daftar Belanja:")
for nomor, barang in enumerate(belanja, start=1):
    print(f"{nomor}. {barang}")

# d) Menampilkan total item dan item ke-3 dalam daftar
total_item = len(belanja)
item_ketiga = belanja[2]  # Indeks 2 merujuk pada item urutan ke-3

print(f"\nTotal item: {total_item}")
print(f"Item ke-3 dalam daftar: {item_ketiga}")