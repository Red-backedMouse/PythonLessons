age = int(input("Введите ваш возраст: "))
if 0 < age <= 6:
    print(f"Ребенок")
elif 6 < age <= 18:
    print(f"Подросток")
elif 18 < age <= 35:
    print(f"Юноша")
elif 35 < age <= 65:
    print(f"Взрослый")
elif 65 < age <= 110:
    print(f"Пожилой")
elif age > 110:
    print(f"Долгожитель")
else:
    print(f"Вы ввели не возраст")