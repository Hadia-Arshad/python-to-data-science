# lambda function
# problem 1 Write a lambda function that takes a number as input and returns its square.
square = lambda x: x*x
print(square(5))
print("THE END")
#     without lambda function
def square(x):
    return x*x
print(square(5))
# problem 2 Write a lambda function that returns "Even" if the number is even, and "Odd" if it’s odd.
def even_odd(x):
    if x%2 ==0:
        return "even"
    else:
        return "odd"
print(even_odd(2))
print("THE END")
#    by lambda function
even_odd = lambda x: "even" if x%2 ==0 else "odd"
print(even_odd(3))
print("THE END")
# problem 3 Given a list of tuples like [(1, 3), (2, 1), (4, 2)], use a lambda function to sort it by the second element of each tuple.
def get_second_element(t):
    return t[1]

data = [(1, 3), (2, 1), (4, 2)]

# Sort using the named function
sorted_data = sorted(data, key=get_second_element)

print(sorted_data)
print("THE END")
# by lambda function
data = [(1, 3), (2, 1), (4, 2)]
sort_data = sorted(data, key = lambda x : x[1])
print(sort_data)
# problem 4 Given a list of words, use filter() with a lambda function to return only the words that start with the letter 'a'. Input: ["apple", "banana", "apricot", "cherry", "avocado"]
words = ["apple", "banana", "apricot", "cherry", "avocado"]
result = list(filter(lambda word: word.startswith("a"), words))
print(result)
print("THE END")
# without lambda function
def starts_with_a(word):
    return word.startswith('a')

words = ["apple", "banana", "apricot", "cherry", "avocado"]

# Use the named function with filter
result = list(filter(starts_with_a, words))

print(result)
# problem 5 Given a list of numbers, use map() with a lambda to multiply all elements by 3.
numbers = [1, 2, 3, 4]
multiply = list(map(lambda x: x*3, numbers))
print(multiply)
print("THE END")
# without lambda function
def multiply(num):
    return num * 3
numbers = [1, 2, 3, 4]
results = list(map(multiply, numbers))
print(results)
print("THE END")
# problem 6 Use map() with a lambda function to square each number in a list.
numbers = [1, 2, 3, 4, 5]
square = list(map(lambda x : x**2, numbers))
print(square)
print("THE END")
# without lambda function
def squares(x):
    return x**2
numbers = [1, 2, 3, 4, 5]
result = list(map(squares, numbers))
print(result)
print("THE END")
# problem 7 Use filter() with a lambda function to return only odd numbers from a list. Input: [1, 2, 3, 4, 5, 6]
numbers = [1, 2, 3, 4, 5, 6]
odd = list(filter(lambda x: x%2 != 0, numbers))
print(odd)
print("THE END")
# without lambda 
def odd(x):
    return x%2 !=0 
numbers = [1, 2, 3, 4, 5, 6]
result = list(filter(odd, numbers))
print(result)
print("THE END")
# problem 8 Given a list of strings, use filter() and a lambda to return words with length > 4. Input: ["apple", "is", "very", "delicious", "yum"]
words = ["apple", "is", "very", "delicious", "yum"]
result = list(filter(lambda word: len(word) > 4 , words))
print(result)
print("THE END")
# without lambda function 
def smaller_words(word):
    return len(word) > 4
words = ["apple", "is", "very", "delicious", "yum"]
result = list(filter(smaller_words, words))
print(result)
# problem 9 Use functools.reduce() with a lambda to multiply all numbers in a list. Input: [1, 2, 3, 4]
from functools import reduce
numbers = [1, 2, 3, 4]
product = (reduce(lambda x, y : x*y, numbers))
print(product)
print("THE END")
# without lambda function
def product (x, y):
    return x*y
numbers = [1, 2, 3, 4]
result = (reduce(product, numbers))
print(result)
print("THE END")
# problem 10 Use reduce() with a lambda to find the largest number in a list. [4, 17, 9, 3, 21, 6]
from functools import reduce
numbers = [4, 17, 9, 3, 21, 6]
largest = reduce(lambda x, y: x if x>y else y, numbers)
print(largest)
print("THE END")
# without lambda function
def largest_no(x, y):
    if x>y:
        return x
    else:
        return y
numbers = [4, 17, 9, 3, 21, 6]
result = reduce(largest_no, numbers)
print(result)