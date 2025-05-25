# problem 1 Check if a number is prime
n = int(input("Enter a number"))
if n<=1:
    print("Its not a prime number")
i = 2
while i<n:
    if n%i==0:
        print("Its not a prime number")   
        break
    i += 1
else:
    print("its a prime number")
print("THE END")
# problem 2  Sum of Digits of a Number 123 (1+2+3)
num = input("Enter a number: ")
sum = 0
for ch in num:
    sum+=int(ch)
print(sum)
print("THE END")
# problem 3 Find the Product of Digits of a Number
num = input("Enter a number")
product = 1
for ch in num:
    product *=int(ch)
print(product)
print("THE END")
# problem 4 Count Even and Odd Digits in a Number
num = "123456"
even_count = 0
odd_count = 0
for ch in num:
    digit = int(ch)
    if digit % 2 ==0:
        even_count += 1
    else:
        odd_count += 1
print("Even digits:", even_count )
print("Odd digits:", odd_count)
print("THE END")
# problem 5 Reverse a Number Using a Loop (No slicing)
num = "123"
i = len(num) -1
reversed_num = ""
while i >=0:
    reversed_num += num[i]
    i -= 1
print(reversed_num)
print("THE END")
# Problem 6: Check if a Number is an Armstrong Number
num = "153"
num_of_digits = len(num)
sum = 0
for ch in num:
    digit = int(ch)
    power_digit = digit ** num_of_digits
    sum += power_digit
if sum == int(num):
    print("Armstrong number")
else:
    print("Not an armstrong number")
# problem 7 Given a number as a string, count how many digits in it are divisible by 3.
num = "6593"
counter = 0
for ch in num:
    digit = int(ch)
    check_divisible = digit % 3
    if check_divisible == 0:
        counter += 1
print(counter)
print("THE END")
# Problem 8: Sum of Digits at Even Index Positions
num = "123456"
sum = 0
for i in range(len(num)):
    if i % 2 == 0:
        digit = int(num[i])
        sum += digit
print(sum)
print("THE END")
# Problem 9: Count the Frequency of Each Digit. Given a number as a string, count how many times each digit appears in it.
num = "1123581321"
digit_count = {}
for ch in num:
    if ch in digit_count:
        digit_count[ch] +=1
    else:
        digit_count[ch] = 1
print(digit_count)
# problem 10 Given a number as a string (e.g., "1234"), check whether all the digits are unique — that is, no digit repeats.
num = "1234"
seen = set()
for ch in num:
    if ch in seen:
        print("its a duplicate")
        break
    seen.add(ch)
else:
     print("All digits are unique")