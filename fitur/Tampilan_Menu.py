class Buku:
    def __init__(self, judul, penulis, isbn, tahun_terbit, genre, status="Tersedia"):
        self.judul = judul
        self.penulis = penulis
        self.isbn = isbn
        self.tahun_terbit = tahun_terbit
        self.genre = genre
        self.status = status

    def __str__(self):
        return f"[{self.isbn}] {self.judul} | Penulis: {self.penulis} | Genre: {self.genre} ({self.tahun_terbit}) - {self.status}"

class SistemPerpustakaan:
    def __init__(self):
        self.koleksi_buku = []

    def tambah_buku(self, buku):
        self.koleksi_buku.append(buku)
        print(f"\n[Sukses] Buku '{buku.judul}' berhasil ditambahkan ke sistem!")

    def tampilkan_semua_buku(self):
        print("\n=== DAFTAR KOLEKSI BUKU ===")
        if not self.koleksi_buku:
            print("Koleksi perpustakaan masih kosong.")
        else:
            for index, buku in enumerate(self.koleksi_buku, start=1):
                print(f"{index}. {buku.judul} (ISBN: {buku.isbn})")
        print("===========================")

    def cari_buku(self, kata_kunci, berdasarkan="judul"):
        hasil = []
        for buku in self.koleksi_buku:
            target = getattr(buku, berdasarkan, "").lower()
            if kata_kunci.lower() in target:
                hasil.append(buku)
        return hasil

    def filter_buku_berdasarkan_genre(self, genre_target):
        return [buku for buku in self.koleksi_buku if genre_target.lower() in buku.genre.lower()]

    def hapus_buku(self, isbn_target):
        for buku in self.koleksi_buku:
            if buku.isbn.lower() == isbn_target.lower():
                self.koleksi_buku.remove(buku)
                print(f"\n[Sukses] Buku '{buku.judul}' (ISBN: {buku.isbn}) berhasil dihapus.")
                return True
        print(f"\n[Gagal] Buku dengan ISBN '{isbn_target}' tidak ditemukan.")
        return False

# ==========================================
# ANTARMUKA MENU INTERAKTIF (CONTROLLER)
# ==========================================

def menu_utama():
    perpustakaan = SistemPerpustakaan()

    # Menambahkan data awal (dummy)
    perpustakaan.tambah_buku(Buku("Struktur Data dan Algoritma", "Budi S.", "978-01", 2023, "Teknologi Informasi"))
    perpustakaan.tambah_buku(Buku("Sistem Basis Data", "Siti Aisyah", "978-02", 2024, "Teknologi Informasi"))

    while True:
        print("\n" + "="*30)
        print("   SISTEM MANAJEMEN PERPUSTAKAAN")
        print("="*30)
        print("1. Tambah Buku Baru")
        print("2. Tampilkan Semua Buku")
        print("3. Cari Buku")
        print("4. Filter Buku Berdasarkan Genre")
        print("5. Hapus Buku")
        print("0. Keluar Aplikasi")
        print("="*30)

        pilihan = input("Pilih menu (0-5): ").strip()

        if pilihan == '1':
            print("\n-- TAMBAH BUKU BARU --")
            judul = input("Judul Buku : ")
            penulis = input("Penulis    : ")
            isbn = input("ISBN       : ")
            genre = input("Genre      : ")
            
            # Validasi input angka untuk tahun
            while True:
                try:
                    tahun = int(input("Tahun Terbit (angka): "))
                    break
                except ValueError:
                    print("Peringatan: Tahun terbit harus berupa angka. Silakan coba lagi.")
            
            buku_baru = Buku(judul, penulis, isbn, tahun, genre)
            perpustakaan.tambah_buku(buku_baru)

        elif pilihan == '2':
            perpustakaan.tampilkan_semua_buku()

        elif pilihan == '3':
            print("\n-- CARI BUKU --")
            kategori = input("Cari berdasarkan (judul/penulis/isbn): ").strip().lower()
            if kategori not in ['judul', 'penulis', 'isbn']:
                print("[Error] Kategori tidak valid.")
                continue
                
            kata_kunci = input(f"Masukkan {kategori} yang dicari: ").strip()
            hasil_cari = perpustakaan.cari_buku(kata_kunci, kategori)
            
            print(f"\n--- Hasil Pencarian '{kata_kunci}' ---")
            if hasil_cari:
                for b in hasil_cari:
                    print(b)
            else:
                print("Buku tidak ditemukan.")

        elif pilihan == '4':
            print("\n-- FILTER BUKU BERDASARKAN GENRE --")
            genre_target = input("Masukkan genre yang dicari: ").strip()
            hasil_filter = perpustakaan.filter_buku_berdasarkan_genre(genre_target)
            
            print(f"\n--- Hasil Filter Genre: '{genre_target}' ---")
            if hasil_filter:
                for b in hasil_filter:
                    print(b)
            else:
                print("Tidak ada buku dengan genre tersebut.")

        elif pilihan == '5':
            print("\n-- HAPUS BUKU --")
            isbn_target = input("Masukkan ISBN buku yang akan dihapus: ").strip()
            perpustakaan.hapus_buku(isbn_target)

        elif pilihan == '0':
            print("\nTerima kasih telah menggunakan sistem manajemen perpustakaan. Sampai jumpa!")
            break

        else:
            print("\n[Error] Pilihan tidak valid, silakan masukkan angka 0-5.")

# Menjalankan aplikasi
if __name__ == "__main__":
    menu_utama()