#User model
import mysql.connector
import json
from flask import make_response
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
            res= make_response({"payload":result},200)
            res.headers['Access-Control-Allow-Origin'] = '*'
            res
            return res
        else:
            return  make_response({"message":"No Data Found"},204)
        
   

       

    #POST
    def user_addone_model(self,data):
        print(data)
        self.cur.execute(f"INSERT INTO users(name,email,role,password,phone) VALUES('{data['name']}','{data['email']}','{data['role']}','{data['password']}','{data['phone']}')")
        
        return make_response({"message":"User Added Successfully"},201)


    #UPDATE
    def user_update_model(self,data):
        print("update data",data)
        self.cur.execute(f"UPDATE users set name='{data['name']}',email='{data['email']}',phone='{data['phone']}',role='{data['role']}',password='{data['password']}' WHERE id={data['id']}")
        if(self.cur.rowcount>0):
            return make_response({"message":"User Update Successfully"},201)
        else:
            return make_response({"message":"Nothing To Updated"},202)
    

    #DELETE
    def user_delete_controller(self,id):
        print("update data",id)
        self.cur.execute(f"DELETE FROM users WHERE id={id}")
        if(self.cur.rowcount>0):
            return make_response({"message":"User DELETED Successfully"},200)
        else:
            return make_response({"message":"Nothing deleted"},202)


     #PATCH   
    def user_patch_model(self,data,id):
        qry="UPDATE users SET "
        for key in data:
            # print(f"{key}={data[key]}")
            qry+= f"{key}='{data[key]}',"
       
        qry=qry[:-1]+f" WHERE id={id}"
        print(qry)
        self.cur.execute(qry)
        if(self.cur.rowcount>0):
            return make_response({"message":"User Update Successfully"},201)
        else:
            return make_response({"message":"Nothing To Updated"},202)
        
