db = [1,3,3.4,5.678,34,78.0009]
print("The List in Python")
print(db[0])
db[0] = db[0] + db[1]
print(db[0])
print("Add in the list")
db.append(111)
print(db)
print("Remove in the list")
db.remove(3)
print(db)
print("Sort in the list")
db.sort()
print(db)
db.reverse()
print(db)
print("Len in the list")
print(len(db))
print("For loop in the list")
for n_db in db:
	print(n_db)
print(min(db))
print(max(db))
print(sum(db))
my_food = ['rice', 'fish', 'meat']
friend_food = my_food
friend_food.append('ice cream')
print(my_food)
print(friend_food)
