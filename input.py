myName = input("your name: ")
myAge = int(input("your age: "))

print("1. Hello World, my name is %s and I am %d years old." % (myName, myAge))
print("2. Hello World, my name is %s and I am %s years old." % (myName, myAge))
print("3. Hello World, my name is {} and I am {} years old.".format(myName, myAge))
print('4. Hello World, my name is {0:s} and I am {1:d} years old.'.format(myName, myAge))
print("5. Hello World, my name is " + myName + " and I am " + str(myAge) + " years old.")
print("6. Hello World, my name is " + myName + " and I am", myAge,  "years old.")

'''
Summary
1. int value can be output as %d or %s
2. raw_input() accepts input as string. (Python 2)
3. print(), brackets can be ignored in Python 2

'''
