
name = input("Введите ваше имя: ")
age = int(input("Введите ваше возраст: "))
weight = float(input("Введите ваш вес в килограммах: "))
length = float(input("Введите ваш рост в метрах: "))
print(f"Привет, {name}! Ваш возраст: {age}. Ваш ИМТ {weight//length**2}")