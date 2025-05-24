# problem 1  odd and even number
num = int(input("Enter a number"))
if (num % 2==0):
    print("the number is even")
else:
    print("the number is odd")

#problem  2   which is the greater number
a = int(input("Enter a number a: "))
b = int(input("Enter a number b: "))
c = int(input("Enter a number c: "))
if (a > b and a > c):
    print("a is greater")
elif (b > a and  b > c):
    print("b is greater")
else:
    print("c is greater")

#problem 3 which is the leap year
year = int(input("Enter a year"))

if(year % 400 == 0):
    print("This year is a leap year")
elif(year % 100 == 0):
    print("This year is not a leap year")
elif(year % 4==0):
    print("This year is a leap year")
else:
    print("This year is not a leap year")
# pronlem 4 Input a number n, and print the sum of first n natural numbers (i.e., 1 + 2 + 3 + ... + n)
n=int(input("Enter a number: "))
sum = 0
i = 0
while i<=n:
    sum = sum + i
    i +=1
print(sum)
# problem 5 Input a number n, print its factorial (e.g., 5! = 120)
n = int(input("Enter a number: "))
fact = 1
i = 1
while i<=n:
    fact = fact * i
    i += 1
print(fact)

# problem 6: Input a string and check if it's a palindrome (reads the same backwards).
string = input("Enter a string")
reverse = string[::-1]
if string == reverse:
    print("Its a palindrome")
else: 
    print("Its not a palindrome")
# problem 7 Input a number and print its reverse (e.g., 123 → 321)
num = input("Enter a number")
reverse = num[::-1]
print(reverse)
# problem 8 Find the Largest Digit in a Number
num = input("Enter a number")
largest = 0
for digit in num:
    digit_int = int(digit)
    if  digit_int > largest:
        largest = digit_int
print("the largest digit is ", largest)
# problem 9 Count Vowels in a String Input a string and count how many vowels are in it.
sentence = input("Enter a sentance ")
vowels = "aeiou"
count = 0
for ch in sentence:
    if ch in vowels:
        count +=1
print("Number of vowels", count)
# problem 10 Count the Digits in a Number
num = input("Enter a string")
count = 0
for digit in num:
    count +=1
print(count)