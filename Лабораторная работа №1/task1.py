numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

missing_index = numbers.index(None)
sum_of_numbers = sum(numbers[:missing_index]) + sum(numbers[missing_index + 1:])
count_of_numbers = len(numbers)
average = round(sum_of_numbers / count_of_numbers, 2)
numbers[missing_index] = average

print("Измененный список:", numbers)

