'''
    import mysql.connector

    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "VroomMustang2000$"
    )

    mycursor = mydb.cursor()

    mycursor.execute(
        "USE Customers;"
        "CREATE TABLE IF NOT EXISTS Customers(",
        "ID INT KEY AUTO_INCREMENT,",
        "Name VARCHAR(60) NOT NULL",
        ");"
    )

    for db in mycursor:
        print(db)
'''