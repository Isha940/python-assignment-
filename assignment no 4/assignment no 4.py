# 1. Write a Python program to check whether a number is even or odd. 
# num = int(input("Enter a number: "))

# if num % 2 == 0:
#     print("Even Number")
# else:
#     print("Odd Number")

# 2. Write a program to find the largest of three numbers
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# if a >= b and a >= c:
#     print("Largest number is:", a)
# elif b >= a and b >= c:
#     print("Largest number is:", b)
# else:
#     print("Largest number is:", c)

# 3. Write a program to check whether a given number is prime.
# num = int(input("Enter a number: "))

# if num <= 1:
#     print("Not a Prime Number")
# else:
#     for i in range(2, num):
#         if num % i == 0:
#             print("Not a Prime Number")
#             break
#     else:
#         print("Prime Number")

# 4. Write a program to print the Fibonacci series up to n terms. 
# n = int(input("Enter number of terms: "))

# a = 0
# b = 1

# for i in range(n):
#     print(a, end=" ")
#     c = a + b
#     a = b
#     b = c

#  5. Write a program to find the factorial of a number using a loop. 
# num = int(input("Enter a number: "))

# fact = 1

# for i in range(1, num + 1):
#     fact = fact * i

# print("Factorial is:", fact)

# 6. Write a program to reverse a string without using [::-1].
# text = input("Enter a string: ")

# reverse = ""

# for i in text:
#     reverse = i + reverse

# print("Reversed string:", reverse)

# 7. Write a program to check whether a string is a palindrome.
# text = input("Enter a string: ")

# reverse = ""

# for i in text:
#     reverse = i + reverse

# if text == reverse:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")

# 8. Write a program to count the number of vowels and consonants in a string.
# text = input("Enter a string: ")

# vowels = 0
# consonants = 0

# for i in text:
#     if i.isalpha():
#         if i.lower() in "aeiou":
#             vowels = vowels + 1
#         else:
#             consonants = consonants + 1

# print("Vowels:", vowels)
# print("Consonants:", consonants)

# 9. Write a program to find the sum of all elements in a list. 
# numbers = [10, 20, 30, 40, 50]

# total = 0

# for i in numbers:
#     total = total + i

# print("Sum of list elements:", total)

# 10. Write a program to find the largest and smallest element in a list without using max() or min().
# numbers = [10, 25, 5, 40, 15]

# largest = numbers[0]
# smallest = numbers[0]

# for i in numbers:
#     if i > largest:
#         largest = i

#     if i < smallest:
#         smallest = i

# print("Largest element:", largest)
# print("Smallest element:", smallest)

# 11. Write a program to remove duplicate elements from a list.
# numbers = [10, 20, 10, 30, 20, 40]

# new_list = []

# for i in numbers:
#     if i not in new_list:
#         new_list.append(i)

# print("Original list:", numbers)
# print("List after removing duplicates:", new_list)

# 12. Write a program to count how many times each element appears in a list using a dictionary.
# numbers = [10, 20, 10, 30, 20, 10]

# frequency = {}

# for i in numbers:
#     if i in frequency:
#         frequency[i] = frequency[i] + 1
#     else:
#         frequency[i] = 1

# print("Element frequency:", frequency)

# 13. Write a program to find the second-largest number in a list. 
# numbers = [10, 25, 40, 15, 30]

# largest = numbers[0]
# second_largest = None

# for i in numbers:
#     if i > largest:
#         second_largest = largest
#         largest = i
#     elif i != largest:
#         if second_largest is None or i > second_largest:
#             second_largest = i

# print("Largest number:", largest)
# print("Second largest number:", second_largest)

# 14. Write a program to sort a list without using sort() or sorted(). 
# numbers = [40, 10, 30, 20, 50]

# for i in range(len(numbers)):
#     for j in range(i + 1, len(numbers)):
#         if numbers[i] > numbers[j]:
#             numbers[i], numbers[j] = numbers[j], numbers[i]

# print("Sorted list:", numbers)

# 15. Write a function that accepts a list of numbers and returns a list containing only the even numbers.
# def even_numbers(numbers):
#     even = []

#     for i in numbers:
#         if i % 2 == 0:
#             even.append(i)

#     return even


# numbers = [10, 15, 20, 25, 30, 35]

# result = even_numbers(numbers)

# print("Even numbers:", result)

# 16. Write a program to find the frequency of each character in a string. 
# text = input("Enter a string: ")

# frequency = {}

# for i in text:
#     if i in frequency:
#         frequency[i] = frequency[i] + 1
#     else:
#         frequency[i] = 1

# print("Character frequency:", frequency)

# 17. Write a program to check whether two strings are anagrams of each other. 
# str1 = input("Enter first string: ")
# str2 = input("Enter second string: ")

# str1 = str1.lower().replace(" ", "")
# str2 = str2.lower().replace(" ", "")

# if sorted(str1) == sorted(str2):
#     print("Strings are Anagrams")
# else:
#     print("Strings are Not Anagrams")

# 18. Write a program to find all duplicate values in a list. 
# numbers = [10, 20, 30, 10, 40, 20, 50]

# duplicates = []

# for i in numbers:
#     if numbers.count(i) > 1 and i not in duplicates:
#         duplicates.append(i)

# print("Duplicate values:", duplicates)

# 19. Write a program that takes a sentence and finds the longest word. 
# sentence = input("Enter a sentence: ")

# words = sentence.split()

# longest = ""

# for i in words:
#     if len(i) > len(longest):
#         longest = i

# print("Longest word:", longest)
# print("Length:", len(longest))

# 20. Create a simple student marks program that: 
# a. accepts marks for 5 subjects,
# b. calculates the total and percentage,
# c. assigns a grade,and displays whether the student passed or failed.
marks = []

for i in range(5):
    m = int(input("Enter marks: "))
    marks.append(m)

total = sum(marks)

percentage = total / 5

print("Total marks:", total)
print("Percentage:", percentage, "%")

if any(m < 35 for m in marks):
    print("Result: Fail")
    print("Grade: F")

elif percentage >= 90:
    print("Grade: A")
    print("Result: Pass")

elif percentage >= 75:
    print("Grade: B")
    print("Result: Pass")

elif percentage >= 60:
    print("Grade: C")
    print("Result: Pass")

elif percentage >= 35:
    print("Grade: D")
    print("Result: Pass")
