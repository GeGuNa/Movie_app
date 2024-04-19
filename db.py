from sqlobject import *


user = "xz"
password = "xz"
db_name= "xz"
host = "localhost"

connection_string = 'sqlite:a.sql'

connection = connectionForURI(connection_string)

sqlhub.processConnection = connection



class Person(SQLObject):
   firstName = StringCol()
   middleInitial = StringCol(
   lastName = StringCol()


Person.createTable()
