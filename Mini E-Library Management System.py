from datetime import datetime


class LoginSystem:

  def doLogin():
    while True:
      print("\nLOGIN")
      username=input("Username: ")    
      password=input("Password: ")

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
        print("\n    Access Granted. ")
        if LibrarySystem.user["role"]=="librarian":
          LibrarySystem.doLibrarianMenu()
        else:
          LibrarySystem.doStudentMenu()
      else:
        print("\n***** Access Denied *****")



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
        

LoginSystem.doLogin()