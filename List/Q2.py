lists=[1,1,56,32,2,3,3,2,1,2,3,4,5,6]

# print(sorted(list(set(lists))))

# seen=set()

# list_style=[x for x in lists if not (x in seen or seen.add(x))]
# print(list_style)

# # Second way
num=[]
for x in lists:
    if x not in num:
        num.append(x)
print(num)