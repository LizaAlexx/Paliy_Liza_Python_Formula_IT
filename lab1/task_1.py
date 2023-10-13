numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
numbers[4] = 0
sum_ = sum(numbers)
len_ = len(numbers)
average_of_numbers = round(sum_ / len_, 2)
numbers[4] = average_of_numbers
print("Измененный список:", numbers)
