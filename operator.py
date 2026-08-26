print("== progam cek kelulusan ==")

# 1. input() - minimal 1
nilai = int(input("masukkan nilai ujian: "))
nilai_tugas = int(input("masukkan nilai tugas: "))

# 2. operator aritmatika - minimal 2
total_nilai = nilai + nilai nilai_tugas    # +
rata_rata = total_nilai / 2                # /

# 3. operator perbandingan - minimal 2
lulus_ujian = nilai >= 75                  # >=
lulus rata + rata_rata >= 70               # >=

# 4. operator logika and dan for
if (lulus_ujian and lulus rata) or (rata_rata >= 85):
    print("selamat, kamu LULUS!")
else:
    print("maaf, kamu TIDAK LULUS. tetap semangat!")

print("---------------------")
print("total nilai :", total nilai)
print("rata-rata:", rata)
print("lulus ujian >=75:", lulus_ujian)
print("lulus rata-rata >=70:, lulus_rata")