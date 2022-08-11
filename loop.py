numbers = [7, 69, 2, 221, 8974]
numbers.sort()
max_result = sum(numbers) - numbers[0]
min_result = sum(numbers) - numbers[-1]
print(min_result,max_result)