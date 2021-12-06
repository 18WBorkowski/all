input_list = []
total = 0
while len(input_list) < 10:
    num = float(input("Enter a number: "))
    input_list.append(num)
for i in input_list:
    total += i
print(total / 10)