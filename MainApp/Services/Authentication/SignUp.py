from flask import *
import json
import mysql.connector
import re


mydb = mysql.connector.connect(
    host = "mysql",
    user = "root",
    port = "3306",
    passwd = "VroomMustang2000!"
)

mycursor = mydb.cursor()

file = open("/usr/src/kota-hr/Services/error.json", 'r')
Error = json.load(file)


def passCheck(password):
    check = True
    while check:  
        if (len(password)<6 or len(password)>12):
            break
        elif not re.search("[a-z]",password):
            break
        elif not re.search("[0-9]",password):
            break
        elif not re.search("[A-Z]",password):
            break
        elif not re.search("[$#@!]",password):
            break
        elif re.search("\s",password):
            break
        else:
            return True
    if check:
        return False



def signup(comp, fn, ln, em, usr, pwd):

    

    if comp == "" or comp == " ":
        formErr = Error['signup']['E0006']['value']
        return render_template('register.htm', ErrMsg = formErr)
    elif fn == "" or fn == " ":
        formErr = Error['signup']['E0007']['value']
        return render_template('register.htm', ErrMsg = formErr)
    elif ln == "" or ln == " ":
        formErr = Error['signup']['E0008']['value']
        return render_template('register.htm', ErrMsg = formErr)
    elif em == "" or em == " ":
        formErr = Error['signup']['E0009']['value']
        return render_template('register.htm', ErrMsg = formErr)
    elif usr == "" or usr == " ":
        formErr = Error['signup']['E0010']['value']
        return render_template('register.htm', ErrMsg = formErr)
    elif pwd == "" or pwd == " ":
        formErr = Error['signup']['E0011']['value']
        return render_template('register.htm', ErrMsg = formErr)
    elif passCheck(pwd) == False:
        formErr = Error['signup']['E0013']['value']
        return render_template('register.htm', ErrMsg = formErr)
    else:
        try:
            dbcreate = "CREATE DATABASE " + comp + ";"
            mycursor.execute(dbcreate)
            dbuse = "USE " + comp
            mycursor.execute(dbuse)
            dbtbemployee = "CREATE TABLE IF NOT EXISTS Employees (ID INT KEY AUTO_INCREMENT, FirstName VARCHAR(60) NOT NULL, LastName VARCHAR(60) NOT NULL, Email VARCHAR(60) NOT NULL, Username VARCHAR(60) NOT NULL, Password VARCHAR(60) NOT NULL);"
            mycursor.execute(dbtbemployee)
            dbtbadmin = "CREATE TABLE IF NOT EXISTS Admins (ID INT KEY AUTO_INCREMENT, FirstName VARCHAR(60), LastName VARCHAR(60), Email VARCHAR(60), Username VARCHAR(60), AdminType VARCHAR(60), Password VARCHAR(60));"
            mycursor.execute(dbtbadmin)
            firstAdminInsert = "INSERT INTO Admins (FirstName, LastName, Email, Username, AdminType, Password) VALUES (%s, %s, %s, %s, %s, %s);"
            firstAdminValues = [(fn, ln, em, usr, "Super Org Admin", pwd)]
            mycursor.executemany(firstAdminInsert, firstAdminValues)
            mydb.commit()
            return render_template('dashboard.htm')
        except:
            formErr = Error['signup']['E0012']['value']
            return render_template('register.htm', ErrMsg = formErr)
        

    '''
def signup(comp, fn, ln, em, usr, pwd):
    mycursor.execute("SHOW DATABASES;")
    for company in mycursor:
        if company == comp:
            formErr = Error['signin']['E0012']['value']
            return render_template('register.htm', ErrMsg = formErr)
    else:
        dbcreate = "CREATE DATABASE IF NOT EXISTS " + comp + ";"
        mycursor.execute(dbcreate)
        dbuse = "USE " + comp
        mycursor.execute(dbuse)
        dbtbemployee = "CREATE TABLE IF NOT EXISTS Employees (ID INT KEY AUTO_INCREMENT, FirstName VARCHAR(60) NOT NULL, LastName VARCHAR(60) NOT NULL, Email VARCHAR(60) NOT NULL, Username VARCHAR(60) NOT NULL, Password VARCHAR(60) NOT NULL);"
        mycursor.execute(dbtbemployee)
        dbtbadmin = "CREATE TABLE IF NOT EXISTS Admins (ID INT KEY AUTO_INCREMENT, FirstName VARCHAR(60), LastName VARCHAR(60), Email VARCHAR(60), Username VARCHAR(60), AdminType VARCHAR(60), Password VARCHAR(60));"
        mycursor.execute(dbtbadmin)
        firstAdminInsert = "INSERT INTO Admins (FirstName, LastName, Email, Username, AdminType, Password) VALUES (%s, %s, %s, %s, %s, %s);"
        firstAdminValues = [(fn, ln, em, usr, "Super Org Admin", pwd)]
        mycursor.executemany(firstAdminInsert, firstAdminValues)
        mydb.commit()
        return "yes"
    '''