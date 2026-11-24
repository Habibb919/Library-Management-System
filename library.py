import json
import os
from book import Book
from user import User


class Library:
    def __init__(self, data_file="data.json"):
        self.data_file = data_file
        self.books = []
        self.users = []

    def add_book(self, title, author, isbn):
        for book in self.books:
            if book.isbn == isbn:
                print("Bu ISBN ilə kitab artıq mövcuddur.")
                return

        book = Book(title, author, isbn)
        self.books.append(book)
        print(f"'{title}' kitabı əlavə olundu.")

    def view_books(self):
        if not self.books:
            print("Kitabxanada hələ kitab yoxdur.")
            return

        for book in self.books:
            book.display_info()

    def search_book(self, title):
        found = []
        for book in self.books:
            if title.lower() in book.title.lower():
                found.append(book)

        if not found:
            print(f"'{title}' adına uyğun kitab tapılmadı.")
            return

        for book in found:
            book.display_info()

    def register_user(self, name, user_id):
        for user in self.users:
            if user.user_id == user_id:
                print("Bu ID ilə oxucu artıq qeydiyyatdan keçib.")
                return

        user = User(name, user_id)
        self.users.append(user)
        print(f"'{name}' adlı oxucu qeydiyyata alındı.")

    def find_book_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def find_user_by_id(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None

    def borrow_book(self, user_id, isbn):
        user = self.find_user_by_id(user_id)
        book = self.find_book_by_isbn(isbn)

        if user is None:
            print("Bu ID ilə oxucu tapılmadı.")
            return

        if book is None:
            print("Bu ISBN ilə kitab tapılmadı.")
            return

        if not book.is_available:
            print(f"'{book.title}' kitabı hazırda başqasında (götürülüb).")
            return

        book.is_available = False
        user.borrowed_books.append(isbn)
        print(f"'{book.title}' kitabı {user.name} tərəfindən götürüldü.")

    def return_book(self, user_id, isbn):
        user = self.find_user_by_id(user_id)
        book = self.find_book_by_isbn(isbn)

        if user is None:
            print("Bu ID ilə oxucu tapılmadı.")
            return

        if book is None:
            print("Bu ISBN ilə kitab tapılmadı.")
            return

        if isbn not in user.borrowed_books:
            print(f"{user.name} bu ISBN-li kitabı götürməyib.")
            return

        book.is_available = True
        user.borrowed_books.remove(isbn)
        print(f"'{book.title}' kitabı {user.name} tərəfindən qaytarıldı.")

    def view_borrowed_books(self):
        has_borrowed = False

        for user in self.users:
            if user.borrowed_books:
                has_borrowed = True
                print(f"\nOxucu: {user.name} (ID: {user.user_id})")
                for isbn in user.borrowed_books:
                    book = self.find_book_by_isbn(isbn)
                    if book is not None:
                        print(f"  - {book.title} ({book.author}) [ISBN: {isbn}]")
                    else:
                        print(f"  - Naməlum kitab [ISBN: {isbn}]")

        if not has_borrowed:
            print("Hazırda heç bir oxucu kitab götürməyib.")

    def save_data(self):
        data = {
            "books": [book.to_dict() for book in self.books],
            "users": [user.to_dict() for user in self.users],
        }

        with open(self.data_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        print(f"Məlumatlar '{self.data_file}' faylında yadda saxlanıldı.")

    def load_data(self):
        try:
            with open(self.data_file, "r", encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError:
            print(f"'{self.data_file}' faylı tapılmadı.")
            return
        except json.JSONDecodeError:
            print(f"'{self.data_file}' faylı pozulub və ya düzgün JSON formatında deyil.")
            return

        loaded_books = []
        for book_data in data.get("books", []):
            book = Book(
                book_data["title"],
                book_data["author"],
                book_data["isbn"],
            )
            book.is_available = book_data.get("is_available", True)
            loaded_books.append(book)

        loaded_users = []
        for user_data in data.get("users", []):
            user = User(
                user_data["name"],
                user_data["user_id"],
            )
            user.borrowed_books = list(user_data.get("borrowed_books", []))
            loaded_users.append(user)

        self.books = loaded_books
        self.users = loaded_users
        print("Məlumatlar yükləndi.")