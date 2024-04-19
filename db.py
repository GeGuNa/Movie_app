from sqlobject import *

user = ""
password = ""
db_name= ""
host = ""

connection_string = 'sqlite:a.sql'

connection = connectionForURI(connection_string)

sqlhub.processConnection = connection



class Person(SQLObject):
   firstName = StringCol()
   middleInitial = StringCol(
   lastName = StringCol()


Person.createTable()
