myList = [1,2,3,4,5, 'Good morning']

print("Oringial list:")
print(myList)
print()

print("Insert an item:")
myList.append('Good afternoon')
print(myList)
print()

print("Delete an item:")
del myList[5]
print(myList)
print()

print("Update an item:")
myList[2] = 'Good Evening'
print(myList)
print()

print("assign last three item to a new list")
print(myList)
myList2 = myList[3:6]
print(myList2)
