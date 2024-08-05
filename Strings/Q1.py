#  How do you count the number of occurrences of each character in a string?


from collections import Counter
my_string = "hello world"
char_count = Counter(my_string)
print(char_count)