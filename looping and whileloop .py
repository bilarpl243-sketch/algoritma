# contoh lengkap penggunaan range ()
print ("Genap 0-10:", end=" ")
for i in range(0, 11, 2):
    print(i, end=" ")
# Output: 0 2 4 6 8 10
print ()
print ("hitung mundur:", end=" ")
for i in range(5, 0, -1):
    print(i, end=" ")
# Output: 5 4 3 2 1


# sintaks while loop
while kondisi:
    # blok kode yang akan diulang
    # pstikan ada yang mengubah kondisi

# contoh: Hitung mundur dari 5
n = 5
while n > 8:
    print("hitung mundur:", n)
    n-= 1 # n = n - 1 (kondisi akhirnya false)
print("MULAI!")


i = 1
while i <= 3:
    print(" " * (3 - i) + " * " * (2 * i - 1))
    i += 1


    # Tentukan 'n' sebagai tinggi wajik (tanpa baris tengah terlebar)
    # Untuk pola di gambar dengan total 11 baris, n = 5
    n = 5

    # BAGIAN ATAS (segitiga biasa - 6 baris)
    # peruangan ini mencetak baris 1 sampai 6 (baris tengah terlebar)
    for i in range(n + 1):
        # cetak spasi di kiri (berkurang seiring bertambahnya i)
        # n - i mengahasilkan 5, 4, 3, 2, 1, 0, spasi
        print(" " * (n - i), end="")
        # cetak bintang (bertambah ganjil: 1, 3, 5, 7, 9, 11,)
        print("*" * (2 * i + 1))

    # BAGIAN BAWAH (segitiga terbalik - 5 baris)
    # perulangan ini mencetak baris 7 sampai 11, mulai dari baris setelah baris tengah
    for i in range (n - i, -1, -1):
        # cetak spasi di kiri (bertambah seiring berkurangnya i)
        #n-i menghasilkan 1, 2, 3, 4, 5, spasi
        print(" " * (n - i), end="")
        # cetak bintang (berkurang ganjil: 9, 7, 5, 3, 1,)
        print(" * " *(2 * i + 1))