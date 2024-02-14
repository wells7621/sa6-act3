list_one = [2, 5, 27, 90, 125]
list_two = [1, 5, 34, 90, 125]

intersect = list(filter(lambda x: x in list_two, list_one))

print(intersect)