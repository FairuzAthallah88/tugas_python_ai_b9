# tugas5.py

# --- Function ---
def greet(nama: str) -> str:
    """Mengembalikan teks sapaan: 'Halo, <nama>!'."""
    return f"Halo, {nama}!"

def tambah(a: float, b: float = 0.0) -> float:
    """Mengembalikan hasil penjumlahan a + b."""
    return a + b

def rata_rata(angka: list[float]) -> float:
    """
    Menghitung rata-rata dari sebuah list angka.
    Mengembalikan 0.0 jika list kosong, dan rata-rata dengan 2 angka di belakang koma.
    """
    if not angka:
        return 0.0
    total = sum(angka)
    return round(total / len(angka), 2)

# --- Class ---
class Student:
    """
    Kelas untuk merepresentasikan data seorang mahasiswa.
    Termasuk nama, NIM, dan daftar nilai.
    """
    def __init__(self, nama: str, nim: str, nilai: list[float] = None):
        self.nama = nama
        self.nim = nim
        self.nilai = nilai if nilai is not None else []

    def tambah_nilai(self, skor: float):
        """Menambahkan satu nilai ke dalam list nilai mahasiswa."""
        self.nilai.append(skor)

    def rata_nilai(self) -> float:
        """Mengembalikan rata-rata nilai mahasiswa menggunakan fungsi rata_rata()."""
        return rata_rata(self.nilai)

    def status(self, threshold: float = 70.0) -> str:
        """Menentukan status kelulusan berdasarkan rata-rata nilai."""
        rata = self.rata_nilai()
        return "LULUS" if rata >= threshold else "TIDAK LULUS"
    
    def __str__(self) -> str:
        """
        Mengembalikan representasi string ringkas dari objek Student,
        digunakan saat objek dicetak.
        """
        rata = self.rata_nilai()
        stat = self.status()
        return f"Student(nama='{self.nama}', nim='{self.nim}', rata={rata}, status={stat})"


# --- DEMO ---
if __name__ == "__main__":
    print("=== FUNCTIONS ===")
    
    # Mengambil input dari user untuk fungsi greet()
    nama_user = input("Masukkan Nama Anda : ")
    print(greet(nama_user))

    # Mengambil input dari user untuk fungsi tambah()
    try:
        angka_a = float(input("Masukkan angka pertama (a): "))
        angka_b = float(input("Masukkan angka kedua (b): "))
        print(f"Hasil tambah({angka_a}, {angka_b}): {tambah(angka_a, angka_b)}")
    except ValueError:
        print("Input tidak valid. Masukkan angka.")

    # Mengambil input dari user untuk fungsi rata_rata()
    print("\nRATA-RATA")
    print("Masukkan nilai-nilai (ketik 'done' jika selesai):")
    nilai_input = []
    while True:
        input_nilai = input("Masukkan nilai: ")
        if input_nilai.lower() == 'done':
            break
        try:
            nilai_input.append(float(input_nilai))
        except ValueError:
            print("Input tidak valid. Masukkan angka.")

    print(f"Hasil rata_rata({nilai_input}) adalah {rata_rata(nilai_input)}")

    print("\n=== CLASS STUDENT ===")
    
    # Membuat objek mahasiswa dengan input dari user
    print("Masukkan data mahasiswa pertama:")
    nama_mhs1 = input("Nama: ")
    nim_mhs1 = input("NIM: ")
    mhs1 = Student(nama_mhs1, nim_mhs1)

    print("Masukkan nilai-nilai Mata Kuliah (ketik 'selesai' jika selesai):")
    while True:
        skor_input = input("Nilai: ")
        if skor_input.lower() == 'selesai':
            break
        try:
            mhs1.tambah_nilai(float(skor_input))
        except ValueError:
            print("Input tidak valid. Masukkan angka.")
    
    print(f"\nMahasiswa 1: {mhs1}")
    print(f"Rata-rata nilai {mhs1.nama}: {mhs1.rata_nilai()}")
    print(f"Status {mhs1.nama}: {mhs1.status()}")