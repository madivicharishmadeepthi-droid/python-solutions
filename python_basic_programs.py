# Python Basic Programs
# Solutions from the uploaded question sheet

# 1. Largest of Three Numbers
a = int(input())
b = int(input())
c = int(input())

if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)


# 2. Check Leap Year
year = int(input())

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")


# 3. Vowel or Consonant
ch = input()

if ch in "aeiouAEIOU":
    print("Vowel")
else:
    print("Consonant")


# 4. Divisible by Both 5 and 11
n = int(input())

if n % 5 == 0 and n % 11 == 0:
    print("Divisible")
else:
    print("Not Divisible")


# 5. Sum of First N Natural Numbers Using while
n = int(input())

i = 1
sum = 0

while i <= n:
    sum += i
    i += 1

print(sum)


# 6. Multiplication Table Using while
n = int(input())

i = 1

while i <= 10:
    print(n, "x", i, "=", n * i)
    i += 1


# 7. Pyramid Pattern
# Output:
#    *
#   ***
#  *****
# *******

for i in range(1, 5):
    print(" " * (4 - i) + "*" * (2 * i - 1))


# 8. Number Pattern
# Output:
# 1
# 12
# 123
# 1234
# 12345

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()
