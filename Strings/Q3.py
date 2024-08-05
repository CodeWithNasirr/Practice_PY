#  How do you reverse the words in a sentence?

sentence = "Hello world"

x=" ".join(word.capitalize()for word in sentence.split()[::-1])
print(x)