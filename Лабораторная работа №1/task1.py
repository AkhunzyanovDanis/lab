numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
sum_numbers = sum(filter(None, numbers))
k = len(numbers)
sr = sum_numbers/k
numbers[4] = sr
print("Измененный список:", numbers)
