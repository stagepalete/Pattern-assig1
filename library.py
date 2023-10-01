from prettytable import PrettyTable

class Library:
    _library = None

    class CLI:
        ...

    class User:
        def __init__(self, name, surname, age):
            self._name = name
            self._surname = surname
            self._age = age
            self._takenbooks = []
        
        def allBooks(self):
            table = PrettyTable()
            table.field_names = ['#', 'name', 'author']
            rows = []
            for id, book in enumerate(self._takenbooks):
                row = [id, book.name(), book.author()]
                rows.append(row)

            table.add_rows(rows)
            print(f'Books\n{table}')

        def takebook(self, book):
            if book._status == 'Available':
                book.took()
                self._takenbooks.append(book)
                print(f'(!) {self.__str__()} took {book}')
            else:
                print(f'(!) {self.__str__()} tried to take {book}, but it is not available')

        def returnbook(self, book):
            if book in self._takenbooks:
                book.tooknt()
                self._takenbooks.remove(book)
            else:
                print(f'(!) {self.__str__()} did not take {book}')

        def __str__(self):
            return f'{self._name} {self._surname}'

    class Book:
        def __init__(self, name, author):
            self._name = name
            self._author = author
            self._status = 'Available'


        def took(self):
            self._status = 'Not available'
            print(f'(!) {self.__str__()} taken')

        def tooknt(self):
            self._status = 'Available'
            print(f'(!) {self.__str__()} returned')

        def status(self):
            return self._status

        def name(self):
            return self._name

        def author(self):
            return self._author

        def __str__(self):
            return f'{self._author}, {self._name}'
        

    def __new__(cls):
        if cls._library is None:
            cls._library = super(Library, cls).__new__(cls)
            cls._library.books = []
            cls._library.users = []
        return cls._library

    def allBooks(self):
        table = PrettyTable()
        table.field_names = ['#', 'name', 'author', 'status']

        rows = []
        for id, book in enumerate(self.books):
            row = [id, book.name(), book.author(), book.status()]
            rows.append(row)

        table.add_rows(rows)
        print(f'Books\n{table}')


    def allUsers(self):
        table = PrettyTable()
        table.field_names = ['#', 'user']
        rows = []
        for id, user in enumerate(self.users):
            row = [id, user]
            rows.append(row)
        table.add_rows(rows)
        print(f'Users\n{table}')
        
    def registerUser(self, user):
        self.users.append(user)
        print(f'(!) Added new client of Library - {user}')

    def addBook(self, book):
        self.books.append(book)
        print(f'(!) Added new book to Library - {book}')

    def tookBook(self, user, book):
        user.takebook(book)

    def returnBook(self, user, book):
        user.returnbook(book)





def main():
    library = Library()

    book1 = library.Book("451 Fahrenheit", "Martin Monroh")
    book2 = library.Book("To Kill a Mockingbird", "Harper Lee")
    user1 = library.User('Yedige','Mazhit', 19)
    library.addBook(book1)
    library.addBook(book2)
    library.registerUser(user1)


    library.allBooks()
    library.allUsers()

    user1.takebook(book1)
    library.allBooks()
    user1.returnbook(book1)
    library.allBooks()




if __name__ == '__main__':
    main()

