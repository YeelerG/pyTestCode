pets = ['Dog', 'Cat', 'Pig', 'mouse']

print("print items:")
for item in pets:
    print(item)

print("\nprint items with index:")

for index, item in enumerate(pets):
    print(index, item)

print("\nfor loop:")
message = "Hello"
for i in message:
    print(i)

print("\nwhile loop:")
length = 5
while length > 0:
    length -= 1
    if length == 2:
        continue
    else:
        print
        message[length]

print("range(start, end, step) usage:")
print
range(10)
print(range(3, 10))
print(range(4, 10, 2))
