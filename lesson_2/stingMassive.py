def string_massive(massive):
    massive2 = []
    for i in massive:
        if i[0] != "а":
            massive2.append(i)
    return massive2


m1 = ["ананас", "банан", "виноград", "авокадо"]
print(f"Не начинается с а: {string_massive(m1)}")