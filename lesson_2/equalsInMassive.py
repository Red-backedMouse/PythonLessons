def equelsNumbersInMassive(massive1, massive2):
    res = []
    for i in range(0, len(massive1)):
        for j in range(0, len(massive2)):
            if massive1[i] == massive2[j]:
                res.append(massive1[i])
                break
    return res


m1 = [1, 3, 3, 2, 1, 4]
m2 = [1, 2, 2, 2, 5]
print(f"Совпадение: {equelsNumbersInMassive(m1, m2)}")
