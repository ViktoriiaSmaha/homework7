a = []
c = []

for i in range(5):
    number = int(input("Enter your number"))
    a.append(number)

for num in a:
    if num > 5:
        c.append(num)

print(c)