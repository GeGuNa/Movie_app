from pony.orm import *


db = Database()


db.bind('mysql', host='localhost', user='phantom', passwd='123456', db='mov')


class Users(db.Entity):
   name = Required(str)
   surn = Required(str)
   registered = Optional(int)
   username = Required(str, unique=True)
   #email = Required(str, unique=True) 
   
   

class Categories(db.Entity):
   name = Required(str)


class Movies(db.Entity):
   name = Required(str)
   description = Required(str)


db.generate_mapping(create_tables=True)


@db_session
def check_user(id):
    return Users.exists(id=id)


@db_session
def check_movie(id):
    return Movies.exists(id=id)


@db_session
def check_cat(id):
    return Categories.exists(id=id)



@db_session
def Get_User(id):
    data = Users.get(id=id)
    return data

@db_session
def Get_Movie(id):
   data = Movies.get(id=id)
   return data
   
   
@db_session
def Get_Cat(id):
   data = Categories.exists(id=id)
   return data
   
   
"""

MariaDB [mov]> describe users;
+------------+--------------+------+-----+---------+----------------+
| Field      | Type         | Null | Key | Default | Extra          |
+------------+--------------+------+-----+---------+----------------+
| id         | int(11)      | NO   | PRI | NULL    | auto_increment |
| name       | varchar(255) | NO   |     | NULL    |                |
| surn       | varchar(255) | NO   |     | NULL    |                |
| registered | int(11)      | YES  |     | NULL    |                |
| username   | varchar(255) | NO   |     | NULL    |                |
+------------+--------------+------+-----+---------+----------------+


"""

   
@db_session
def Insert_usr(name: str, surn: str, nick: str):
   db.execute(f"insert into users (`name`,`surn`,`username`)  values('{name}','{surn}','{nick}')")
   print("done")
   
#Insert_usr("","","")     


#va = Get_User(1)

@db_session
def Users_list():
   #with db_session:
   aq = db.select("select * from users where id > 0")
   return aq
   #for va in aq:
      #print(f" id = {va.id} nick = {va.username} ")

"""
varq1 = Users_list()
for va in varq1:
   print(f" id = {va.id} nick = {va.username} ")
"""


"""
with db_session:
   qq = db.select("select * from users where id > 4")
   for az in qq:
      print(f" {az.id} {az.username} \n")
"""
