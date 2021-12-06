import sqleasy
import time

'''
hey guys, this is sql easy
'''

sqleasy.connect("database")
sqleasy.createTable("database", "users", "user TEXT, password TEXT, sqleasy BOOLEAN")
sqleasy.insertValue("database", "users", "user, password", "'sqleasy', 'password'")
sqleasy.getValue("database", "*", "users")
print("")
time.sleep(1)
sqleasy.changeValue("database", "users", "user", "'sqleasyiscool'", "user", "sqleasy")
sqleasy.getValue("database", "user", "users")
print("")
sqleasy.deleteValue("database", "users", "user", "'sqleasyiscool'")
sqleasy.getValue("database", "user", "users")
print("")
sqleasy.addColumnInTable("database", "users", "sqleasyiscool BOOLEAN")
sqleasy.deleteTable("database", "users")
