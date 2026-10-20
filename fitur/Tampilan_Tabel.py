"""Fungsi tampilan yang dipakai bersama (F2, F3 judul, F5)."""


def _potong(teks, panjang):
    """Memotong teks yang melebihi lebar kolom agar tabel tetap rapi."""
    teks = str(teks)
    if len(teks) > panjang:
        return teks[:panjang - 3] + "..."
    return teks


def cetak_tabel(daftar_buku):
    """Mencetak tabel dari list buku (list of dict)."""
    garis = "-" * 100
    print(garis)
    print(f"{'No':<4}{'Kode':<9}{'Judul':<28}{'Pengarang':<20}"
          f"{'Genre':<16}{'Tahun':<7}Status")
    print(garis)
    for no, b in enumerate(daftar_buku, start=1):
        status = f"[{b['status'].upper()}]"
        print(f"{no:<4}{_potong(b['kode_buku'], 8):<9}"
              f"{_potong(b['judul'], 27):<28}"
              f"{_potong(b['pengarang'], 19):<20}"
              f"{_potong(b['genre'], 15):<16}"
              f"{b['tahun_terbit']:<7}{status}")
    print(garis)
