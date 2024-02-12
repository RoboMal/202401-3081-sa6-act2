people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
# Use a lambda function as the sorting key
sorted_people = sorted(people, key=lambda x: x[1])
print(sorted_people)

'''
Breakdown:
Using x[1] on Line 3 essentially sorts the list of tuples by age.
This is because x[1] refers to the SECOND element of each tuple (recall, list indicies start at 0)
'''