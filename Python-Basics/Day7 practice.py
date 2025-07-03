# comprehension practice
# List Comprehension Problems
# problem 1 Create a list of squares of numbers from 1 to 10.
#for x in range(1,5):
    #square = x**2
    #print(square)
# comprehension form
square = [x**2 for x in range(1, 11)]
print(square)
print("THE END")
# problem 2  use list comprehension to create a list of even numbers.
#for x in range (1,11):
    #if  x%2 ==0:
       # print(x)
       # comprehension form 
even =  [x for x in range(1, 11) if x%2 == 0]
print(even)
print("THE END")
# problem 3 Given a list of words, return a list containing the length of each word. Input: ["apple", "banana", "kiwi"] Output: [5, 6, 4]
fruits = ["apple", "banana", "kiwi"]
length = [len(fruit) for fruit in fruits]
print(length)
print("THE END")
# String Comprehension Problems
# problem 4 Extract only vowels from a given string using comprehension.
word = "hello world"
vowels = "aeiou"
new_word = ""
for ch in word:
    if ch not in vowels:
        new_word += ch
print(new_word)
# string comprehension foam
new_word = ''.join([ch for ch in "hello world" if ch not in "aeiou"])
print(new_word)
# problem 5 Extract uppercase letters from a string. Input: "PyTHon" Output: ['P', 'T', 'H']
word = "pYtHoN"
for ch in word:
    if ch.isupper() is True:
        print(ch)
print("THE END")
# comprehension form
upp_letter = [ch for ch in "pYtHoN" if ch.isupper() is True]
print(upp_letter)
print("THE END")
#Set Comprehension Problems
# problem 6  Get a set of unique characters from a string. Input: "hello" Output: {'h', 'e', 'l', 'o'}
string = "hello"
unique_charac = set()
for ch in string:
    if ch not in unique_charac:
        unique_charac.add(ch)
print(unique_charac)
print("THE END")
# comprehension
unique_character = {ch for ch in "hello"}
print(unique_character)
# problem 7  Square Roots Rounded: Create a set of rounded square roots from 1 to 10. Expected Output: {1, 2, 3} (since sqrt(9)=3, sqrt(4)=2, etc.)
rounded_root = set()
for i in range(1, 11):
    root =round( i ** (0.5))
    rounded_root.add(root)
print(rounded_root)
print("the end")
# set coprehension
rounded_roots = {round(i ** 0.5) for i in range(1, 11)}
print(rounded_roots)
print("THE END")
#                                  Dictionary Comprehension Problems
# problem 8. Number: Square Pairs: Create a dictionary mapping numbers from 1 to 5 to their squares. Expected Output: {1:1, 2:4, 3:9, 4:16, 5:25}
dictionary = {}
for i in range(1, 6):
    squares = i**2
    dictionary[i] = squares
print(dictionary)
print("THE END")
#  comprehension
dict = {i:i ** 2 for i in range(1, 6)}
# problem 9 Word: Length Mapping From a list of words, make a dictionary where the word is the key and its length is the value.Input: ["apple", "banana", "kiwi"] Output: {"apple": 5, "banana": 6, "kiwi": 4}
fruits = ["apple", "banana", "kiwi"]
length_fruits = {}
for word in fruits:
    length_fruits[word]= len(word)
print(length_fruits)
print("THE END")
fruit = ["apple", "banana", "kiwi"]
length_fruit = {word : len(word) for word in fruits}
print(length_fruit)
print("THE END")
# problem 10 Character Frequency: Count how many times each character appears in a string. Input: "hello" Output: {'h':1, 'e':1, 'l':2, 'o':1}
word = "hello"
frequency = {}
for ch in word:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1
print(frequency)
# comprehension
word = "hello"
frequency = {ch:word.count(ch) for ch in word }
print(frequency)