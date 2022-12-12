from datetime import datetime


class LoginSystem:

  def doLogin():
    while True:
      print("\n================================================"+
                             "\n\t\t    LOGIN"+
             "\n================================================")
      username=input("\tUsername: ")    
      password=input("\tPassword: ")

      rec=""
      valid=False
      with open(LibrarySystem.USERS_FILE) as file:
        while (line:=file.readline().rstrip()):
          rec=line.split("|")
          if username==rec[1] and password==rec[2]:
            valid=True
            break

      if valid:  
        LibrarySystem.user["id"]=int(rec[0])
        LibrarySystem.user["user"]=rec[1]
        LibrarySystem.user["role"]=rec[3]
        print("\n\t\tAccess Granted. ")
        if LibrarySystem.user["role"]=="librarian":
          LibrarySystem.doLibrarianMenu()
        else:
          LibrarySystem.doStudentMenu()
      else:
        print("\n\t  ***** Access Denied *****")



class LibrarySystem:

  USER_ID_FILE="user_id.txt"
  USERS_FILE="users.txt"
  PROFILES_FILE="profiles.txt"
  BOOKS_FILE="books.txt"
  BORROWERS_FILE="borrowers.txt"

  finePerDay = 10.00

  user={}

  def doLibrarianMenu():
    while True:
      print(
        "\n================================================"+
        "\n\n               LIBRARIAN MENU "+
        "\n\n================================================"+
        "\n\n\t     [1] USER MANAGEMENT"+
        "\n\t     [2] BOOK MANAGEMENT"+
        "\n\t     [3] BORROWER MANAGEMENT"+
        "\n\t     [0] GO BACK TO LOGIN"+
        "\n\n================================================"
      )
      choice=int(input("Choice: "))
      if choice==0:
        break
      elif choice==1:
        LibrarySystem.doUserManagementMenu()
      elif choice==2:
        LibrarySystem.doBookManagementMenu()
      elif choice==3:
        LibrarySystem.doBorrowerManagementMenu()
      else:
        print("Invalid choice.")


                
  def doUserManagementMenu():
    while True:
      print(
        "\n================================================"+
        "\n\n             USER MANAGEMENT MENU "+
        "\n\n================================================"+
        "\n\n\t    [1] ADD USER"+
        "\n\t    [2] SEARCH USER"+
        "\n\t    [3] UPDATE USER"+
        "\n\t    [4] UPDATE USER PROFILE"+
        "\n\t    [5] DELETE USER"+
        "\n\t    [0] GO BACK TO LIBRARIAN MENU"+
        "\n\n================================================"
      )

      choice=int(input("Choice: "))
      if choice==0:
        break
      elif choice==1:
        LibrarySystem.doAddUser()
      elif choice==2:
        LibrarySystem.doSearchUser()
      elif choice==3:
        LibrarySystem.doUpdateUser()
      elif choice==4:
        LibrarySystem.doUpdateUserProfile()
      elif choice==5:
        LibrarySystem.doDeleteUser()
      else:
        print("Invalid choice.")



  def doAddUser():
    id=1
    role=""

    print("\nADD USER")
    username=input("Username: ")
    password=input("Password: ")

    while True:
      print(
        "\nRole:\n"+
        "1. Librarian\n"+
        "2. Student\n"
      )
      choice=int(input("Choice: "))
      if choice==1:
        role="Librarian"
        break
      elif choice==2:
        role="Student"
        break
      else:
        print("Invalid choice.") 

    with open(LibrarySystem.USER_ID_FILE) as file:
      id=int(file.readline())

    with open(LibrarySystem.USER_ID_FILE,"w") as file:
      file.write("{}\n".format(id+1))

    with open(LibrarySystem.USERS_FILE,"a") as file:
      file.write("{}|{}|{}|{}\n".format(id,username,password,role))

    print("\nRecord added.")



  def doSearchUser():
    print("\nSEARCH USER")
    search=input("\nSearch Text: ")
    print()
    words=search.split(" ")
    with open(LibrarySystem.USERS_FILE) as file:
      notFound=True
      while (line:=file.readline().rstrip()):
        found=False
        for word in words: 
          if line.lower().find(word.lower())!=-1:
            found=True
            notFound=False
            break
        if found:
          rec=line.split("|")
          print("ID: {}".format(rec[0]))
          print("Username: {}".format(rec[1]))
          print("Role: {}".format(rec[3]))
      if notFound:
        print("\nRecord not found.")   



  def doUpdateUser():
    print("\nUPDATE USER")
    id=int(input("User ID: "))
    print()

    with open(LibrarySystem.USERS_FILE) as file:      
      lines=[]
      found=False
      while (line:=file.readline().rstrip()):
        rec=line.split("|")
        if id==int(rec[0]):
          found=True

          print("ID: {}".format(rec[0]))
          print("Username: {}".format(rec[1]))
          print("Role: {}\n".format(rec[3]))

          username=input("Update Username: ")
          password=input("Update Password: ")

          role=""

          while True:
            print(
              "\nUpdate Role:\n"+
              "1. Librarian\n"+
              "2. Student\n"
            )
            choice=int(input("Choice: "))
            if choice==1:
              role="Librarian"
              break
            elif choice==2:
              role="Student"
              break
            else:
              print("Invalid choice.") 

          lines.append("{}|{}|{}|{}".format(id,username,password,role))
          
        else:
          lines.append(line)

      if found:
        with open(LibrarySystem.USERS_FILE,"w") as file:
          for line in lines:
            file.write("{}\n".format(line))
        print("\nRecord updated.")  
      else:
        print("\nRecord not found.")  



  def doUpdateUserProfile():
    print("\nUPDATE USER PROFILE\n")    
    id=int(input("User ID: "))
    print()

    with open(LibrarySystem.PROFILES_FILE) as file:      
      lines=[]
      found=False
      while (line:=file.readline().rstrip()):
        rec=line.split("|")
        if id==int(rec[0]):
          found=True

          print("Firstname: {}".format(rec[1]))
          print("Lastname: {}".format(rec[2]))
          print("Address: {}".format(rec[3]))
          print()

          firstname=input("Update Firstname: ")
          lastname=input("Update Lastname: ")
          address=input("Update Address: ")

          lines.append("{}|{}|{}|{}".format(id,firstname,lastname,address))
          
        else:
          lines.append(line)

      if found:
        with open(LibrarySystem.PROFILES_FILE,"w") as file:
          for line in lines:
            file.write("{}\n".format(line))
      else:
        print("ENTER PROFILE")  

        firstname=input("Firstname: ")
        lastname=input("Lastname: ")
        address=input("Address: ")

        with open(LibrarySystem.PROFILES_FILE,"a") as file:
          file.write("{}|{}|{}|{}\n".format(id,firstname,lastname,address))

      print("\nRecord updated.")  



  def doDeleteUser():
    print("\nDELETE USER")
    id=int(input("User ID: "))
    print()

    with open(LibrarySystem.USERS_FILE) as file:
      lines=[]
      found=False
      while (line:=file.readline().rstrip()):
        rec=line.split("|")
        if id==int(rec[0]):
          found=True
        else:
          lines.append(line)

      if found:
        with open(LibrarySystem.USERS_FILE,"w") as file:
          for line in lines:
            file.write("{}\n".format(line))
        print("\nRecord is deleted.")
      else:
        print("\nRecord not found.")  
      
      
  def doBookManagementMenu():
    while True:
      print(
        "\n================================================"+
        "\n\n             BOOK MANAGEMENT MENU\n"+
        "\n================================================"+
        "\n\n\t    [1] BOOK LIST"+
        "\n\t    [2] ADD BOOK"+
        "\n\t    [3] SEARCH BOOK"+
        "\n\t    [4] UPDATE BOOK"+
        "\n\t    [5] DELETE BOOK"+
        "\n\t    [0] GO BACK TO LIBRARIAN MENU"+
        "\n\n================================================"
      )
      choice=int(input("Choice: "))
      if choice==0:
        break
      elif choice==1:
        LibrarySystem.doListBooks()
      elif choice==2:
        LibrarySystem.doAddBook()
      elif choice==3:
        LibrarySystem.doSearchBook()
      elif choice==4:
        LibrarySystem.doUpdateBook()
      elif choice==5:
        LibrarySystem.doDeleteBook()
      else:
        print("Invalid choice.")



  def doListBooks():
    print("\nList Books:")
    found=False
    with open(LibrarySystem.BOOKS_FILE) as file:
      while (line:=file.readline().rstrip()):
        rec=line.split("|")
        if not found:
          print("{:<5} {:<40} {:<40} {:<9}".format("ID","Book Name","Book Author","Available"))
          found=True
        print("{:<5} {:<40} {:<40} {:<9}".format(rec[0],rec[1],rec[2],rec[3]))
       


  def doAddBook():

    print("\nADD BOOK")

    found=True      
    while found:
      found=False      
      id=input("Book ID: ")

      with open(LibrarySystem.BOOKS_FILE) as file:      
        while (line:=file.readline().rstrip()):
          rec=line.split("|")
          if id==rec[0]:
            found=True
            break

      if found:
        print("\nID already exist.")

    name=input("Book name: ")
    author=input("Book author: ")
    available="true";

    with open(LibrarySystem.BOOKS_FILE,"a") as file:      
      file.write("{}|{}|{}|{}\n".format(id,name,author,available))

    print("\nRecord added.")



  def doSearchBook():
    print("\nSEARCH BOOK")
    search=input("Search Text: ")
    print()
    
    words=search.split(" ")
    with open(LibrarySystem.BOOKS_FILE) as file:
      notFound=True
      while (line:=file.readline().rstrip()):
        found=False
        for word in words: 
          if line.lower().find(word.lower())!=-1:
            found=True
            notFound=False
            break
        if found:
          rec=line.split("|")
          print("ID: {}".format(rec[0]))
          print("Book name: {}".format(rec[1]))
          print("Author: {}".format(rec[2]))
          print("Available: {}\n".format(rec[3]))

      if notFound:
        print("Record not found.")   
    


  def doUpdateBook():
    print("\nUPDATE BOOK")
    id=int(input("Book ID: "))
    print()

    with open(LibrarySystem.BOOKS_FILE) as file:      
      lines=[]
      found=False
      while (line:=file.readline().rstrip()):
        rec=line.split("|")
        if id==int(rec[0]):
          found=True

          print("ID: {}".format(rec[0]))
          print("Book name: {}".format(rec[1]))
          print("Author: {}\n".format(rec[2]))
          
          name=input("Update Book name: ")
          author=input("Update Author: ")

          available=""
          while True:
            print(
              "\nUpdate Book is Available:\n"+
              "1. Yes\n"+
              "2. No\n"
            )
            choice=int(input("Choice: "))
            if choice==1:
              available="true"
              break
            elif choice==2:
              available="false"
              break
            else:
              print("Invalid choice.") 

          lines.append("{}|{}|{}|{}".format(id,name,author,available))
          
        else:
          lines.append(line)

      if found:
        with open(LibrarySystem.BOOKS_FILE,"w") as file:
          for line in lines:
            file.write("{}\n".format(line))
        print("\nRecord updated.")
      else:
        print("\nRecord not found.")



  def doDeleteBook():
    print("\nDELETE BOOK")
    id=int(input("Book ID: "))
    print()

    with open(LibrarySystem.BOOKS_FILE) as file:
      lines=[]
      found=False
      while (line:=file.readline().rstrip()):
        rec=line.split("|")
        if id==int(rec[0]):
          found=True
        else:
          lines.append(line)

      if found:
        with open(LibrarySystem.BOOKS_FILE,"w") as file:
          for line in lines:
            file.write("{}\n".format(line))
        print("\nRecord is deleted.")
      else:
        print("\nRecord not found.")
      
      
  
  def doBorrowerManagementMenu():
    while True:
      print(
        "\n================================================"+
        "\n\n             BORROWER MANAGEMENT MENU\n"+
        "\n================================================"+
        "\n\n\t    [1] SEARCH BORROWER"+
        "\n\t    [0] GO BACK TO LIBRARIAN MENU"+
        "\n\n================================================"
      )
      choice=int(input("Choice: "))
      if choice==0:
        break
      elif choice==1:
        LibrarySystem.doSearchBorrower()
      else:
        print("Invalid choice.")



  def doSearchBorrower():
    print("\nSEARCH BORROWER")
    id=int(input("User ID: "))
    print()

    with open(LibrarySystem.PROFILES_FILE) as file0:
      while (line0:=file0.readline().rstrip()):
        rec0=line0.split("|")
        if id==int(rec0[0]):
          print("Name: {} {}".format(rec0[1],rec0[2]))
          print("Address: {}\n".format(rec0[3]))
          break

    count=0
    with open(LibrarySystem.BORROWERS_FILE) as file1:
      while (line1:=file1.readline().rstrip()):
        rec1=line1.split("|")
        if id==int(rec1[0]):
          with open(LibrarySystem.BOOKS_FILE) as file2:
            while (line2:=file2.readline().rstrip()):
              rec2=line2.split("|")
              if rec1[1]==rec2[0]:
                count+=1 
                if rec1[4]=="false":
                  print("{}. Borrowed Book ID {} Title {} by {} at {} not yet Returned.\n".format(count,rec2[0],rec2[1],rec2[2],rec1[2]))
                else:
                  print("{}. Borrowed Book ID {} Title {} by {} at {} and Returned at {}\n".format(count,rec2[0],rec2[1],rec2[2],rec1[2],rec1[3]))

                  

  def doStudentMenu():
    while True:
      print(
        "\n================================================"+
        "\n\n                STUDENT  MENU\n"+
        "\n================================================"+
        "\n\n\t  [1] ACCOUNT MANAGEMENT"+
        "\n\t  [2] BORROW\RETURN BOOK MANAGEMENT"+
        "\n\t  [0] GO BACK TO LOGIN"+
        "\n\n================================================"
      )
      
      choice=int(input("Choice: "))
      if choice==0:
        break
      elif choice==1:
        LibrarySystem.doAccountManagementMenu()
      elif choice==2:
        LibrarySystem.doBorrowReturnBookManagementMenu()
      else:
        print("Invalid choice.")

        

  def doAccountManagementMenu():
    while True:
      print(
        "\n================================================"+
        "\n\n            ACCOUNT MANAGEMENT MENU\n"+
        "\n================================================"+
        "\n\n\t    [1] CHANGE PASSWORD"+
        "\n\t    [2] VIEW PROFILE"+
        "\n\t    [3] UPDATE PROFILE"+
        "\n\t    [0] GO BACK TO STUDENT MENU"+
        "\n\n================================================"
      )
      choice=int(input("Choice: "))
      if choice==0:
        break
      elif choice==1:
        LibrarySystem.doChangePassword()
      elif choice==2:
        LibrarySystem.doViewProfile()
      elif choice==3:
        LibrarySystem.doUpdateProfile()
      else:
        print("Invalid choice.")



  def doChangePassword():
    print("\nChange Password:")
    lines=[]
    found=False
    with open(LibrarySystem.USERS_FILE) as file:
      while (line:=file.readline().rstrip()):
        rec=line.split("|")
        if LibrarySystem.user["id"]==int(rec[0]):
          found=True
          password=input("Update Password: ")
          lines.append("{}|{}|{}|{}".format(rec[0],rec[1],password,rec[3]))
        else:  
          lines.append(line)
    if found:
      with open(LibrarySystem.USERS_FILE,"w") as file:
        for line in lines:
          file.write("{}\n".format(line))
      print("Record updated.")
    else:  
      print("Record not found.")



  def doViewProfile():
    print("\nView Profile:\n")

    with open(LibrarySystem.PROFILES_FILE) as file:      
      lines=[]
      found=False
      while (line:=file.readline().rstrip()):
        rec=line.split("|")
        if LibrarySystem.user["id"]==int(rec[0]):
          found=True

          print("Firstname: {}".format(rec[1]))
          print("Lastname: {}".format(rec[2]))
          print("Address: {}\n".format(rec[3]))

      if not found:
        print("Record not found.")



  def doUpdateProfile():
    print("\nUpdate Profile:\n")

    with open(LibrarySystem.PROFILES_FILE) as file:      
      lines=[]
      found=False
      while (line:=file.readline().rstrip()):
        rec=line.split("|")
        if LibrarySystem.user["id"]==int(rec[0]):
          found=True

          print("Firstname: {}".format(rec[1]))
          print("Lastname: {}".format(rec[2]))
          print("Address: {}\n".format(rec[3]))

          firstname=input("Update Firstname: ")
          lastname=input("Update Lastname: ")
          address=input("Update Address: ")

          lines.append("{}|{}|{}|{}".format(LibrarySystem.user["id"],firstname,lastname,address))
          
        else:
          lines.append(line)

      if found:
        with open(LibrarySystem.PROFILES_FILE,"w") as file:
          for line in lines:
            file.write("{}\n".format(line))
      else:
        print("ENTER PROFILE")  

        firstname=input("Firstname: ")
        lastname=input("Lastname: ")
        address=input("Address: ")

        with open(LibrarySystem.PROFILES_FILE,"a") as file:
          file.write("{}|{}|{}|{}\n".format(LibrarySystem.user["id"],firstname,lastname,address))

      print("Record updated.")
  
  
        
  def doBorrowReturnBookManagementMenu():
    while True:
      print(
        "\n================================================"+
        "\n\n       BORROW\RETURN BOOK MANAGEMENT MENU\n"+
        "\n================================================"+
        "\n\n\t    [1] BOOK LIST"+
        "\n\t    [2 SEARCH BOOK"+
        "\n\t    [3] BORROW BOOK"+
        "\n\t    [4] RETURN BOOK"+
        "\n\t    [0] GO BACK TO STUDENT MENU"+
        "\n\n================================================"
     )
      choice=int(input("Choice: "))
      if choice==0:
        break
      elif choice==1:
        LibrarySystem.doListBooks()
      elif choice==2:
        LibrarySystem.doSearchBook()
      elif choice==3:
        LibrarySystem.doBorrowABook()
      elif choice==4:
        LibrarySystem.doReturnABook()
      else:
        print("Invalid choice.")



  def doBorrowABook():
    print("\nBorrow a Book:\n")
    id=input("Book ID: ")
    print()

    with open(LibrarySystem.BOOKS_FILE) as file:      
      lines=[]
      found=False
      while (line:=file.readline().rstrip()):
        rec=line.split("|")
        if id==rec[0] and rec[3]=="true":
          found=True

          print("ID: {}".format(rec[0]))
          print("Book name: {}".format(rec[1]))
          print("Author: {}\n".format(rec[2]))

          lines.append("{}|{}|{}|{}".format(rec[0],rec[1],rec[2],"false"))

        else:
          lines.append(line)

      if found:
        with open(LibrarySystem.BOOKS_FILE,"w") as file:
          for line in lines:
            file.write("{}\n".format(line))

        with open(LibrarySystem.BORROWERS_FILE,"a") as file:

         user_id=LibrarySystem.user["id"]
         book_id=id
          
         now=datetime.now()
         date_borrowed=now.strftime("%Y/%m/%d %I:%M:%S %p")
         date_returned="none"
         returned="false"
          
         file.write("{}|{}|{}|{}|{}\n".format(user_id,book_id,date_borrowed,date_returned,returned))
       
         print("Book borrowed.")
    
      else:
        print("Book is not available.")


  def doReturnABook():
    print("\nReturn a Book\n")
    borrowed=[]
    found=False
    with open(LibrarySystem.BORROWERS_FILE) as file1:
      while (line1:=file1.readline().rstrip()):
        rec1=line1.split("|")
        if LibrarySystem.user["id"]==int(rec1[0]):
          with open(LibrarySystem.BOOKS_FILE) as file2:
            while (line2:=file2.readline().rstrip()):
              rec2=line2.split("|")
              if rec1[1]==rec2[0] and rec1[4]=="false":
                found=True
                borrowed.append([rec2[1],rec2[2],rec1[1],rec1[2]])

    if found:
      print("{:>3} {:<40} {:<40} {:<8} {:<22}".format("###","Book Name","Book Author","Book ID","Borrowed Date"))
      for i in range(len(borrowed)):
        print("{:>3} {:<40} {:<40} {:<8} {:<22}".format(i+1,borrowed[i][0],borrowed[i][1],borrowed[i][2],borrowed[i][3]))

      print()


      book_id=input("Book ID to return: ")
      
      foundId=False
      for book in borrowed:

        if book_id==book[2]:
          foundId=True  

          dtfmt="%Y/%m/%d %I:%M:%S %p"
          date_borrowed=datetime.strptime(book[3],dtfmt)  

          date_returned=datetime.now()


          # use this for testing date returned 
          #date_returned=datetime.strptime("2022/12/3 11:14:00 PM",dtfmt)


          delta=date_returned-date_borrowed
          str_date_returned=date_returned.strftime("%Y/%m/%d %I:%M:%S %p")

          if delta.days > 7:
            fine = int(delta.days-7) * LibrarySystem.finePerDay
            print("Books borrowed over a week must pay PHP {:.2f} per day fine.".format(LibrarySystem.finePerDay))

            print("Over {} days so you must pay PHP {:.2f} fine.".format(int(delta.days-7),fine))

          found=False
          lines=[]
          with open(LibrarySystem.BOOKS_FILE) as file3:
            while (line3:=file3.readline().rstrip()):
              rec3=line3.split("|")
              if book_id==rec3[0]:
                found=True
                lines.append("{}|{}|{}|{}".format(rec3[0],rec3[1],rec3[2],"true"))
              else:
                lines.append(line3)
          if found:
            with open(LibrarySystem.BOOKS_FILE,"w") as file4:
              for line in lines:
                file4.write("{}\n".format(line))

          found=False
          lines=[]
          with open(LibrarySystem.BORROWERS_FILE) as file5:
            while (line5:=file5.readline().rstrip()):
              rec5=line5.split("|")
              if LibrarySystem.user["id"]==int(rec5[0]) and book_id==rec5[1]:
                found=True
                lines.append("{}|{}|{}|{}|{}".format(rec5[0],rec5[1],rec5[2],str_date_returned,"true"))
              else:
                lines.append(line5)

          if found:
            with open(LibrarySystem.BORROWERS_FILE,"w") as file6:
              for line in lines:
                file6.write("{}\n".format(line))

      if foundId:
        print("Book is returned.")
      else:
        print("Book not found.")

    else:
      print("No borrowed books.")


        
LoginSystem.doLogin()
