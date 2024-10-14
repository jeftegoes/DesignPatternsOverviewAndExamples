from database import Database

database = Database()

d1 = Database()
d2 = Database()

print(d1.id, d2.id)
print(d1 == d2)
print(database == d1)