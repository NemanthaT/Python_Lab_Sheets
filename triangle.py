print("Enter the first side of the triangle: ")
fside=input()
print("Enter the second side of the triangle: ")
sside=input()
print("Enter the third side of the triangle: ")
tside=input()

if fside+sside>tside and sside+tside>fside and fside+tside>sside:
    print("The triangle is valid")

    if fside==sside and sside==tside:
        print("It is an equilateral triangle")

    elif fside==sside or sside==tside or fside==tside:
        print("It is an isosceles triangle")
    else:
        print("It is a scalene triangle")

else:
    print("Triangle is not valid")

# Path: circle.py
