# How do you find the intersection of two sets?
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1&set2)


for x in set1:
    if x in set2:
        print(x)


common_elements = set1.intersection(set2)
for x in common_elements:
    print(x)
