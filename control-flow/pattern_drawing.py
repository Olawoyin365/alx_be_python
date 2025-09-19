num = int(input("Enter the size of the pattern: "))
row = 0
while row < num:
    for i in range(num):
        print("*", end="")
    print()
    row += 1
