from book import Book

book1 = Book("1984", "George Orwell", "978-0451524935")
book1.display_info()

book1.is_available = False
book1.display_info()
