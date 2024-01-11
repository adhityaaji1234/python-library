class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def display_books(self):
        if not self.books:
            print("The library has no books.")
        else:
            print("Books available in the library:")
            for book in self.books:
                status = "Available" if not book.is_borrowed else "Borrowed"
                print(f"Title: {book.title} | Author: {book.author} | Genre: {book.genre} | Status: {status}")

class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self.is_borrowed = False

    def borrow_book(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"Book '{self.title}' by {self.author} is borrowed.")
        else:
            print(f"Book '{self.title}' is already borrowed.")
        self.display_status()

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"Book '{self.title}' by {self.author} is returned.")
        else:
            print(f"Book '{self.title}' is not borrowed.")
        self.display_status()

    def display_status(self):
        status = "Borrowed" if self.is_borrowed else "Returned" if self.is_borrowed == False else "Available"
        print(f"Title: {self.title} | Author: {self.author} | Genre: {self.genre} | Status: {status}")


if __name__ == "__main__":
    library = Library()

    num_books = int(input("Berapa banyak judul buku yang ingin Anda tambahkan? "))
    for _ in range(num_books):
        title = input("Masukkan judul buku: ")
        author = input("Masukkan penulis buku: ")
        genre = input("Masukkan genre buku: ")
        new_book = Book(title, author, genre)
        library.add_book(new_book)

    library.display_books()

    while True:
        action_choice = input("Apakah Anda ingin meminjam, mengembalikan, atau keluar? (pinjam/kembali/keluar): ")
        
        if action_choice.lower() == "pinjam":
            book_to_borrow = input("Masukkan judul buku yang ingin dipinjam: ")
            for book in library.books:
                if book.title.lower() == book_to_borrow.lower():
                    book.borrow_book()
                    break
            else:
                print("Buku tidak ditemukan di perpustakaan.")
            continue

        elif action_choice.lower() == "kembali":
            book_to_return = input("Masukkan judul buku yang ingin dikembalikan: ")
            for book in library.books:
                if book.title.lower() == book_to_return.lower():
                    book.return_book()
                    break
            else:
                print("Buku tidak ditemukan di perpustakaan.")
            continue

        elif action_choice.lower() == "keluar":
            while True:
                exit_choice = input("Apakah Anda ingin keluar dari perpustakaan? (ya/tidak): ")
                if exit_choice.lower() == "ya":
                    print("Terima kasih telah mengunjungi perpustakaan!")
                    break
                elif exit_choice.lower() == "tidak":
                    break
            if exit_choice.lower() == "tidak":
                continue
            else:
                break

    
    

    








            
