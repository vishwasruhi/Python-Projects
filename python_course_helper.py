import sqlite3 as lite

# functionality goes here

class DatabaseManage(object):
    def __init__(self):
        global con
        try:
            con = lite.connect('vishwass.db')
            with con:
                curr = con.cursor()
                curr.execute("CREATE TABLE IF NOT EXISTS vishwas(ID INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT, price TEXT, is_private BOOLEAN NOT NULL DEFAULT 1 )")
        except Exception:
            print("Unable to create DB!")
    
    #TODO: Create Data
    def insert_data(self,data):
        try:
            with con:
                curr = con.cursor()
                curr.execute(
                    "INSERT INTO vishwas(name,description,price,is_private) VALUES (?,?,?,?)",data
                    )
                return True
        except Exception:
            return False

    #TODO: Read the Data    
    def fetch_data(self):
        try:
            with con:
                curr= con.cursor()
                curr.execute("SELECT * FROM vishwas")
                return curr.fetchall()
        except Exception:
            return False
    #TODO: Delete Data
    def delete_data(self,ID):
        try:
            with con:
                curr = con.cursor()
                sql = "DELETE FROM vishwas WHERE ID=?"
                curr.execute(sql, [ID])
            return True
        except Exception:
            return False
        


#provide interface to user

def main():
    print("*"*40)
    print("\n :: COURSE MANAGEMENT :: \n")
    print("*"*40)
    print("\n")
    db = DatabaseManage()

    print("#"*40)
    print("\n :: User Manual :: \n")
    print("#"*40)

    print("1. Insert a new course\n")
    print("2. Show all course\n")
    print("3. Delete a course(Need ID of Course)\n")
    print("#"*40)

    print("\n")

    choice=input('\n Enter a choice: ')

    if choice == "1":
        name=input("\n Enter course name: ")
        description=input("\n Enter course description: ")
        price=input("\n Enter course price: ")        
        private=input("\n Is this course private(0/1): ")

        if db.insert_data([name,description,price,private]):
            print("Course was inserted successfully")
        else:
            print("Course was not inserted")


    elif choice == "2":
        print("\n:: Course List ::")
        for index, item in enumerate(db.fetch_data()):
            print("\n SL no: " + str(index + 1))
            print("Course ID: " + str(item[0]))
            print("Course Name: " + str(item[1]))
            print("Course Description: " + str(item[2]))
            print("Course Price: " + str(item[3]))
            private = "Yes" if item[4] else "No"
            print("Is Private: " + private)
            print("\n")
    
    elif choice == "3":
        record_id = input("Enter the course ID")
        
        if db.delete_data(record_id):
            print("Course was deleted successfully")
        else:
            print("Course was not deleted")
        
    else:
        print("BAD CHOICE")



if __name__ == '__main__':
    main()