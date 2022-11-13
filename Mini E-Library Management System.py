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

    def addBook(self, newBook):
        newBook = str(input("Enter Bookname: "))
        self.addBook = newBook
        self.books.append(newBook)

class Student: 
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book you want to return: ")
        return self.book
         

if __name__ == "__main__":
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

import os
clear = lambda: os.system('cls')						
print("\n\n\n\n")
print("\t\t\t *======================================================*\n")
print("\t\t         *|\t                                        \t|*\n")
print("\t\t         *|\t                                        \t|*\n")
print("\t\t         *|\t                                        \t|*\n")
print("\t\t         *|\t\t      MINI E-LIBRARY\t\t\t|*\n")
print("\t\t         *|\t      When in doubt go to the Libray.\t\t|*\n")
print("\t\t         *|\t                                        \t|*\n")
print("\t\t         *|\t                                        \t|*\n")
print("\t\t         *|\t                                        \t|*\n")
print("\t\t         *======================================================*\n")
print("\n\t\t         Press Enter to Continue          ")
input()


def accMenu(): 
    import os
    clear = lambda: os.system('cls')
print("\n================================================")
print("\n\n                ACCOUNTS MENU")
print("\n\n================================================")
print("     [1] LIBRARIAN")
print("     [2] STUDENT")
print("     [3] EXIT")
print("\n\n================================================")
            
accMenu()

account:accMenu()
menuChoice = int(input("\n\nEnter your choice number: "))
import os
clear = lambda: os.system('cls')
clear
if menuChoice == 1:
 libLogin:clear = lambda: os.system('cls')
 clear
print("\n================================================")
print("\n\n             LIBRARIAN LOGIN ")
print("\n\n================================================")
libusern = str(input("USERNAME: "))
libpass = str(input("PASSWORD: "))
if libusern == "libadmin" and libpass == "libpass":
  	libMenu:clear = lambda: os.system('cls')
clear
print("\n================================================")
print("\n\n               LIBRARIAN MENU ")
print("\n\n================================================")
print("\n     [1] VIEW BOOKS LIST")
print("\n     [2] ADD BOOKS")
print("\n     [3] GO BACK TO ACCOUNTS MENU")
print("\n\n================================================")
libChoice = int(input("Enter your choice: "))
if libChoice == 1:
 centraLibrary.displayAvailableBooks()
elif libChoice == 2:
 centraLibrary.addBook(self.newBook())
elif libChoice == 3:
    accMenu()
elif libusern != "libadmin" and libpass != "libpass":
    print("\n\n    Invalid Login Details! \n    Press any key to try again.. ")
input()
accMenu()

if menuChoice == 2:
     stdntLogin:clear = lambda: os.system('cls')
     clear
     print("\n================================================")
print("\n\n            STUDENT LOGIN ")
print("\n\n================================================")
stdntUsern = str(input("USERNAME: "))
stdntPass = str(input("PASSWORD: "))
if stdntUsern == "stdntusern" and stdntPass == "stdntpass":
  	stdntMenu:clear = lambda: os.system('cls')
clear
print("\n================================================")
print("\n\n               STUDENT MENU ")
print("\n\n================================================")
print("\n     [1] VIEW BOOKS LIST")
print("\n     [2] BORROW BOOK")
print("\n     [3] RETURN BOOOK")
print("\n     [4] GO BACK TO ACCOUNTS MENU")
print("\n\n================================================")
stdntChoice = int(input("Enter your choice: "))
if stdntChoice == 1:
 centraLibrary.displayAvailableBooks()
elif stdntChoice == 2:
 centraLibrary.borrowBook(student.requestBook())
elif stdntChoice == 3:
    centraLibrary.returnBook(student.returnBook())
elif stdntChoice == 4:
   accMenu() 
elif stdntUsern != "stdntusern" and stdntPass != "stdntpass":
    print("\n\n    Invalid Login Details! \n    Press any key to try again.. ")
input()
accMenu()



#elif choice == 2:
 #centraLibrary.borrowBook(student.requestBook())
#elif a == 3:
 #
 # 
 # 
 #centraLibrary.returnBook(student.returnBook())
        
#a = int(input("Enter a choice: "))
#if a == 1:
 #centraLibrary.displayAvailableBooks()
#elif a == 2:
 #centraLibrary.borrowBook(student.requestBook())
#elif a == 3:
 #centraLibrary.returnBook(student.returnBook())
#elif a == 4:
            #print("Thanks for choosing our Library.")
           # exit()
#else:
      #      print("Invalid Choice!")