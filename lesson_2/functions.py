def inter_numbers():
    res = []
    while True:
        x = int(input("Ввведите число: "))
        if x > 0:
            res.append(x)
        else:
            break
    return res


def calc_numbers(massive):
    calc = 1
    for i in range(0, len(massive)):
        calc = calc*massive[i]
    return calc


print(f"Произведение {calc_numbers(inter_numbers())}")