import sys

a, b, c = map(int, input("Enter three sides of the triangle: ").split())

if a > 10 or b > 10 or c > 10:
    print("Out of range")
    sys.exit(0)

if a < b + c and b < a + c and c < a + b:
    if a == b == c:
        print("Equilateral triangle")
    elif a == b != c or a!= b == c or a == c!=b:
        print("Isosceles")
    else:
        print("Scalene triangle")
else:
    print("Invalid input")
