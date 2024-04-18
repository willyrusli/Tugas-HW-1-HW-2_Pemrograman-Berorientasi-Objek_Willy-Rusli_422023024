Class Buku:
    def _init_(self, id_buku, judul_buku, harga):
        self.id_buku = id_buku
        self.judul_buku = judul_buku
        self.harga = harga

class Inventory:
    def _init_(self):
        self.buku_list = []

    def tambah_buku(self, buku):
        self.buku_list.append(buku)
        print("Buku telah ditambahkan.")

    def tampilkan_buku(self):
      if self.buku_list:
        print("Daftar Buku:")
        for buku in self.buku_list:
          print(f"ID: {buku.id_buku}, Judul: {buku.judul_buku}, Harga: {buku.harga}")
      else:
          print("Tidak ada buku dalam inventori.")

    def cari_buku(self, id_buku):
        for buku in self.buku_list:
          if buku.id_buku == id_buku:
            return buku
        return None

    def update_buku(self, id_buku, judul_buku, harga):
        buku = self.cari_buku(id_buku)
        if buku:
            buku.judul_buku = judul_buku
            buku.harga = harga
            print("Buku telah diupdate.")
          else:
            print("Buku tidak ditemukan.")

    def hapus_buku(self, id_buku):
        buku = self.cari_buku(id_buku)
        if buku:
          self.buku_list.remove(buku)
          print("Buku telah dihapus.")
        else:
          print("Buku tidak ditemukan.")

def main():
    inventory = Inventory()

    while True:
        print("\nPilih operasi:")
        print("1. Tambah Buku")
        print("2. Tampilkan Buku")
        print("3. Update Buku")
        print("4. Hapus Buku")
        print("5. Keluar")
          pilihan = input("Masukkan pilihan (1/2/3/4/5): ")

        if pilihan == '1':
            id_buku = input("Masukkan ID Buku: ")
            judul_buku = input("Masukkan Judul Buku: ")
            harga = input("Masukkan Harga Buku: ")
            buku = Buku(id_buku, judul_buku, harga)
            inventory.tambah_buku(buku)
        elif pilihan == '2':
            inventory.tampilkan_buku()
        elif pilihan == '3':
            id_buku = input("Masukkan ID Buku yang ingin diupdate: ")
            judul_buku = input("Masukkan Judul Buku baru: ")
            harga = input("Masukkan Harga Buku baru: ")
            inventory.update_buku(id_buku, judul_buku, harga)
        elif pilihan == '4':
            id_buku = input("Masukkan ID Buku yang ingin dihapus: ")
            inventory.hapus_buku(id_buku)
        elif pilihan == '5':
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if _judul_ == "_main_":
    main() 
