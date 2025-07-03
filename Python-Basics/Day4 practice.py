# problem 1 Given a string of digits, find the number of digits that are strictly less than the digit immediately to their right.
num = "1537426"
count = 0
for i in range(len(num)-1):
    current_digit = int(num[i])
    next_digit = int(num[i + 1])
    if current_digit < next_digit:
        count += 1
print(count)
print("THE END")
# problem 2 Given a number as a string (e.g., "97531"), check if each digit is less than or equal to the previous one. If they are, print "Digits are in decreasing order"; otherwise, print "Digits are not in decreasing order".
num = "97531"
for i in range(len(num)-1):
    privious_digit = int(num[i])
    current_digit = int(num[i + 1])
    if current_digit >= privious_digit:
        print("digit are not in decsreasing order")
        break
else:
    print("digits are in decreasing order")
print("THE END")
# problem 4 Given a string of digits (e.g., "5392710"), find the largest difference between any two digits in the number, regardless of position.

num = "5392710"
digit = []
for i in num:
    digit.append(int(i))
    max_digit = max(digit)
    min_digit = min(digit)
    max_possible_diff = max_digit - min_digit
print("Maximum difference is: ", max_possible_diff)
print("THE END")
# problem 5 Given a string of digits (e.g., "12233445"), create a list of digits that appear only once in the string.
num = "12233445"
frequency = {}
for digit in num:
    if digit in frequency:
        frequency[digit] +=1
    else:
        frequency[digit] = 1

print(frequency)
unique_digit = []
for digit in frequency:
    if frequency[digit] == 1:
        unique_digit.append(digit)
print("unique digit:", unique_digit)
print("THE END")
# problem 6 Given a string of digits (e.g., "122345544"), find the digit(s) that occur the most number of times. If multiple digits have the same highest frequency, return all of them as a list.
num = "112233"
frequency = {}
for digit in num:
    if digit in frequency:
        frequency[digit] +=1
    else:
        frequency[digit] = 1
print(frequency)
max_val = max(frequency.values())
print(max_val)
most_frequent_digit = []
for digit in frequency:
    if frequency[digit] == max_val:
        most_frequent_digit.append(digit)
print(most_frequent_digit)
print("THE END")
# problem 7 Given a string of digits (e.g., "2301"), replace each digit with its corresponding word using a dictionary. Example: Input: "2301" → Output: "two three zero one" digit)
digit_words = {
    '0' : 'zero',
    '1' : 'one',
    '2' : 'two',
    '3' : 'three',
    '4' : 'four',
    '5' : 'five',
    '6' : 'six',
    '7' : 'seven',
    '8' : 'eight',
    '9' : 'nine'
}
num = "2301"
word = []
for digit in num:
    word.append(digit_words[digit])
    join_words = " ".join(word)
print(join_words)
# problem 8 Given a string of digits (like "5081"), convert each digit to its word form using a dictionary, and join the words with hyphens (-).
digit_words = {
    '0' : 'zero',
    '1' : 'one',
    '2' : 'two',
    '3' : 'three',
    '4' : 'four',
    '5' : 'five',
    '6' : 'six',
    '7' : 'seven',
    '8' : 'eight',
    '9' : 'nine'
}
num = "5081"
word = []
for digit in num:
    word.append(digit_words[digit])
    join_words = " - ".join(word)
print(join_words)
print("the end")
# problem 9 Given a string of digits (e.g., "1532"), find the product of all digits except the largest digit. If the largest digit occurs more than once, exclude only one of them.
num = "1532"
digits = []
for d in num:
    digits.append(int(d))
print(digits)
max_digit = max(digits)
digits.remove(max_digit)
product =1 
for d in digits:
    product *= d
print(product)