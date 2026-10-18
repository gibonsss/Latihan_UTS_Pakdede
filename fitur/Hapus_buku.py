class Buku:
    def __init__(self, judul, penulis, isbn, tahun_terbit, genre, status="Tersedia"):
        self.judul = judul
        self.penulis = penulis
        self.isbn = isbn
        self.tahun_terbit = tahun_terbit
        self.genre = genre  
        self.status = status

    def __str__(self):
        return f"[{self.isbn}] {self.judul} | Penulis: {self.penulis} - {self.status}"

class SistemPerpustakaan:
    def __init__(self):
        self.koleksi_buku = []

    def tambah_buku(self, buku):
        self.koleksi_buku.append(buku)

    def hapus_buku(self, isbn_target):
        """
        Menghapus buku dari koleksi berdasarkan ISBN.
        Mengembalikan True jika berhasil, False jika buku tidak ditemukan.
        """
        # Melakukan perulangan untuk mencari buku dengan ISBN yang cocok
        for buku in self.koleksi_buku:
            if buku.isbn.lower() == isbn_target.lower():
                self.koleksi_buku.remove(buku)
                print(f"Berhasil: Buku '{buku.judul}' (ISBN: {buku.isbn}) telah dihapus dari sistem.")
                return True
                
        print(f"Gagal: Buku dengan ISBN '{isbn_target}' tidak ditemukan.")
        return False

    def tampilkan_semua_buku(self):
        print("\n--- Daftar Koleksi Buku Saat Ini ---")
        if not self.koleksi_buku:
            print("Koleksi perpustakaan kosong.")
        for buku in self.koleksi_buku:
            print(buku)

# ==========================================
# CONTOH PENGGUNAAN
# ==========================================

# 1. Inisialisasi Sistem
perpustakaan = SistemPerpustakaan()
perpustakaan.tambah_buku(Buku("Struktur Data dan Algoritma", "Budi S.", "978-01", 2023, "Teknologi Informasi"))
perpustakaan.tambah_buku(Buku("Sistem Basis Data", "Siti Aisyah", "978-02", 2024, "Teknologi Informasi"))

# 2. Menampilkan koleksi awal
perpustakaan.tampilkan_semua_buku()

# 3. Menguji Fitur Hapus Buku (Buku Ditemukan)
print("\n[Proses Penghapusan]")
perpustakaan.hapus_buku("978-01")

# 4. Menguji Fitur Hapus Buku (Buku Tidak Ditemukan)
print("\n[Proses Penghapusan]")
perpustakaan.hapus_buku("978-99")

# 5. Menampilkan koleksi setelah penghapusan
perpustakaan.tampilkan_semua_buku()