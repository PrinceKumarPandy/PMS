import pymysql
from tkinter import messagebox
def connect_database():
    try:
        conn=pymysql.connect(host='localhost',user='root',password='0123456')
        mycursor=conn.cursor()
    except:
        messagebox.showerror('Error','Something went wrong, Please open mysql app before running again')
        return
    mycursor.execute('CREATE DATABASE IF NOT EXISTS employee_data')
    mycursor.execute('USE employee_data')
    mycursor.execute('CREATE TABLE IF NOT EXISTS data (Id VARCHAR(20),Name VARCHAR(50),Mobile VARCHAR(15),Role VARCHAR(50),Gender VARCHAR(20),Projectname VARCHAR(50)')


def insert(id,name,mobile,role,gender,projectname):
    print(id,name,mobile,role)




