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

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
class UserExists(Exception):
    pass

class UserDatabase:
    def __init__(self):
        self.database = {}
    
    def add_user(self, user):
        if user.username in self.database:
            raise UserExists
        self.database[user.username] = user

class MainApp:
    def __init__(self):
        self.database = {}
        self.logged_in_user = None

    def show_main_menu(self):
        while True:
            print('1 - Register')
            print('2 - Login')
            print('3 - Logout')
            print('4 - Change Password')
            print('5 - Check Info')
            print('6 - Exit')

            _ = ""
            try: _ = int(input('What do you want to do? '))
            except ValueError:
              print('Incorrect Entry!')
            
            if _ == 6:
                print('Goodbye!')
                MainApp.exit

            if _ == 1:
                self.register()
            
            elif _ == 2:
                self.login()
                
            elif _ == 3:
                self.logout()
                
            elif _ == 4:
                self.change_password()

            elif _ == 5:
                self.checkInfo()

            else:
                print('Incorrect entry!, Try again?')

    def register(self):
        username = input('Username:')

        if username in self.database:
            print('This username is already taken.')
            return

        password = input('Password:')

        self.database[username] = User(username, password)
    
    def login(self):
        username = input('Username:')

        if username not in self.database:
            print('Username or password is not valid.')
            return

        password = input('Password:')

        user = self.database[username]

        if user.password != password:
            print('Username or password is not valid.')
            return
        
        self.logged_in_user = user
        print('Logged in.')
        libMenu()
    
    def logout(self):
        if not self.logged_in_user:
            print('You are not logged in.')
            return
        
        self.logged_in_user = None
        print('Logged out.')

def run_app():
    app = MainApp()
    app.show_main_menu()

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
  print("\n================================================")
  print("\n\n================================================")
  print("     [1] LIBRARIAN")
  print("     [2] STUDENT")
  print("     [3] EXIT")
  print("\n\n================================================")
  menuChoice = int(input("\n\nEnter your choice number: "))
  if menuChoice == 1:
   print("\n================================================")
   print("\n\n             LIBRARIAN LOGIN ")
   print("\n\n================================================")
#libusern = str(input("USERNAME: "))
#libpass = str(input("PASSWORD: "))
#if libusern == "libadmin" and libpass == "libpass":
   run_app()
  if menuChoice == 2:
     print("\n================================================")
     print("\n\n            STUDENT LOGIN ")
     print("\n\n================================================")
     stdntUsern = str(input("USERNAME: "))
     stdntPass = str(input("PASSWORD: "))
     if stdntUsern == "stdntusern" and stdntPass == "stdntpass":
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
                    input()
                    accMenu()

                elif stdntChoice == 2:
                   centraLibrary.borrowBook(student.requestBook())
                   accMenu()

                elif stdntChoice == 3:
                   centraLibrary.returnBook(student.returnBook())
                   accMenu()

                elif stdntChoice == 4:
                   accMenu()
     else: 
       print("\n\n    Invalid Login Details! \n    Press any key to try again.. ")
       input()
       accMenu()

def libMenu():
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
  input()
  return accMenu()
#elif libChoice == 2:
 #centraLibrary.addBook(self.newBook())
 elif libChoice == 3:
   accMenu()
 elif libusern != "libadmin" and libpass != "libpass":
    print("\n\n    Invalid Login Details! \n    Press any key to try again.. ")
input()
accMenu()
        


  

''' def libMenu():
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
#elif libChoice == 2:
 #centraLibrary.addBook(self.newBook())
 elif libChoice == 3:
   accMenu()
 elif libusern != "libadmin" and libpass != "libpass":
    print("\n\n    Invalid Login Details! \n    Press any key to try again.. ")
input()
accMenu() '''
a

