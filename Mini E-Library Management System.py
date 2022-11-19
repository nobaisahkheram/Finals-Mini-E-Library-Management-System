class Library:
    def __init__(self,Count_book,name):
        self.Count_book_dict = Count_book
        self.name = name
        self.bookdict = {}
        self.max_book_count = {}
        self.Count_book_dict

    #display books name and quantity currently present in the library   
    def displayAvailableBooks(self): 
        for books in self.Count_book_dict.items():
            print(books)

from datetime import date,timedelta
class User:
    def __init__(self,username,password,user,email,mobile,address):
        self.username = username
        self.password = password
        self.user = user
        self.email = email
        self.mobile = mobile
        self.address = address
        
class Member(User):
    def __init__(self,username,password,user,email,mobile,address,studentID):
        super().__init__(username,password,user,email,mobile,address)
        self.member_id = studentID
        self.max_book_count = {}
        self.bookdict = {}
        
    def Count_book(self,user,book):
        if user not in self.max_book_count:
            self.max_book_count[user] = [book]
            return len(self.max_book_count[user])
        else:
            if len(self.max_book_count[user])<=4:
                self.max_book_count[user].append(book)
                return len(self.max_book_count[user])
            else:
                return len(self.max_book_count[user])

class Librarian(User):
    def __init__(self,username,password,name,email,mobile,address,librarian_id):
        super().__init__(username,password,name,email,mobile,address)
        self.librarian_id = librarian_id

# add new_book in the library
    def add_book(self,library,book_name,quantity,author,rack,publish_date,pages):
        if quantity>0:
            if book_name in library.Count_book_dict.keys():
                library.Count_book_dict[book_name][0]+=quantity
            else:
                library.Count_book_dict.update({book_name:[quantity,author,rack,publish_date,pages]})
                print("\nBook has been succesfully added to the Library.")
        else:
            print("Error! Please enter positive integer for quantity of book.")
            
    def removeBook(self,library,book_name,quantity,author,rack,publish_date,pages):
        if quantity>0:
            if book_name in library.Count_book_dict.keys():
                if library.Count_book_dict[book_name][0]>=1:
                    library.Count_book_dict[book_name][0]-=quantity
                    if library.Count_book_dict[book_name][0] < 0:
                        library.Count_book_dict[book_name][0]+=quantity
                        print("\nError! Please enter correct quantity of book. We only have {} books of {}".format(library.Count_book_dict[book_name][0],book_name))
                    else:
                        print("\nGreat! Book has been succesfully removed.")
                else:
                    library.Count_book_dict.pop(book_name)
                    print("\nSorry, We don't have any books of {} in our Library".format(book_name))
            else:
                print("\nSorry, We don't have any books of {} in our Library".format(book_name))
        else:
            print("Error! Please enter positive integer for quantity of book.")
    
 # Issuing book to the user by cross verifying libray stock and user can issue only one book of particular subject
 # maintaining record         
    def borrowBook(self,library,book,user): 
            if book in library.Count_book_dict.keys():
                if library.Count_book_dict[book][0]>=1:
                    if (book,user) not in self.bookdict.keys():
                        if not self.check_previous_fine(book,user):
                            if self.Count_book(user,book)<=5:
                                lend_date = date.today()
                                returnDate = date.today()+timedelta(days = 10)
                                self.bookdict.update({(book,user):returnDate})
                                library.Count_book_dict[book][0] -= 1
                                for value in self.bookdict.keys():
                                    if value == (book,user):
                                        print("Great! {} book is issued to your name {} on {}. You can get the book".format(value[0],value[1],lend_date))
                                        print("You have 10 days to read the book. Please be advise to return the book on time otherwise P10/day fine will be charge.")
                                        print("Thank you for using Mini E-Library. Enjoy!")
                                        print(self.max_book_count)
                            else:
                                print("Sorry, you can issue maximum of 5 books only.")
                        else:
                            print("Sorry, you have to pay the fine first to be able to borrow the book.")
                    else:
                        print("This book was already issued to your name")
                else:
                    print("Sorry, this book is currently not available.")
            else:
                print("Sorry, This book is either not available or has already been issued to someone else. Please wait until the book is available")
     
    def check_previous_fine(self,book,user):
        current_date = date.today()
        for key,value in self.bookdict.items():
            if key[1]==user:
                returnDate = self.bookdict[key]
                if current_date > returnDate:
                    delay_days = (current_date - returnDate).days
                    total_fine = delay_days*10
                    return total_fine
                else:
                    return 0 

#return book,updating records and if delay then charge fine P10/day.            
    def returnBook(self,library,book,user):
        if (book,user)in self.bookdict.keys():
            returnDate =  self.bookdict[(book,user)]
            current_date = date.today()
            if current_date > returnDate:
                delay_days = (current_date - returnDate).days
                total_fine = delay_days*10
                print("Please pay fine, you have to pay {} pesos" .format(total_fine))
                print("We are redirecting you on Payment page. Please wait...")
                self.payment(library,book,user)
            else:
                self.max_book_count[user].remove(book)
                self.bookdict.pop((book,user))
                library.Count_book_dict[book][0] += 1
                print("\n")
                print("Book sucessfully returned. Thank you, Hope you enjoyed reading it. Have a great day!")
        else:
            print("\n")
            print("Please provide correct username and book name")
            
            
    def payment(self,library,book,user):
        print("For payment process. Enter your choice ")
        choice = input("Yes/No: ")
        if choice == "Yes":
            print("Your payment is now processing.")
            print("PLEASE WAIT...")
            input()
            print("PAYMENT SUCCESFUL")
            self.max_book_count[user].remove(book)
            self.bookdict.pop((book,user))
            library.Count_book_dict[book][0] += 1
        else:
            print("We are redirecting you to Homepage")
            
            
    def check_fine(self,library,book,user):
        if (book,user)in self.bookdict.keys():
            returnDate =  self.bookdict[(book,user)]
            current_date = date.today()
            if current_date > returnDate:
                delay_days = (current_date - returnDate).days
                total_fine = delay_days*10
                print("Please pay fine, you have to pay {} pesos." .format(total_fine))
                print("Do you want to pay fine now?")
                choice = input("Yes/No")
                if choice == "Yes":
                    self.payment(library,book,user)
                else:
                    print("We are redirecting you to Homepage.")
            else:
                print("You don't need to pay fine.")
        else:
            print("Enter correct information.")

