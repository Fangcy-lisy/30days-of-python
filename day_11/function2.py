#level two
#1 错误
def evens_and_odds(number:int):
    total_evens = 0
    total_odds = 0
    for i in range(number+1): #number是整数，不可以遍历
        if i % 2 == 0:
            total_evens += 1
        else:
            total_odds += 1
    print(f'The number of evens is {total_evens}.')
    print(f'The number of odds is {total_odds}.')

#2 cuowu
def factorial(number:int):
    # calculate = number**number #5的阶乘
    # return calculate
    result = 0
    for i in range(1, number + 1):
        result *= 1

#3 cuowu
# def is_empty(parameter):
#     for i in parameter:
#         print(i)
#     else:
#         print("It's empty")
def is_empty(parameter):
    if len(parameter) == 0:
        return True
    else:
        return False  
#其他写法 if not parameter: return True Or return not parameter

#4 buhui 
def calculate_average(items):
    total = 0
    number = len(items)
    list_order = []
    for i in items:
        total += i
    print('平均数： ', total/number)#字符串和数字表达式之间没有连接符，属于语法错误

def calculate_median(items):
    sorted_items = sorted(items)# 用于列表、元组等可迭代对象
    length = len(sorted_items)
    middle = length // 2
    if length % 2 != 0:
        return sorted_items[middle]
    else:
        return (
            sorted_items[middle - 1] +
            sorted_items[middle]
        ) / 2

def calculate_mode(items):
    count = {}
    for item in items:
        if item in count:
            count[item] += 1
        else:
            count[item] = 1
    mode = max(count, key = count.get)
    return mode

def calculate_range(items):
    return max(items) - min(items)

def calculate_variance(items):
    mean = calculate_average(items)
    total = 0

    for item in items:
        difference = item - mean
        total += difference ** 2

    return total / len(items)

def calculate_std(items):
    variance = calculate_variance(items)
    return variance ** 0.5

#level three
#1 错误  质数：大于 1，并且除了 1 和自己以外没有其他因数。
# def is_prime(number:int):
#     if number % 2 != 0:
#         print(f'{number} is odds')
def is_prime(number: int):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

#2 buhui
# def is_only(items):
#     length = len(items)
#     count = 0
#     for item in items:
def is_only(items):
    return len(items) == len(set(items))

#3 buhui
# def is_same_type(items):
#     for item in items:
def is_same_type(items):
    if len(items) == 0:
        return True

    first_type = type(items[0])

    for item in items:
        if type(item) != first_type:
            return False

    return True

#4 buhui Python 字符串已经提供了：.isidentifier() 另外注意关键字
# def variable_check(parameter):
#     return parameter.isidentifier()
import keyword

def variable_check(parameter):
    return parameter.isidentifier() and not keyword.iskeyword(parameter)

#5
from countries_data import countries

#1
def the_most_spoken_languages(data, number):
    language_count = {}

    for country in data:
        for language in country['languages']:
            if language in language_count:
                language_count[language] += 1
            else:
                language_count[language] = 1 #重点理解：这一步会得到{English：1}

    def get_count(item):
        return item[1]

    sorted_languages = sorted(
        language_count.items(),#.items() 把字典中的每一组 key 和 value 组合成一个元组
        key=get_count,          #返回的是一个 dict_items 视图对象，不是普通列表。
        reverse=True     #把 get_count 这个函数交给 sorted()，让 sorted() 自己对每一个 item 调用它。
    )#不加reverse=True默认就是从小到大排序。

    return sorted_languages[:number]
#2
def get_population(country):
    return country['population']


def the_most_populated_countries(data, number):
    sorted_countries = sorted(  #sorted(data, key=函数名, reverse=True)
        data,
        key=get_population,
        reverse=True
    )

    return sorted_countries[:number]
print(the_most_populated_countries(countries,1))