from collections import deque

class StackArray:
    def __init__(self, max_size=100):
        self.MAX = max_size
        self.st = [None] * self.MAX
        self.top_idx = -1

    def is_empty(self):
        return self.top_idx == -1

    def is_full(self):
        return self.top_idx == self.MAX - 1

    def push(self, x):
        if self.is_full():
            print("Stack penuh")
            return
        self.top_idx += 1
        self.st[self.top_idx] = x
        print(f"Push {x} berhasil")

    def pop(self):
        if self.is_empty():
            print("Stack kosong")
            return
        print(f"Pop {self.st[self.top_idx]} berhasil")
        self.top_idx -= 1

    def peek(self):
        if self.is_empty():
            print("Stack kosong")
            return
        print(f"Elemen teratas: {self.st[self.top_idx]}")

    def display(self):
        if self.is_empty():
            print("Stack kosong")
            return
        print("Isi stack (atas ke bawah): ", end="")
        for i in range(self.top_idx, -1, -1):
            print(self.st[i], end=" ")
        print()


def stack_menu():
    stack = StackArray()

    while True:
        print("\n=== MENU STACK ===")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display")
        print("5. Kembali")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            data = input("Masukkan data: ")
            stack.push(data)
        elif pilihan == "2":
            stack.pop()
        elif pilihan == "3":
            stack.peek()
        elif pilihan == "4":
            stack.display()
        elif pilihan == "5":
            break
        else:
            print("Pilihan tidak valid")


def queue_menu():
    queue = deque()

    while True:
        print("\n=== MENU QUEUE ===")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Front")
        print("4. Display")
        print("5. Kembali")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            data = input("Masukkan data: ")
            queue.append(data)
            print(f"Enqueue {data} berhasil")

        elif pilihan == "2":
            if len(queue) == 0:
                print("Queue kosong")
            else:
                data = queue.popleft()
                print(f"Dequeue {data} berhasil")

        elif pilihan == "3":
            if len(queue) == 0:
                print("Queue kosong")
            else:
                print(f"Elemen terdepan: {queue[0]}")

        elif pilihan == "4":
            if len(queue) == 0:
                print("Queue kosong")
            else:
                print("Isi queue (depan ke belakang):", list(queue))

        elif pilihan == "5":
            break
        else:
            print("Pilihan tidak valid")


def main():
    while True:
        print("\n=== PROGRAM STACK DAN QUEUE ===")
        print("1. Stack")
        print("2. Queue")
        print("3. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            stack_menu()
        elif pilihan == "2":
            queue_menu()
        elif pilihan == "3":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid")


if __name__ == "__main__":
    main()
