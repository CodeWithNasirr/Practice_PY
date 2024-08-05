#  How do you remove duplicates from a list of dictionaries based on a key?

my_list = [{'id': 1, 'value': 'a'}, {'id': 2, 'value': 'b'}, {'id': 1, 'value': 'c'}]
set=set()
uiq_list=[]

for d in my_list:
    if d['id'] not in set:
        uiq_list.append(d)
        set.add(d['id'])

print(uiq_list)