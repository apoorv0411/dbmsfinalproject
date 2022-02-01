from asyncio.windows_events import NULL
from helper import DBH
import mysql.connector as connector


#main 

def main():
    db = DBH()
    while True:
        print("*************WELCOME TO THE REGISTRATION FORM DATABASE**************")
        print()
        print("Press 1 to insert a new user")
        print("Press 2 to display all users")
        print("Press 3 to delete user")
        print("Press 4 to update user")
        print("Press 5 to exit the program")
        print()
        try:
            choice=int(input())
            if(choice==1):
                uid=int(input("Enter user ID: "))
                username=input("Enter username: ")
                userphone=input("Enter user's phone: ")
                db.insert_userdata(uid, username, userphone)

                pass
            elif choice==2:
                db.fetch_all()
                pass 
            elif choice==3:
                userid=int(input("Enter the user id of whom you want to delete"))
                db.delete_user(userid)
                pass
            elif choice==4:
                uid=int(input("Enter user ID: "))
                username=input("Enter new name: ")
                userphone=input("Enter new name: ")
                db.update_user(uid, username, userphone)
                pass
            elif choice==5:
                break
            else: 
                print("The input is invalid")
        except Exception as e:
                print(e)
                print("Invalid")

if __name__== "__main__":
    main()

#helper = DBH()
#helper.insert_userdata(111, "Apoorv", 4532)
#helper.insert_userdata(121, "Justin", 45332)
#helper.insert_userdata(183, "Peter", 54532)
#helper.insert_userdata(191, "Carlos", 453832)
#helper.insert_userdata(511, "Filip", 7632)
#helper.insert_userdata(151, "Monty", 9932)
#helper.insert_userdata(161, "Martin", 6321)
#helper.insert_userdata(110, "Ariana", 8783)
#helper.insert_userdata(311, "Kelly", 9885)
#helper.delete_user(161)
#
#helper.update_user(311, "Ainura", '34334')
#helper.fetch_all()
