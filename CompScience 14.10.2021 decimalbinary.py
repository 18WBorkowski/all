dec = int(input("Enter decimal number: "))
binary = ""
while dec != 0:
    r = dec % 2
    dec = dec//2 
    binary += str(r)
    
print(int(binary[::-1]))
