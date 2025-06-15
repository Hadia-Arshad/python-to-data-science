# Write a function square(num) that returns the square of a number.
def square(num):
    square = num**2
    return square
print(square(5))
# Write a function is_even(num) that returns True if the number is even, otherwise False.
def is_even(num):
    if num % 2 == 0:
        print("the number is even")
    else:
        print("the number is not even")
is_even(6)
#Write a function celsius_to_fahrenheit(c) that converts temperature from Celsius to Fahrenheit using the formula: °F=(°C×9/5)+32
def cel_to_fahr(c):
    cel_to_fahr= (c*9/5)+32
    return cel_to_fahr
print(cel_to_fahr(0))
#Write a function maximum(a, b) that returns the greater of two numbers.
def maximum(a, b):
    if a>b:
        return a
    else:
        return b
print(maximum(6, 8))
# Write a  function factorial(n) that returns the factorial of a given number n.
def fact(n):
    result = 1
    i = 1
    while i<=n:
        result *= i
        i +=1
    return result
print(fact(5))
#Write a function fibonacci(n) that returns the nth Fibonacci number. (Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, …)
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a = 0
    b = 1
    i = 2
    while i<=n:
        next = a + b
        a = b
        b = next
        i += 1
    return b

print(fibonacci(6))
# Write a function sum_of_digits(n) that returns the sum of digits of a number 
def sum_of_digits(num):
    sum = 0
    for digit in str(num):
        sum += int(digit)
    return sum
print(sum_of_digits("1122"))
# Write a function is_palindrome(s) that checks whether a given string is a palindrome or not.
def is_palindrome(s):
    s_reverse = s[::-1]
    if s_reverse == s:
        return True
    else: 
        return False
print(is_palindrome("maam"))
print("the end")
#You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps.
# Write a function count_ways(n) to return the number of distinct ways to climb to the top.
def count_ways(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n==2:
        return 2
    else:
        return count_ways(n - 1) + count_ways(n - 2)
print(count_ways(5))