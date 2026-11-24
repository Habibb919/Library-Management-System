from library import Library


def show_menu():
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Register User")
    print("5. Borrow Book")
    print("6. Return Book")
    print("7. View Borrowed Books")
    print("8. Save Data")
    print("9. Exit")


def get_int(prompt, error_message="ID rəqəm olmalıdır"):
    try:
        return int(input(prompt))
    except ValueError:
        print(error_message)
        return None


def main():
    library = Library()
    library.load_data()

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            isbn = input("ISBN: ")
            library.add_book(title, author, isbn)

        elif choice == "2":
            library.view_books()

        elif choice == "3":
            title = input("Search title: ")
            library.search_book(title)

        elif choice == "4":
            name = input("Name: ")
            user_id = get_int("User ID: ")
            if user_id is None:
                continue
            library.register_user(name, user_id)

        elif choice == "5":
            user_id = get_int("User ID: ")
            if user_id is None:
                continue
            isbn = input("ISBN: ")
            library.borrow_book(user_id, isbn)

        elif choice == "6":
            user_id = get_int("User ID: ")
            if user_id is None:
                continue
            isbn = input("ISBN: ")
            library.return_book(user_id, isbn)

        elif choice == "7":
            library.view_borrowed_books()

        elif choice == "8":
            library.save_data()

        elif choice == "9":
            save_choice = input("Save before exit? (y/n): ").strip().lower()
            if save_choice == "y":
                library.save_data()
            break

        else:
            print("Yanlış seçim, 1-9 arası rəqəm daxil edin.")


if __name__ == "__main__":
    main()