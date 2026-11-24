from library import Library

lib = Library()

print("=== 1. Boş kitabxana ===")
lib.view_books()

print("\n=== 2. Kitab əlavə etmə ===")
lib.add_book("1984", "George Orwell", "111")
lib.add_book("Animal Farm", "George Orwell", "222")
lib.add_book("1984", "George Orwell", "111")

print("\n=== 3. Bütün kitablar ===")
lib.view_books()

print("\n=== 4. Axtarış ===")
lib.search_book("1984")
lib.search_book("orwell")
lib.search_book("harry")

print("\n=== 5. Oxucu qeydiyyatı ===")
lib.register_user("Aysel", 1)
lib.register_user("Elvin", 2)
lib.register_user("Aysel", 1)

print("\n=== 6. Kitab götürmə ===")
lib.borrow_book(1, "111")
lib.borrow_book(2, "111")
lib.borrow_book(5, "111")
lib.borrow_book(1, "999")

print("\n=== 7. Götürülmüş kitablar ===")
lib.view_borrowed_books()

print("\n=== 8. Status yoxlaması ===")
lib.view_books()

print("\n=== 9. Kitab qaytarma ===")
lib.return_book(2, "111")
lib.return_book(1, "111")
lib.view_books()
lib.view_borrowed_books()

