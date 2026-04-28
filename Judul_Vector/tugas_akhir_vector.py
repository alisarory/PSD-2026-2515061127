vector = [1, 4, 6, 7, 8]

while True:
    print("\n=== Vector Operations ===")
    print("1. Add element")
    print("2. Show vector")
    print("3. Sum elements")
    print("4. Search element")
    print("5. Delete element")
    print("6. Find max and min")
    print("7. Exit")

    choice = input("Choose menu: ")

    if choice == "1":
        value = int(input("Enter number: "))
        vector.append(value)
        print("Element added successfully.")

    elif choice == "2":
        print("Vector:", vector)

    elif choice == "3":
        print("Sum of elements:", sum(vector))

    elif choice == "4":
        value = int(input("Enter number to search: "))
        if value in vector:
            print(value, "found in vector.")
        else:
            print(value, "not found.")

    elif choice == "5":
        value = int(input("Enter number to delete: "))
        if value in vector:
            vector.remove(value)
            print("Element deleted.")
        else:
            print("Element not found.")

    elif choice == "6":
        if len(vector) > 0:
            print("Max value:", max(vector))
            print("Min value:", min(vector))
        else:
            print("Vector is empty.")

    elif choice == "7":
        print("Program finished.")
        break

    else:
        print("Invalid choice.")
