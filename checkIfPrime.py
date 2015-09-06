from prime import checkIfPrime

try:
    num = int(input("Please input a number: "))
    print(checkIfPrime(num))
except ValueError:
    print("It is not a number.")
except Exception as e:
    print("Unknown error: ", e)

# print sys.path
