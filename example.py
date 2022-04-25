import sqleasy
import time

'''
this is sqleasy
'''

sqleasy.connect("database")
sqleasy.createTable("database", "users", "user TEXT, password TEXT, sqleasy BOOLEAN")
sqleasy.insertValue("database", "users", "user, password", "'sqleasy', 'password'")
print(sqleasy.getValue("database", "*", "users"))
print("")
time.sleep(1)
sqleasy.changeValue("database", "users", "user", "'sqleasyiscool'", "user", "sqleasy")
print(sqleasy.getValue("database", "user", "users"))
print("")
sqleasy.deleteValue("database", "users", "user", "'sqleasyiscool'")
print(sqleasy.getValue("database", "user", "users"))
print("")
sqleasy.addColumnInTable("database", "users", "sqleasyiscool BOOLEAN")
sqleasy.deleteTable("database", "users")
