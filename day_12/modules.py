#1 buhui
import random
import string

def random_user_id():
    characters = string.ascii_lowercase + string.digits
    user_id = ''
    for i in range(6):
        user_id += random.choice(characters)
    return user_id
print(random_user_id())
#2 buhui#不接受参数，所以input应放在函数内
def user_id_gen_by_user():#input() 得到的是字符串，需要int()
    number1=int(input('Enter string number:'))
    number2 =int(input('Enter id number:'))
    characters = string.ascii_letters + string.digits
    # user_id = ''#应放在外层循环中，不然每次循环不会清空
    ids= []#用列表储存数据
    for i in range(number2):
        user_id = ''
        for j in range(number1):
            user_id += random.choice(characters)
        ids.append(user_id)
    # return user_id 只返回一个值
    return '\n'.join(ids)#.join(ids)表示：用前面的字符串，把 ids 里的多个字符串连接起来。
                         #把 ids 列表里的所有 ID 用换行连接成一个大字符串，然后返回。
                         #join() 是字符串的方法，不是列表的方法。点号必须放在字符串后面
print(user_id_gen_by_user())

# append() 是列表的方法，而且它返回 None，所以不要写 x = x.append(...)。
# append() 的作用是：直接把 color 加到 colors 这个列表末尾
# tuple () 和字符串都没有 .append()；要追加内容通常用 list []。
# random.choice(...) 是 random 模块的方法，不是字符串自己的 .choice()。
# randint(0, 255) 如果想得到 RGB 三个不同的随机数，要放进循环里重新执行。
# for i in number 只有 number 可迭代时才行；如果 number 是整数，要用 range(number)。
# print(function_name) 打印的是函数本身；要执行函数得写 print(function_name())。
#3
from random import randint
# def rgb_color_gen():
#     numbers  = randint(0,255)#这样写只会循环一次，应放到循环里
#     rgb = ()
#     for i in range(3):
#         rgb = rgb.append(numbers) #rgb是tuple,没有.append()方法，应用list
#     return rgb
# print('rgb', rgb_color_gen())
def rgb_color_gen():
    red = randint(0,255)
    green = randint(0, 255)
    blue = randint(0, 255)
    return f'rgb({red},{green},{blue})'
print(rgb_color_gen())
'Or'
def rgb_color_gen():
    rgb = []
    for i in range(3):
        rgb.append(randint(0,255))
    return f'rgb({rgb[0],rgb[1],rgb[2]})'
#level two 
#1 buhui
def list_of_hexa_colors():
    color = '#'
    characters = '0123456789abcdef'
    for i in range(6):
        # color = color + string.choice()# 字符串没有 .choice()
        color += random.choice(characters)
    return color
print(list_of_hexa_colors())
"题目要求数组"
def list_of_hexa_colors(number):
    colors = []
    characters = '0123456789abcdef'
    for i in range(number):
        color = '#'
        for j in range(6):
            color += random.choice(characters)
        colors.append(color)
    return colors
#2 buhui
# def list_of_rgb_colors(number):
#     rgb = ()#改为[]
#     numbers  = randint(0,255)
#     color = []
#     for i in range(number):
#         for j in range(3):
#             rgb = rgb.append(numbers) #tuple不可以.append()
#             color = color.append(rgb) #append() 返回 None
#     return '\n'.join(color)
# print(list_of_rgb_colors)
def list_of_rgb_colors(n):
    colors = []
    for i in range(n):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        colors.append(f'rgb({r},{g},{b})')
    return colors

#3 有小函数以后，可以用它们组合成更大的函数
def generate_colors(type,numbers):
    string_hexa = '0123456789abcdef'
    string_rgb = randint(0,255)
    # hexa_color = '#' #需放在外层循环中，不然会复用
    color = []
    if type == 'hexa':
        for i in range(numbers):
            hexa_color = '#'
            for j in range(6):
                hexa_color = hexa_color + random.choice(string_hexa)
                color.append(hexa_color)
        return color
    elif type == 'rgb':
        return list_of_rgb_colors(numbers)
print(generate_colors())
"Or"
def generate_colors(color_type, number):
    if color_type == 'hexa':
        return list_of_hexa_colors(number)

    elif color_type == 'rgb':
        return list_of_rgb_colors(number)

    else:
        return 'Invalid color type'

#level three
#1 不会
# def shuffle_list(items):
#     set_random = set(items) #set的作用是去重，不是随机排序
#     items_random = list(set_random)
#     return items_random
def shuffle_list(items):
    new_items = items.copy()
    random.shuffle(new_items)
    return new_items

#2 buhui
# def random_numbers():
#     string_numbers = '0123456789'
#     number = ()
#     for i in range(7):
#         number_elect = random.choice(string_numbers)
#         string_numbers = string_numbers.remove(number_elect)#字符串没有 .remove()
#         number = number.append(number_elect)#tuple没有.append
#     return number
# print(random_numbers())
def random_numbers():
    numbers = range(10)
    result = random.sample(numbers, 7)

    return result
# return random.sample(range(10), 7)
print(random_numbers())

# random.choice(...)是随机选一个；
# random.randint(0, 255)是随机生成一个整数；
# random.shuffle(...)是随机打乱列表；
# random.sample(..., 7)是随机选 7 个不重复的元素
    
