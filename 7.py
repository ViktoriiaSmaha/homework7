text = input("Enter text")
result = 0

for symbol in text:
    if symbol.isdigit():
        result = result + 1
print(result)