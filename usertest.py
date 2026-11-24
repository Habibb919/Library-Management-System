from user import User

user1 = User("Aysel", 1)
user1.display_info()

user1.borrowed_books.append("978-0451524935")
user1.display_info()