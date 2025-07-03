# Given a number as a string (e.g., "1537426"), count how many digits are greater than the digit that comes before them.
num = "1537426"
count = 0
for i in range(1, len(num)):
    current_digit = int(num[i])
    previous_digit= int(num[i-1])
    if current_digit > previous_digit:
        count +=1
    else:
        print(f"{current_digit} is not greater than {previous_digit}")
print("Count of digits greater than previous: ", count)
print("THE END")
# problem 2 Given a number as a string (e.g., "1234"), check if each digit is greater than or equal to the previous one. If they are, print "Digits are in increasing order"; otherwise, print "Digits are not in increasing order".
num = "1234"
for i in range(1, len(num)):
    current_digit = int(num[i])
    previous_digit = int(num[i - 1])
    if current_digit <= previous_digit:
        print("digits are not increasing order")
        break
else:
    print("digits are in incresing order")
print("THE END")
# PROBLEM 3 Given a number as a string (e.g., "5392710"), find the largest absolute difference between any two consecutive digits.
num = "5392710"
differences = []
for i in range(0, len(num)-1):
    current_digit = int(num[i])
    next_digit = int(num[i+1])
    consecutive_difference = abs(current_digit - next_digit)
    differences.append(consecutive_difference)
max_diff = max(differences)
print("Maximum difference is", max_diff)
print("THE END")
# problem 4 Given a string of digits (e.g. "1223334444"), find the digit that appears consecutively the most times in a row, and how many times it appears in that sequence.
num = "1223334444"
current_digit = num[0]        # Start with the first digit ('1')
current_count = 1             # We’ve seen '1' once so far

for i in range(len(num)-1):   # Loop through the string till the second last digit
    if num[i + 1] == current_digit:
        current_count += 1    # Same digit again → increase count
    else:
        print(f"{current_digit} appears {current_count} times")  
        # We encountered a **new digit**, so print how many times the current one occurred

        current_digit = num[i + 1]  # Update current_digit to the new digit
        current_count = 1          # Reset count to 1 for the new digit

# After the loop ends, the last digit group hasn’t been printed yet:
print(f"{current_digit} appears {current_count} times")
print("THE END")
# problem 5 Given a string of digits, remove consecutive duplicate digits.
num = "12233444"
perivous_digit= num[0]
result = num[0]
for i in range(len(num)-1):
    if num[i + 1] != perivous_digit:
        result += num[i + 1]     
    perivous_digit = num[i + 1]
print(result)
print("THE END")
# problem 6 Given a string of digits, insert a dash (-) between two even digits.
num = "124364"
result = num[0]
for i in range(len(num)-1):
    current_digit = int(num[i])
    next_digit = int(num[i + 1])
    if (current_digit%2 ==0 and next_digit % 2 ==0):
        result += "-" + num[i+1]
    else:
        result += num[i + 1]
print(result)
print("THE END")
# problem 7 Given a string of digits, count how many substrings are palindromes.
num = "12321"
count = 0
for start in range(len(num)):
    for end in range(start + 1, len(num)+ 1):
        substring = num[start:end]
       # print(substring) it will print all the substrings
        if substring == substring[::-1]:
            count+=1
print("Total palindrome substrings: ", count)
print("THE END")
# problem 8 Given a string of digits, check whether it is a balanced number.
# A number is considered balanced if the sum of digits on the left half is equal to the sum of digits on the right half. If the number has an odd length, ignore the middle digit.
num = "1230321"
mid = len(num) // 2
if len(num)%2 ==0:
    left = num[: mid]
    right = num[mid :]
else:
    left = num[: mid]
    right = num[mid+1:]
left_reverse =left [::-1]
if left_reverse == right:
    print("yes it is a special [palindrom]")
else:
    print("No its not")

print("The End")
# problem 9 Given a string of digits, check if the sum of its digits is a prime number.
num = "2351"
sum = 0
for i in range(len(num)):
    digit = (num[i])
    sum += int(digit)
if sum < 2:
    print("not a prime number")
else:
    for i in range(2, sum):
        if sum % i == 0:
            print(f"{sum} is not a prime number")
    else:
        print(f"{sum} is a prime number")
print("THE END")
# problem 10 Given a string of digits, find the digit that appears the most number of times. If multiple digits have the same highest frequency, return the smallest one among them.
num = "1223344555666"
frequency = {}
for digit in num:
    if digit in frequency:
        frequency[digit] +=1
    else:
        frequency[digit] = 1
print(frequency)
max_count = max(frequency.values())
most_frequent_digit = []
for digit, count in frequency.items():
    if count ==max_count:
        most_frequent_digit.append(int(digit))
        result = min(most_frequent_digit)
print("Most frequent digit is:", result)
print("The End")