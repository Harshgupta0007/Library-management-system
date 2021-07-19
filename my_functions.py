from book import Book
import json
def print_options():
    print("Select from the following options::")
    print("Press 1 to create a new book")
    print("Press 2 to save book locally")
    print("Press 3 to load books from disk")
    print("Press 4 to issue a book")
    print("Press 5 to return book")
    print("Press 6 to update book")
    print("Press 7 to show all books")
    print("Press 8 to find book by id")
    

def input_book_info():
    book_id = input("ID: ")
    name  = input('NAME: ')
    description = input("DESCRIPTION: ")
    isbn = input('ISBN: ')
    page_count = int(input("Page count: "))
    issued = input("ISSUED :: (y/Y for True anything else for False)")
    issued = (issued == 'y' or issued== 'Y')
    author = input("Author: ")
    year = int(input("Year: "))
    return {
            'id' : book_id,
            'name' : name,
            'description':description,
            'isbn' : isbn,
            'page_count' :page_count,
            'issued' : issued,
            'author' : author,
            'year' : year 
    }
def create_books():
    print("Enter book info")
    book_input = input_book_info()
    book = Book(book_input['id'], book_input['name'], book_input['description'], book_input['isbn'], book_input['page_count'], book_input['issued'], book_input['author'], book_input['year'])
    print(book.to_dict())
    return book

def save_books(books):
    json_books = []
    for book in books:
        json_books.append(book.to_dict())

    try:
        file  = open("books.dat","w")
        file.write(json.dumps(json_books, indent = 4))
        file.close()
    except:
        print("We had an error saving books")

def load_books():
    try:
        file = open("books.dat", "r")
        loaded_books = json.loads(file.read())
        books =[]
        for book in loaded_books:
            new_obj = Book(book['id'], book['name'], book['description'], book['isbn'], book['page_count'], book['issued'], book['author'], book['year'])
            books.append(new_obj)
        print("Successfully loaded")
        return books
    except:
        print("The file doesn't exist or an error occured during loading")

def find_books(books, book_id):
    for index, book in enumerate(books):
        if book.id == book_id:
            return index
    return None

def issue_book(books):
    id = input("Enter the id of the you are looking for::")
    index = find_books(books, id)
    if index != None:
        books[index].issued = True
        print("Book successfully issued.")
    else:
        print("We did not find the book you were looking for.")

def return_book(books):
    id = input("Enter the id of the you want to return::")
    index = find_books(books, id)
    
    if index != None:
        books[index].issued = False
        print("Book successfully returned.")
    else:
        print("We did not find the book you were looking for.")

def update_book(books):
    id = input("Enter the id of the book you want to update.")
    index = find_books(books, id)
    if index != None:
        new_book = create_books()
        old_book = books[index]
        books[index] = new_book
        del old_book
        print("Book successfully updated.")
    else: 
        print("We did not find the book you want to update.")

def show_all_books(books):
    for item in books:
        print(item.to_dict())

def show_books(books):
    id = input("Enter the id of the book you are looking for::")
    index = find_books(books, id)
    if index != None:
        print(books[index].to_dict())
    else:
        print("We could not find any book ")



    
