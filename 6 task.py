N = int(input("Enter number for N"))
list = []
for i in range(N):
    number = int(input("Enter your number"))
    list.append(number)
print(list)
largest_number = list[0]
for number in list:
    if number > largest_number:
       largest_number = number
print(largest_number)
