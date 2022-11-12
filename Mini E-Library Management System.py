class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("Books present in this library are: ")
        for book in self.books: 
            print(" *" + book)
    
    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}. Please keep it safe and return it within 30 days")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry, This book is either not available or has already been issued to someone else. Please wait until the book is available")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning this book! Hope you enjoyed reading it. Have a great day!")

class Student: 
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book you want to return: ")
        return self.book
         

if _name_ == "_main_":
    centraLibrary = Library([ "JavaScript Book",
                                        "PHP",
                                        "C++",
                                        "Python",
                                        "Java",
                                        "In Search of Lost of Time by Marcel Proust          ",
                                        "Ulysses by James Joyce",
                                        "Don Quixote by Miguel de Cervantes",
                                        "One Hundred of Solitude by Gabriel Garcia MArquez",
                                        "The Great Gatsby by F. Scott Fitzgerald",
                                        "Moby Dick by Herman Melville",
                                        "War and Peace by Leo Tolstoy",
                                        "Hamlet by William Shakespear ",
                                        "The Odyssey by Homer",
                                        "Madame Bovary by Gustave Flubert",])
    student = Student()
    
    while(True):
        welcomeMsg = '''\n====== Welcome to Library  System======
                User:
            1. Admin
            2. Students
            
        Please choose an option:
        1. List all the books
        2. Request a book
        3. Return a book
        4. Exit the Library
        '''
        print(welcomeMsg)
        a = int(input("Enter a choice: "))
        if a == 1:
            centraLibrary.displayAvailableBooks()
        elif a == 2:
            centraLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centraLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("Thanks for choosing our Library.")
            exit()
        else:
            print("Invalid Choice!")