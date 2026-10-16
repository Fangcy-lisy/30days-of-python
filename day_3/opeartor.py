print(not not True)  # True
print(not not False) # False
age = 23
height = 175.43
complex_num = 4 + 3j
#4
input_num1 = input("Enter the triangle base: ")
input_num2 = input("Enter the triangle height: ")
triangle_area = 0.5 * float(input_num1) * float(input_num2)
print("The area of the triangle is:", triangle_area)
#5
input_num3 = input("Enter the triangle side a: ")
input_num4 = input("Enter the triangle side b: ")
input_num5 = input("Enter the triangle side c: ")
perimeter = float(input_num3) + float(input_num4) + float(input_num5)
print("The perimeter of the triangle is:", perimeter)
#6 不熟
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
rectangle_area = length * width
rectangle_perimeter = 2 * (length + width)
print("The area of the rectangle is:", rectangle_area)
print("The perimeter of the rectangle is:", rectangle_perimeter)
#7
radius = float(input("Enter the radius of the circle: "))
circle_area = 3.14 * radius ** 2
circle_circumference = 2 * 3.14 * radius
print("The area of the circle is:", circle_area)    
print("The circumference of the circle is:", circle_circumference)
#8  不会
slope = 2
y_intercept = -2
x_intercept = 1
print(x_intercept, slope, y_intercept)
#9
point1 = (2, 2)
point2 = (6, 10)
m = (point2[1] - point1[1]) / (point2[0] - point1[0])
print("The slope of the line is:", m)
distance = ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5
print("The distance between the two points is:", distance)
#10
print(slope >= m)
# 不会
for x in range(-6,4):
     y = x**2 + 6*x + 9
     print("x =", x, "y =", y)

     if y == 0:
         print("The value of y when x =", x, "is:", y)
         break 

python_length = len('python')
dragon_length = len('dragon')
#11
print(python_length)
print(dragon_length)
print(python_length != dragon_length)
#12
print('on' in 'python' and 'on' in 'dragon')
#13
print('jargon' in 'I hope this course is not full of jargon')
#14
print('on' not in 'python' and 'on' not in 'dragon')
#15
length = len('python')
length_folat = float(length)
print(length_folat)
length_folat_str = str(length_folat)
print(length_folat_str)
#17buhui
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
#18buhui
print(7//3 == int(2.7))
#19
print(type('10') == type(10))
#20
print(int(float('9.8')) == 10)
#21
hours = int(input("Enter hours: "))
rate_per_hour = int(input("Enter rate per hour: "))
weekly_earnings = hours * rate_per_hour
print("The weekly earnings are:", weekly_earnings)
#22
years = int(input("Enter number of years you have lived: "))
seconds_lived = years * 365 * 24 * 60 * 60
print("You have lived for approximately", seconds_lived, "seconds.")
#23
print("1\t1\t1\t1\t1")
print("2\t1\t2\t4\t8")
print("3\t1\t3\t9\t27")
print("4\t1\t4\t16\t64")
print("5\t1\t5\t25\t125")
