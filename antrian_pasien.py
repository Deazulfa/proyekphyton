import os


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


antrian = Queue()

while True:
    print("===== Sistem Antrian Pendaftaran Pasien =====")
    print("Antrian saat ini:", antrian.items)
    print("=============================================")
    print("1. Tambah Antrian")
    print("2. Panggil Antrian")
    print("3. Lihat Jumlah Antrian")
    print("4. Keluar")
    choice = int(input("Masukkan pilihan anda: "))

    if choice == 1:
        name = input("Masukkan nama pasien: ")
        antrian.enqueue(name)
        os.system("cls")
        print("Pasien", name, "telah ditambahkan ke dalam antrian!\n\n")
    elif choice == 2:
        if antrian.is_empty():
            os.system("cls")
            print("Antrian kosong")
        else:
            nama = antrian.dequeue()
            os.system("cls")
            print("Pasien", nama, "dipanggil!\n\n")
    elif choice == 3:
        os.system("cls")
        print("Jumlah antrian saat ini:", antrian.size())
    elif choice == 4:
        break
    else:
        print("Pilihan tidak tersedia")

os.system("cls")

print("Terima kasih telah menggunakan program ini")
