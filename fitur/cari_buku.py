class Buku:
    def __init__(self, judul, penulis, isbn, tahun_terbit, status="Tersedia"):
        self.judul = judul
        self.penulis = penulis
        self.isbn = isbn
        self.tahun_terbit = tahun_terbit
        self.status = status

    def __str__(self):
        return f"[{self.isbn}] {self.judul} | Penulis: {self.penulis} ({self.tahun_terbit}) - {self.status}"

class SistemPerpustakaan:
    def __init__(self):
        # Menyimpan data di dalam list memori (bisa diganti dengan database nantinya)
        self.koleksi_buku = []

    def tambah_buku(self, buku):
        self.koleksi_buku.append(buku)

    def cari_buku(self, kata_kunci, berdasarkan="judul"):
        """
        Mencari buku berdasarkan kata kunci.
        Parameter 'berdasarkan' bisa diisi: 'judul', 'penulis', atau 'isbn'.
        """
        hasil_pencarian = []
        # Ubah kata kunci ke huruf kecil untuk pencarian case-insensitive
        kata_kunci = kata_kunci.lower()

        for buku in self.koleksi_buku:
            # Ambil nilai atribut yang sesuai dan ubah ke huruf kecil
            if berdasarkan == "judul":
                target = buku.judul.lower()
            elif berdasarkan == "penulis":
                target = buku.penulis.lower()
            elif berdasarkan == "isbn":
                target = buku.isbn.lower()
            else:
                print("Kategori pencarian tidak valid.")
                return []

            # Cek apakah kata kunci ada di dalam atribut target (partial match)
            if kata_kunci in target:
                hasil_pencarian.append(buku)

        return hasil_pencarian

# ==========================================
# CONTOH PENGGUNAAN
# ==========================================

# 1. Inisialisasi Sistem
perpustakaan = SistemPerpustakaan()

# 2. Menambahkan Data Dummy
perpustakaan.tambah_buku(Buku("Struktur Data dan Algoritma", "Budi S.", "978-602-01", 2023))
perpustakaan.tambah_buku(Buku("Pengantar Sistem Basis Data", "Siti Aisyah", "978-602-02", 2024))
perpustakaan.tambah_buku(Buku("Jaringan Komunikasi Terapan", "Budi S.", "978-602-03", 2022))

# 3. Menguji Fitur Pencarian
print("--- Hasil Pencarian Judul: 'Data' ---")
hasil_judul = perpustakaan.cari_buku("data", berdasarkan="judul")
for b in hasil_judul:
    print(b)

print("\n--- Hasil Pencarian Penulis: 'Budi' ---")
hasil_penulis = perpustakaan.cari_buku("budi", berdasarkan="penulis")
for b in hasil_penulis:
    print(b)