# tugas4.py

# --- List - akses & manipulasi ---
print("--- List ---")
data_list = ["Arduino UNO", 15, "ESP32", 9, "Raspberry Pi", 20, "Arduino Mega"]
print(f"List : {data_list}")
print(f"Elemen pertama: {data_list[0]}")
print(f"Elemen terakhir: {data_list[-1]}")
print(f"Slicing [1:6:2]: {data_list[1:6:2]}")

data_list.append("LED")
print(f"append ('LED'): {data_list}")
data_list.insert(2, "Motor")
print(f"insert (2, 'Motor'): {data_list}")
data_list.extend([100, 200])
print(f"Extend ([100, 200]): {data_list}")
data_list.pop(1)
print(f"pop(1): {data_list}")
data_list.remove("ESP32")
print(f"remove ('ESP32'): {data_list}")


# --- Tuple - immutability & unpacking ---
print("\n--- Tuple - immutability & unpacking ---")
data_tuple = ("Fairuz", 21, "Teknik Elektro", 2022, "Palembang")
print(f"Tuple: {data_tuple}")
print(f"Panjang tuple: {len(data_tuple)}")
print(f"Akses indeks 1: {data_tuple[1]}")
nama, umur, *lainnya = data_tuple
print(f"Unpacking: nama: {nama}, umur: {umur}, lainnya: {lainnya}")


# --- Set - keunikan & operasi himpunan ---
print("\n--- Set - keunikan & operasi himpunan ---")
set1 = {1, 2, 3, 4, 5, 2, 1}
set2 = {4, 5, 6, 7, 8}
print(f"Set 1 (duplikat hilang): {set1}")
print(f"Set 2: {set2}")
print(f"Union (|): {set1 | set2}")
print(f"Intersection (&): {set1 & set2}")
print(f"Difference (-): {set1 - set2}")
print(f"Symmetric difference (^): {set1 ^ set2}")


# --- Dictionary - key/value dasar ---
print("\n--- Dictionary ---")
data_mahasiswa = {
    "Nama": "Athallah",
    "Nim": "062240342200",
    "Angkatan": 2022,
    "Kota": "Palembang"
}
print(f"Dict awal: {data_mahasiswa}")

data_mahasiswa["Prodi"] = "D4 Teknik Elektro"
print(f"Tambah 'Prodi': {data_mahasiswa}")
data_mahasiswa["Kota"] = "Prabumulih"
print(f"Ubah nilai 'Kota': {data_mahasiswa}")
del data_mahasiswa["Nim"]
print(f"Hapus key 'Nim': {data_mahasiswa}")

print(f"Keys: {data_mahasiswa.keys()}")
print(f"Values: {data_mahasiswa.values()}")
print(f"Items: {data_mahasiswa.items()}")

print("Iterasi key: value:")
for key, value in data_mahasiswa.items():
    print(f"{key}: {value}")


# --- Nested structures ---
print("\n--- Nested Structures ---")
daftar_komponen = [
     {"nama": "Resistor", "nilai": "10k ohm", "jenis": "Pasif"},
     {"nama": "Kapasitor", "nilai": "100uF", "jenis": "Pasif"},
     {"nama": "Transistor", "nilai": "NPN", "jenis": "Aktif"},
     {"nama": "LED", "nilai": "Merah", "jenis": "Aktif"},
     {"nama": "Induktor", "nilai": "10mH", "jenis": "Pasif"}
]

# Mencetak semua nama komponen
print("Daftar nama komponen:")
for komponen in daftar_komponen:
     print(f"- {komponen['nama']}")

#Filter komponen aktif menggunakan list comprehension
komponen_aktif = [
     komp for komp in daftar_komponen if komp["jenis"] == "Aktif"
]
print("Komponen-komponen Aktif:")
for komp in komponen_aktif:
     print(f"- {komp['nama']} ({komp['nilai']})")


# --- Comprehension & utilitas ---
print("\n--- Comprehension & Utilitas ---")
# List comprehension
angka_1_20 = range(1, 21)
list_genap = [i for i in angka_1_20 if i % 2 == 0]
list_kuadrat = [i**2 for i in angka_1_20]
print(f"List genap (1-20): {list_genap}")
print(f"List kuadrat (1-20): {list_kuadrat}")

# Dict comprehension
dict_genap_ganjil = {i: "genap" if i % 2 == 0 else "ganjil" for i in range(1, 11)}
print(f"Dict genap/ganjil: {dict_genap_ganjil}")

# Set comprehension
kalimat = "Hello python programming"
huruf_unik = {huruf for huruf in kalimat.lower() if huruf.isalpha()}
print(kalimat)
print(f"Huruf unik dari kalimat: {huruf_unik}")


# --- Keanggotaan & pencarian sederhana ---
print("\n--- Keanggotaan & Pencarian Sederhana ---")
mencari_buah = "anggur"
if mencari_buah in data_list:
     print(f"'{mencari_buah}' ada di list.")
     print(f"Posisi '{mencari_buah}': {data_list.index(mencari_buah)}")
else:
     print(f"'{mencari_buah}' tidak ada di list.")