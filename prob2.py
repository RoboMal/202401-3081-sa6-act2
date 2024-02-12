numbers = [1, 2, 3, 4, 5, 6]
# Write a lambda function and use filter
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

'''
Breakdown:
'filter' automatically removes items that do not meet the enclosed condition
In this case, lambda function is being used to check if number is even by calculating
x % 2 (or, "x mod 2")
If result == 0: list item is even
else: list item is not even
'''