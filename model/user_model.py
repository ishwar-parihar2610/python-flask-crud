#User model
import mysql.connector
import json
class user_model():

    # connection String
    def __init__(self):
        try:
            self.conn=  mysql.connector.connect(
                host="localhost",
                user="root",
                password="123456",
                database="flask_tutoriial"
            )
            self.conn.autocommit=True
               
            self.cur=self.conn.cursor(dictionary=True)
            print("Connection Successfull")


        except:
            print("Some error")
    
    #get
    def user_getall_model(self):
        self.cur.execute("SELECT * FROM users")
        result=self.cur.fetchall()
      
        if(len(result)>0):
            return json.dumps(result)
            print("result",result)
        else:
            return "Empty Selection"

       

    #POST
    def user_addone_model(self,data):
        print(data)
        self.cur.execute(f"INSERT INTO users(name,email,role,password,phone) VALUES('{data['name']}','{data['email']}','{data['role']}','{data['password']}','{data['phone']}')")
        
        return "User Create Successfully"


    #UPDATE
    def user_update_model(self,data):
        print("update data",data)
        self.cur.execute(f"UPDATE users set name='{data['name']}',email='{data['email']}',phone='{data['phone']}',role='{data['role']}',password='{data['password']}' WHERE id={data['id']}")
        if(self.cur.rowcount>0):
            return "User Updated Successfully"
        else:
            return "Nothing To Updated"
    

    #DELETE
    def user_delete_controller(self,id):
        print("update data",id)
        self.cur.execute(f"DELETE FROM users WHERE id={id}")
        if(self.cur.rowcount>0):
            return "User DELETED Successfully"
        else:
            return "Nothing deleted"
