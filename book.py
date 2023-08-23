class Book:
    def __init__(self,
                 title: str,
                 author: str,
                 genre: str,
                 rating: float,
                 number_of_pages: int):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__rating = rating
        self.__number_of_pages = number_of_pages

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def rating(self):
        return self.__rating

    @property
    def number_of_pages(self):
        return self.__number_of_pages

    @property
    def genre(self):
        return self.__genre

    def __str__(self) -> str:
        return f"Title: {self.title}\n" \
               f"Author: {self.author}\n" \
               f"Genre: {self.genre}\n" \
               f"Rating: {self.rating}\n" \
               f"Number of Pages: {self.number_of_pages}"

    __repr__ = __str__
