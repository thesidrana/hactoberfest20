#Programs orts words of string
print("Enter a string:")
my_str = input()

words = my_str.split()
words.sort()

print("The sorted words are:")
for word in words:
   print(word)
