# factorial 4 = 1*2*3*4
j = 1
num = int(input("Enter number: "))
for i in range(1, num + 1):
    i *= j
    j = i
print(i)