class Users:
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

    def librarian_main_menu(self):
        while True:
            print("\n")
            print("\n     [1] REGISTER")
            print("\n     [2] LOG IN")
            print("\n     [3] LOG OUT")
            print("\n     [4] EXIT")
            print("\n\n================================================")

            _ = ""
            try: _ = int(input('What do you want to do? '))
            except ValueError:
              print('Incorrect Entry!')
            
            if _ == 4:
                print('Goodbye!')
                accMenu()

            if _ == 1:
                self.register()
            
            elif _ == 2:
                self.login()
                
            elif _ == 3:
                self.logout()

            else:
                print('Incorrect entry!, Try again?')

    def register(self):
        username = input('Username:')

        if username in self.database:
            print('This username is already taken.')
            return

        password = input('Password:')

        self.database[username] = Users(username, password)
    
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
    app.librarian_main_menu()

library = Library({"The Reader":[4,"Bernhard Schlink","120H",1995,218],
                   "The Secret Garden":[3,"Frances Hodgson Burnett","121H",1911,375],
                   "Number of Stars":[5,"Lois Lowry","122H",1989,137],
                   "In Search of Lost of Time":[8,"Marcel Proust","123H",2003,165],
                   "Ulysses": [5, "James Joyce", "124H", 2000, 188],
                   "Don Quixote": [10, "Miguel de Cervantes", "125H", 2018, 105],
                   "One Hundred of Solitude": [9, "Gabriel Garcia Marquez", "126H", 2020, 210],
                   "War and Peace": [9, "Leo Tolstoy", "127H", 2020, 200],
                   "Madame Bovary": [13, "Gustave Flubert", "128H", 2019, 250],
                   "The Alchemist": [10, "Paulo Coelho", "129H", 2018, 200],
                   "Atomic Habits": [10, "James Clear", "129H", 2020, 210],
                   "Thinking Fast And Slow": [10, "Daniel Kahneman", "130H", 2011, 150],
                   "The Four Agreements": [6, "Don Miguel Ruiz", "131H", 2019, 195],
                   "The 7 Habits Of Highly Effective People": [6, "Stephen R. Covey", "132H", 2019, 123],
                   "Best Self": [5, "Mike Bayer", "133H", 2018, 120]}, 
                   "Mini E-Library")

m1 = Member("@nobaisah_123","lyzel_9","jennyalmeniana","stephanieandal368@gmail.com","9982030680","NA","100")

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
                print("\n\n==========================================")
                print("\n     [1] VIEW BOOKS LIST")
                print("\n     [2] BORROW BOOK")
                print("\n     [3] RETURN BOOOK")
                print("\n     [4] GO BACK TO ACCOUNTS MENU")
                print("\n\n================================================")
                stdntChoice = int(input("Enter your choice: "))
                if stdntChoice == 1:
                    print("Books present in {} are: ".format(library.name))
                    library.displayAvailableBooks()
                    print("\n")
                    input()
                    accMenu()

                elif stdntChoice == 2:
                   book = input("Please enter the name of the book you wanted to borrow: ")
                   user = input("Please enter your Name: ")
                   m1.borrowBook(library,book,user)
                   print("\n")
                   accMenu()

                elif stdntChoice == 3:
                   book = input("please Enter the name of the book you want to return :")
                   user = input("please enter your name:")
                   m1.returnBook(library,book,user)
                   print("\n")
                   accMenu()

                elif stdntChoice == 4:
                   accMenu()

                else:
                    print("Error! Not a valid option")
                    input()
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
 print("\n     [3] DELETE BOOKS")
 print("\n     [4] GO BACK TO ACCOUNTS MENU")
 print("\n\n================================================")
 libChoice = int(input("Enter your choice: "))
 if libChoice == 1:
  print("Books present in {} are: ".format(library.name))
  library.displayAvailableBooks()
  print("\n")
  input()
  accMenu()

 elif libChoice == 2:
  username = input("USERNAME: ")
  password = input("PASSWORD: ")
  libr = Librarian(username,password,"librusern","librpass")
  print("\n")
  book_name = input("Enter the name of the book you want to add: ")
  quantity = int(input("Enter the quantity of book to add: "))
  author = input("Enter the name of Author: ")
  rack = input("Enter rack number: ")
  publish_date = input("Enter the publish date: ")
  pages = input("Enter the total number of page of book: ")
  libr.add_book(library,quantity,author,rack,publish_date,pages)
  print("\n")
  input()
  accMenu()

 elif libChoice == 3:
  username = input("USERNAME: ")
  password = input("PASSWORD: ")
  libr = Librarian(username,password,"librusern","librpass")
  print("\n")
  book_name = input("Enter the name of the book you want to remove: ")
  quantity = int(input("Enter quantity of book to remove: "))
  author = input("Enter the name of Author: ")
  rack = input("Enter rack number: ")
  publish_date = input("Enter the publish date: ")
  pages = input("Enter the total number of page: ")
  libr.removeBook(library,book_name,quantity,author,rack,publish_date,pages)
  print("\n")
  input()
  accMenu()

 elif libChoice == 4:
   input()
   accMenu()

accMenu()

