x = int(input("Ведите целое, положительное число: "))
count = 1
for i in range(1, x + 1):
    if i % 2 == 0:
        print(f"{i=}")