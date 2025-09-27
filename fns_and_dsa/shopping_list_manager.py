def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add = input("Enter an item to add to the list: ")
            add = shopping_list.append(add)
        elif choice == '2':
            rem = input("Enter an item to remove from the list: ")
            if rem not in shopping_list:
                print(f"{rem} not found in the list")
            else:
                rem = shopping_list.remove(rem)
        elif choice == '3':
            print(shopping_list)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
