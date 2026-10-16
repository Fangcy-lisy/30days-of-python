"""
#1、#2、#4、#13、#14、#15 基本正确；
主要问题集中在 #3、#5、#6~#12。
其中有几个非常典型的初学者错误: return 缩进位置、把数学公式直接写进 Python、
append()/remove() 的返回值，以及把 list 当成有 .upper() 方法。
1. return 一执行，函数立刻结束

2. list 没有 .upper()
   要对列表里的每个字符串调用 .upper()

3. append() / remove()
   会修改列表，但返回 None

4. 数学公式不能原样抄进 Python
   b²      → b ** 2
   4ac     → 4 * a * c
   2a      → 2 * a
"""
#1 
def add_two_numbers(
    number_one, number_two
):
    total = number_one + number_two
    return total #简化写法 return number_one + number_two
#2
def area_of_circle(radius: float)->float:
    area = 3.14 * radius * radius 
    return area
#3
# def add_all_nums1(*number):
#     if type(number) is not int:
#         print('number is not right')
#     else:
#         total = number + 
        
def add_all_nums(*numbers):
    total = 0
    for number in numbers:
        if not isinstance(number,(int, float)):
            return 'All arguments must be numbers.'
            
        total += number
    return total

#4 
def convert_celsius_to_fahrenheit(temperature_Celsius: int)->float: 
    temperature_Fahrenheit = (temperature_Celsius * 9/5) + 32
    return temperature_Fahrenheit

#5
spring = [3, 4, 5]
summer = [6,7,8]
autumn = [9,10,11]
winter = [12,1,2]
def check_season(month:int):
    if month in spring:
        return "spring"
    elif month in summer:
        return "summer"
    elif month in autumn:
        return "autumn"
    elif month in winter:
        return "winter"

#6 buhui
# def calculate_slope():
def calculate_slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

#7 错误
# def solve_quadratic_eqn(ax² + bx + c = 0):
#     answer_one = (-b*2-(b*2-4ac)*0.5)/2a
#     answer_two = (-b*2+(b*2-4ac)*0.5)/2a
# return answer_one
# return answer_two
def solve_quadratic_eqn(a, b, c):
    answer_one = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
    answer_two = (-b - (b**2 - 4*a*c)**0.5) / (2*a)

    return answer_one, answer_two

#8
# def print_list(list):
#     for item in items: #in list  不要把变量叫 list，因为是 Python 内置类型。
#         print(item)
def print_list(items):
    for item in items:
        print(item)

#9 buhui
# def reverse_list(items):
#     for item in items:
def reverse_list(items):
    reversed_items = []

    for i in range(len(items) - 1, -1, -1):
        reversed_items.append(items[i])

    return reversed_items

#10 buhui
# def capitalize_list_items(list):
#     list_upper = list.upper()  #list.upper() 不存在，.upper() 是字符串的方法
#     print(list_upper)
def capitalize_list_items(items):
    upper_items = []

    for item in items:
        upper_items.append(item.upper())

    return upper_items

#11 buhui
# def add_item(list, parameter):
#     list_append = list.append() #放入要添加的东西 append()本身返回None，应先修改，再返回列表
#     return list_append
def add_item(items, parameter):
    items.append(parameter)
    return items

#12 buhui
# def remove_item(list, parameter):
#     list_remove = list.remove(parameter) #remove() 也会修改原列表，返回值也是None。list_remove得到None
#     return list_remove
def remove_item(items, parameter):
    items.remove(parameter)
    return items


#13
def sum_of_numbers(number):
    total = 0
    for i in range(number+1):
        total += i
    return total

#14
def sum_of_odds(number):
    total = 0
    for i in range(number+1):
        if i % 2 != 0:
            total += i
    return total

#15
def sum_of_even(number):
    total = 0
    for i in range(number+1):
            if i % 2 == 0:
                total += i
    return total

   



