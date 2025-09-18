# tugas3.py

# 1. Deklarasi Variabel dan Tipe Data
Nama = "Fairuz Athallah"  # string
Umur = 21                 # integer
Berat_Badan = 68.5        # float
Mahasiswa = True          # boolean
Identitas_Mahasiswa = ["D4 Teknik Elektro", "Jurusan Teknik Elektro", "Politeknik Negeri Sriwijaya"] # list


# 2. Manipulasi String
print("--- Manipulasi String ---")
Perkenalan = "Halo, nama saya " + Nama + "."
print(Perkenalan)

# Menghitung panjang string
panjang_nama = len(Nama)
print(f"Panjang Nama: {panjang_nama} karakter")

# Mengubah huruf menjadi besar dan kecil
nama_besar = Nama.upper()
nama_kecil = Nama.lower()
print(f"Nama huruf besar: {nama_besar}")
print(f"Nama huruf kecil: {nama_kecil}")


# 3. Operasi Matematika Sederhana
print("\n--- Operasi Matematika Sederhana ---")
angka1 = 10
angka2 = 5
print(f"Angka 1: {angka1}, Angka 2: {angka2}") # Deklarasi Angka
print(f"Penjumlahan: {angka1 + angka2}")       # Penjumlahan
print(f"Pengurangan: {angka1 - angka2}")       # Pengurangan
print(f"Perkalian: {angka1 * angka2}")         # Perkalian
print(f"Pembagian: {angka1 / angka2}")         # Pembagian
print(f"Pembagian bulat: {angka1 // angka2}")  # Pembagian Bulat
print(f"Sisa bagi: {angka1 % angka2}")         # Sisa Bagi


# 4. List dan Akses Elemen
print("\n--- List dan Akses Elemen ---")
print(f"Identitas Mahasiswa: {Identitas_Mahasiswa}")

# Menampilkan elemen tertentu (elemen pertama)
print(f"Prodi: {Identitas_Mahasiswa[0]}")

# Menambahkan item baru ke list
Identitas_Mahasiswa.append("Semester 7")
print(f"Identitas Mahasiswa setelah ditambah: {Identitas_Mahasiswa}")

# Menghapus item dari list (menggunakan nilai)
Identitas_Mahasiswa.remove("Jurusan Teknik Elektro")
print(f"Identitas Mahasiswa setelah 'Jurusan Teknik Elektro' dihapus: {Identitas_Mahasiswa}")


# 5. Penggunaan Input dari User
print("\n--- Penggunaan Input dari User ---")
nama_user = input("Masukkan Nama Anda: ")
umur_user = input("Masukkan Umur Anda: ")
print(f"Halo, nama saya {nama_user} dan umur saya {umur_user} tahun.")