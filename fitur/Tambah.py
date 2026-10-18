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

