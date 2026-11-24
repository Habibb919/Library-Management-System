class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.user_id}")
        print(f"Borrowed books: {len(self.borrowed_books)}")
        print("-" * 30)

    def to_dict(self):
        return {
            "name": self.name,
            "user_id": self.user_id,
            "borrowed_books": self.borrowed_books,
        }