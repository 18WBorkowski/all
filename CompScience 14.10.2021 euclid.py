num1 = int(input("Enter number: "))
num2 = int(input("Enter number: "))

a = 0 # larger num
b = 0 # smaller num

if num1 > num2:
    a = num1
    b = num2
else:
    a = num2
    b = num1

r = 1
while r != 0:
    r = a % b
    a = b
    if r != 0:
        b = r

print(b)
