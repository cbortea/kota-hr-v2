from crypt import methods
from flask import *

from Sessions.cookies import cookieChecker
from Authentication.SignIn import sigin
from Authentication.SignUp import signup

main = Flask(__name__, template_folder = '../Templates', static_folder = '../Static')

@main.route(
    '/', 
    methods = ['GET']
)
def domainAccess():
    if request.method == 'GET':
        return cookieChecker()

@main.route(
    '/login',
    methods = ['GET', 'POST']
)
def login():
    if request.method == 'GET':
        return render_template('login.htm')
    if request.method == 'POST':
        company = request.form['comp']
        username = request.form['usr']
        password = request.form['pwd']
        return sigin(username, password, company)

@main.route(
    '/register',
    methods = ['GET', 'POST']
)
def register():
    if request.method == 'GET':
        return render_template('register.htm')
    if request.method == 'POST':
        company = request.form['comp']
        firstName = request.form['fn']
        lastName = request.form['ln']
        email = request.form['em']
        username = request.form['usr']
        password = request.form['pwd']
        return signup(company, firstName, lastName, email, username, password)



if __name__ == '__main__':
    main.run(
        debug = True,
        host = '0.0.0.0',
        port = 5002
    )




'''

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "VroomMustang2000$"
)

print (mydb)

if mydb:
    print("Connection successful")
else:
    print("Connection unsuccessful")

'''