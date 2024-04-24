def evens_numbers(count):
    evens = []
    for i in range(1, count+1):
        number = int(input(f"Введите число {i}: "))
        if number % 2 == 0:
            evens.append(number)
    return evens


print(f"Четные значения: {evens_numbers(int(input("Сколько цифр вы хотите ввести? ")))}")
