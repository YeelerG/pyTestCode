def checkIfPrime(number):
    for x in range(2, number):
        if number % x == 0:
            return False
    return True

'''
try:
    num = int(input("Please input a number: "))
    print
    checkIfPrime(num)
except ValueError:
    print("Please input a number.")
except Exception as e:
    print("Unknown error: ", e)

'''