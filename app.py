import my_functions as mf
import os
books =[]
mf.print_options()
option = input()
while option != 'x' and option != 'X' :
    if option == '1':
        books.append(mf.create_books())
    elif option =='2':
        mf.save_books(books)
    elif option == '3':
        books = mf.load_books()
    elif option == '4':
        mf.issue_book(books)
    elif option == '5':
        mf.return_book(books)
    elif option == '6':
        mf.update_book(books)
    elif option == '7':
        mf.show_all_books(books)
    elif option == '8':
        mf.show_books(books)
    else:
        print("The given command dosn't exist")
    input("Enter a key to continue......")
    os.system("cls") 
    mf.print_options()
    option = input()

