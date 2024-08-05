# How do you flatten a list of lists?

my_list = [[1, 2, 3], [4, 5], [6, 7, 8]]
flat_list = [item for sublist in my_list for item in sublist]
print(flat_list)