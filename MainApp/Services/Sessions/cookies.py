from flask import *

def cookieChecker():
    uck = request.cookies.get('userID')
    sck = request.cookies.get('sessionCookie')
    if not request.cookies.get('sessionCookie'): 
        return redirect(url_for('login'))