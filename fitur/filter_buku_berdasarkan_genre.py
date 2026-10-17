class Buku:
    # Menambahkan parameter genre pada constructor
    def __init__(self, judul, penulis, isbn, tahun_terbit, genre, status="Tersedia"):
        self.judul = judul
        self.penulis = penulis
        self.isbn = isbn
        self.tahun_terbit = tahun_terbit
        self.genre = genre  
        self.status = status

    def __str__(self):
        return f"[{self.isbn}] {self.judul} | Genre: {self.genre} | Penulis: {self.penulis} ({self.tahun_terbit}) - {self.status}"

class SistemPerpustakaan:
    def __init__(self):
        self.koleksi_buku = []

    def tambah_buku(self, buku):
        self.koleksi_buku.append(buku)

    def filter_buku_berdasarkan_genre(self, genre_target):
        """
        Menyaring koleksi buku berdasarkan genre tertentu.
        Mendukung pencarian parsial dan mengabaikan huruf besar/kecil.
        """
        hasil_filter = []
        genre_target = genre_target.lower()

        for buku in self.koleksi_buku:
            # Pengecekan dilakukan dalam huruf kecil agar "Fiksi" dan "fiksi" dianggap sama
            if genre_target in buku.genre.lower():
                hasil_filter.append(buku)

        return hasil_filter

# ==========================================
# CONTOH PENGGUNAAN
# ==========================================

# 1. Inisialisasi Sistem
perpustakaan = SistemPerpustakaan()

# 2. Menambahkan Data Dummy dengan atribut Genre
perpustakaan.tambah_buku(Buku("Struktur Data dan Algoritma", "Budi S.", "978-01", 2023, "Teknologi Informasi"))
perpustakaan.tambah_buku(Buku("Laskar Pelangi", "Andrea Hirata", "978-02", 2005, "Fiksi Drama"))
perpustakaan.tambah_buku(Buku("Sistem Basis Data", "Siti Aisyah", "978-03", 2024, "Teknologi Informasi"))
perpustakaan.tambah_buku(Buku("Bumi Manusia", "Pramoedya A. T.", "978-04", 1980, "Fiksi Sejarah"))

# 3. Menguji Fitur Filter Genre
print("--- Filter Genre: 'Teknologi Informasi' ---")
hasil_teknologi = perpustakaan.filter_buku_berdasarkan_genre("teknologi informasi")
for b in hasil_teknologi:
    print(b)

print("\n--- Filter Genre: 'Fiksi' ---")
# Akan menampilkan "Fiksi Drama" dan "Fiksi Sejarah" karena menggunakan pencocokan parsial
hasil_fiksi = perpustakaan.filter_buku_berdasarkan_genre("fiksi")
for b in hasil_fiksi:
    print(b)