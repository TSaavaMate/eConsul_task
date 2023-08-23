from book import Book

books = [
    Book("The big four", "Agatha Christie", "detective", 4.5, 278),
    Book("Pride and Prejudice", "Jane Austen", "romance", 4.6, 432),
    Book("The Great Gatsby", "F. Scott Fitzgerald", "classic", 4.0, 180),
    Book("The Lord of the Rings", "J.R.R. Tolkien", "fantasy", 4.5, 1178),
    Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", "fantasy", 4.8, 320),
    Book("Brave New World", "Aldous Huxley", "dystopian", 4.1, 288),
    Book("The Hobbit", "J.R.R. Tolkien", "fantasy", 4.7, 310)
]
# In Python, we have lambda which is a  way  to create short, anonymous functions.
# They are used for short operations or methods that are used only once.
# It has syntax like lambda arguments:action  and this represents whole function body
# Mostly lambda is used to filter elements , sort them by some condition or map some objects into new objects according
# Some condition like example below

book_titles = map(lambda book: book.title, books)

filtered_books = filter(lambda book: book.rating > 4.3, books)

sorted_books = sorted(books, key=lambda book: book.rating, reverse=True)

print(list(book_titles))
print(list(filtered_books))
print(list(sorted_books))
