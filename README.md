The cli.py script provides an interactive command-line interface for managing the library. The available operations are:

Add Category: Add a new category to the library.
Add Author: Add a new author to the library.
Add Book: Add a new book, linking it to an author and one or more categories.
Display Books: Display all books in the library along with their associated authors and categories.

Start the CLI by running:
python cli.py

Select the operation from the menu;
Library Management System
1. Add Category
2. Add Author
3. Add Book
4. Display Books
0. Exit

Database
Uses SQLite to store:

authors, categories, books, and a join table book_categories.
