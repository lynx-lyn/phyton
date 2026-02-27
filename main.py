import backend
import logger
import urllib.request
import json


# ================== HANDLER MENU ==================

def tambah_item_handler():
    nama = input("Masukkan nama item: ")
    hasil = backend.tambah_item(nama)
    print(hasil)
    logger.tulis_log(f"Tambah item: {nama}")


def lihat_semua_handler():
    daftar = backend.semua_item()

    if not daftar:
        print("Daftar kosong.")
    else:
        print("\nDaftar Belanja:")
        for i, item in enumerate(daftar, start=1):
            print(f"{i}. {item}")

    logger.tulis_log("Lihat semua item")


def hapus_item_handler():
    try:
        no = int(input("Masukkan nomor item yang ingin dihapus: "))
        hasil = backend.hapus_item(no)
        print(hasil)
        logger.tulis_log(f"Hapus item nomor {no}")
    except ValueError:
        print("Input harus berupa angka.")


def edit_item_handler():
    try:
        no = int(input("Masukkan nomor item yang ingin diedit: "))
        nama_baru = input("Masukkan nama baru: ")
        hasil = backend.edit_item(no, nama_baru)
        print(hasil)
        logger.tulis_log(f"Edit item nomor {no} jadi {nama_baru}")
    except ValueError:
        print("Input harus berupa angka.")


def cari_item_handler():
    kata = input("Masukkan kata kunci pencarian: ")
    hasil = backend.cari_item(kata)

    if not hasil:
        print("Item tidak ditemukan.")
    else:
        print("Hasil pencarian:")
        for item in hasil:
            print("-", item)

    logger.tulis_log(f"Cari item: {kata}")


def hitung_total_handler():
    total = backend.hitung_total_item()
    print(f"Total item: {total}")
    logger.tulis_log("Hitung total item")


# ================== MENU ==================

def tampilkan_menu():
    print("\n=== APLIKASI DAFTAR BELANJA ===")
    print("1. Tambah item")
    print("2. Lihat semua item")
    print("3. Hapus item")
    print("4. Edit item")
    print("5. Cari item")
    print("6. Hitung jumlah item")
    print("7. Keluar")


def main():
    logger.tulis_log("Program dimulai")

    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-7): ")

        if pilihan == '1':
            tambah_item_handler()

        elif pilihan == '2':
            lihat_semua_handler()

        elif pilihan == '3':
            hapus_item_handler()

        elif pilihan == '4':
            edit_item_handler()

        elif pilihan == '5':
            cari_item_handler()

        elif pilihan == '6':
            hitung_total_handler()

        elif pilihan == '7':
            logger.tulis_log("Program selesai")
            print("Terima kasih dan sampai jumpa.")
            break

        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()