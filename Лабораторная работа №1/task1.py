numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
sum_numbers = sum(filter(None, numbers))
# количество символов
numbers_of_numbers = len(numbers)
# среднее значение
average = sum_numbers/numbers_of_numbers
numbers[4] = average
print("Измененный список:", numbers)
