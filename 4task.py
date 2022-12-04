N = int(input("Enter number for N"))
numbers = []
for i in range(N):
    number = int(input("Enter your number"))
    numbers.append(number)
numbers.reverse()
print(numbers)