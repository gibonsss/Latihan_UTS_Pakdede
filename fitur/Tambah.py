# Inisialisasi daftar buku (database sederhana)
koleksi_buku = []

def tambah_buku(judul, penulis, tahun, isbn):
    """Fungsi untuk menambahkan buku baru ke dalam koleksi perpustakaan."""
    
    # Validasi apakah ISBN sudah ada untuk menghindari duplikasi
    for buku in koleksi_buku:
        if buku['isbn'] == isbn:
            print(f"Gagal: Buku dengan ISBN {isbn} sudah terdaftar di sistem.")
            return False
            
    # Membuat dictionary untuk buku baru
    buku_baru = {
        'judul': judul,
        'penulis': penulis,
        'tahun': tahun,
        'isbn': isbn
    }
    
    # Menambahkan buku ke dalam koleksi
    koleksi_buku.append(buku_baru)
    print(f"Sukses: Buku '{judul}' karya {penulis} berhasil ditambahkan!")
    return True

def tampilkan_semua_buku():
    """Fungsi untuk menampilkan semua buku di perpustakaan."""
    print("\n--- Daftar Buku Perpustakaan ---")
    if not koleksi_buku:
        print("Koleksi masih kosong.")
        return
        
    for i, buku in enumerate(koleksi_buku, 1):
        print(f"{i}. {buku['judul']} | Penulis: {buku['penulis']} | Tahun: {buku['tahun']} | ISBN: {buku['isbn']}")
    print("--------------------------------\n")

# --- Contoh Penggunaan Program ---

# Menambahkan buku baru
tambah_buku("Bumi Manusia", "Pramoedya Ananta Toer", 1980, "978-979-97312-3-4")
tambah_buku("Laskar Pelangi", "Andrea Hirata", 2005, "978-979-3062-79-2")

# Mencoba menambahkan buku dengan ISBN yang sama (akan gagal)
tambah_buku("Buku Palsu", "Penulis Anonim", 2026, "978-979-97312-3-4")

# Menampilkan hasil
tampilkan_semua_buku()