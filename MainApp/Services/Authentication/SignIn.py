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


def sigin(usr, pwd, comp):
    if usr == "" or usr == " " or pwd == "" or pwd == " " or comp == "" or comp == " ":
        formErr = Error['signin']['E0001']['value']
        return render_template('login.htm', ErrMsg = formErr)
    else:
        try:
            a = "SELECT Password FROM " + comp + ".Admins WHERE Username = '" + usr + "';"
            mycursor.execute(a)
            password = str(mycursor.fetchone())
            passc = re.sub("[(',)]", "", password)
            if pwd == passc:
                return render_template('dashboard.htm')
            else:
                formErr = Error['signin']['E0004']['value']
                return render_template('login.htm', ErrMsg = formErr)
        except:
            formErr = Error['signin']['E0002']['value']
            return render_template('login.htm', ErrMsg = formErr)
    file.close()