x = int(input("Ведите целое, положительное число: "))
count = 1
while count <= x:
    if count % 2 == 0:
        print(f"{count = }")
    count += 1