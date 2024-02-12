numbers = [1, 2, 3, 4]
# Write a lambda function and use map
squared_numbers = list(map(lambda x: x * x, numbers))
print(squared_numbers)

'''
Breakdown: 
'list' constructor creates new list since one was not provided.
'map' makes an iterator that computes function arguments/applies the function to all list items
'lambda' eliminates the need to create helper function
'numbers' is the list being used as the second argument, lambda function automatically iterates through whole list
In this case, lambda function is being used to square list items (by multiplying them by themselves)
'''
