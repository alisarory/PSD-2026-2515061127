class HashMap:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        total = 0
        for char in key:
            total += ord(char)
        return total % self.size

    def insert(self, key, value):
        index = self.hash_function(key)

        for data in self.table[index]:
            if data[0] == key:
                data[1] = value
                print("Data berhasil diupdate")
                return

        self.table[index].append([key, value])
        print("Data berhasil ditambahkan")

    def search(self, key):
        index = self.hash_function(key)

        for data in self.table[index]:
            if data[0] == key:
                return data[1]

        return None

    def delete(self, key):
        index = self.hash_function(key)

        for data in self.table[index]:
            if data[0] == key:
                self.table[index].remove(data)
                print("Data berhasil dihapus")
                return

        print("Data tidak ditemukan")

    def display(self):
        print("\nIsi Hash Map:")
        for i in range(self.size):
            print(f"Index {i}: {self.table[i]}")


def main():
    hm = HashMap()

    while True:
        print("\n=== PROGRAM HASH MAP ===")
        print("1. Insert Data")
        print("2. Search Data")
        print("3. Delete Data")
        print("4. Display Hash Map")
        print("5. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            key = input("Masukkan key: ")
            value = input("Masukkan value: ")
            hm.insert(key, value)

        elif pilihan == "2":
            key = input("Masukkan key yang dicari: ")
            hasil = hm.search(key)

            if hasil is not None:
                print("Data ditemukan:", hasil)
            else:
                print("Data tidak ditemukan")

        elif pilihan == "3":
            key = input("Masukkan key yang ingin dihapus: ")
            hm.delete(key)

        elif pilihan == "4":
            hm.display()

        elif pilihan == "5":
            print("Program selesai")
            break

        else:
            print("Pilihan tidak valid")


if __name__ == "__main__":
    main())
