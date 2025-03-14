from helpers import (
    add_book,
    view_books,
    view_authors,
    view_categories,
    exit_program
)

def menu():
    print("Library CLI - Please select an option:")
    print("0. Exit")
    print("1. Add a Book")
    print("2. View Books")
    print("3. View Authors")
    print("4. View Categories")

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            view_authors()
        elif choice == "4":
            view_categories()
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
