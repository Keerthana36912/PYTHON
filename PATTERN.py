star = int(input("enter no of stars: "))
block = int(input("enter no of blocks: "))
line = int(input("enter no of lines: "))
for i in range(block):       
    count = 0
    for j in range(line - i):   
        for k in range(star):
            print("*", end="")
            count += 1
        print()
    print(count)
    print("_______")
