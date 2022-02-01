from asyncio.windows_events import NULL
import mysql.connector as connector

class DBH:
    def __init__(self):
        self.con = connector.connect(host = 'localhost',
        port = '3306', user = 'root', password = 'Lollypop23', database = 'testdb')
        query = 'create table if not exists user(userId int primary key, userName varchar(100), phone varchar(10))'
        cur = self.con.cursor()
        cur.execute(query)
        print("The database is created")

    #add information to the users 
    def insert_userdata(self, userid, username, phone):
        query = "insert into user(userId,userName,phone) values({}, '{}', '{}')".format(
            userid, username, phone) 
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit
        print("This user is saved to the database")
        return True

    #fetching all the users information
    def fetch_all(self):
        query = "select * from user"
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("UserId : ", row[0])
            print("UserName : ", row[1])
            print("User Phone Number : ", row[2])
            print()
            print()
    
    #query used to delete user information
    def delete_user(self, userId, nameNew, phoneNew):
        query = "Delete from user where userId = {}" .format(userId)
        print(query)
        c = self.con.cursor()
        c.execute(query)
        self.con.commit()
        print("deleted")

    #query used to update user information
    def update_user(self, userId, nameNew, phoneNew):
        query = "update user set userName ='{}', phone ='{}' where userId = {}".format(nameNew, phoneNew, userId)
        print (query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Updated")

