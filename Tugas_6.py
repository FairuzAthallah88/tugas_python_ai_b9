# tugas6.py

import numpy as np
import pandas as pd
import os
np.random.seed(42)

# --- Class GradeBook ---
class GradeBook:
    """Kelas untuk mengelola dan menganalisis data nilai mahasiswa."""
    def __init__(self, df: pd.DataFrame):
        self.df = df
    
    def average(self) -> float:
        """Menghitung rata-rata nilai dari DataFrame."""
        return self.df['nilai'].mean()

    def pass_rate(self, threshold: float = 70.0) -> float:
        """Menghitung persentase mahasiswa yang lulus."""
        lulus = self.df[self.df['nilai'] >= threshold]
        return (len(lulus) / len(self.df)) * 100

    def save_summary(self, path: str):
        """Menulis ringkasan ke file teks."""
        summary = f"Ringkasan Data Nilai\n"
        summary += f"========================\n"
        summary += f"Jumlah Data: {len(self.df)} Mahasiswa\n"
        summary += f"Rata-rata Nilai: {self.average():.2f}\n"
        summary += f"Persentase Lulus (>={70.0}): {self.pass_rate():.2f}%\n"
        summary += f"Jumlah Lulus: {len(self.df[self.df['status'] == 'LULUS'])}\n"
        summary += f"Jumlah Tidak Lulus: {len(self.df[self.df['status'] == 'TIDAK LULUS'])}\n"
        
        with open(path, 'w') as file:
            file.write(summary)
            
    def __str__(self) -> str:
        """Mengembalikan string ringkas tentang GradeBook."""
        return f"GradeBook(total_data={len(self.df)}, rata_rata_nilai={self.average():.2f})"

# --- Demo ---
if __name__ == "__main__":
    
    print("=== NUMPY ===")
    
    # Membuat array NumPy berisi nilai ujian acak
    nilai_ujian = np.random.randint(50, 100, size=12)
    print(f"Array nilai ujian: {nilai_ujian}")
    
    # Menghitung statistik NumPy
    rata_rata_np = np.mean(nilai_ujian)
    median_np = np.median(nilai_ujian)
    std_dev_np = np.std(nilai_ujian)
    min_np = np.min(nilai_ujian)
    max_np = np.max(nilai_ujian)

    print(f"Rata-rata: {rata_rata_np:.2f}")
    print(f"Median: {median_np}")
    print(f"Standar Deviasi: {std_dev_np:.2f}")
    print(f"Nilai Minimum: {min_np}")
    print(f"Nilai Maksimum: {max_np}")
    
    # Menulis ringkasan NumPy ke file
    with open('ringkasan_tugas6.txt', 'w') as f:
        f.write("=== Ringkasan Statistik NumPy ===\n")
        f.write(f"Rata-rata: {rata_rata_np:.2f}\n")
        f.write(f"Median: {median_np}\n")
        f.write(f"Standar Deviasi: {std_dev_np:.2f}\n")
        f.write(f"Nilai Minimum: {min_np}\n")
        f.write(f"Nilai Maksimum: {max_np}\n\n")

    print("\n" + "="*50 + "\n")

    print("=== PANDAS ===")
    
    # Membuat DataFrame
    data_mahasiswa = {
        'nama': ['Budi', 'Siti', 'Joko', 'Ani', 'Fajar', 'Maya', 'Rudi', 'Lisa', 'Eka', 'Gilang'],
        'nim': ['101', '102', '103', '104', '105', '106', '107', '108', '109', '110'],
        'nilai': nilai_ujian[:10]  # Mengambil 10 data pertama dari array NumPy
    }
    df = pd.DataFrame(data_mahasiswa)

    # Menambahkan kolom 'status'
    df['status'] = np.where(df['nilai'] >= 70, 'LULUS', 'TIDAK LULUS')
    
    print("DataFrame Mahasiswa (5 baris pertama):")
    print(df.head())
    
    print("\n" + "="*50 + "\n")

    print("=== OOP: GRADEBOOK ===")
    
    # Membuat objek GradeBook
    grade_book = GradeBook(df)
    
    # Menggunakan metode-metode kelas
    print(f"Ringkasan objek: {grade_book}")
    
    rata_rata_df = grade_book.average()
    persentase_lulus = grade_book.pass_rate()
    
    print(f"Rata-rata nilai: {rata_rata_df:.2f}")
    print(f"Persentase kelulusan: {persentase_lulus:.2f}%")
    
    # Menyimpan ringkasan ke file .txt
    grade_book.save_summary('ringkasan_tugas6.txt')
    print("\nRingkasan telah disimpan ke file 'ringkasan_tugas6.txt'.")