#level one
#1~#3
'''
1.解释 map、filter 和 reduce 的区别:
reduce不返回另一个可迭代对象, 
map返回一个列表,
filter每个项目返回布尔值 
map     → 每一个都处理
filter  → 筛选
reduce  → 多个变一个
2.解释高阶函数、闭包和装饰器的区别。
高阶函数的特点是：函数可以接收另一个函数，或者返回一个函数。
闭包是：内部函数被返回以后，仍然记得外层函数中的变量。
装饰器是：接收一个函数，对它增加功能，再返回一个新函数。
3.定义调用函数，见示例
def add(a,b):
    return a+b
result=add(2,3)
print(result)
'''
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#4~6
for i in countries:
    print(i)
for i in names:
    print(i)
for i in numbers:
    print(i)

#level two
#1 
# map() 和 filter() 返回的不是普通 list，
# 直接 print() 时不会看到最终列表，需要用 list() 转换。
# countries_upper = map(.upper(), countries)
countries_upper = map(str.upper, countries)
print(countries_upper)
"Or"
countries_upper = map(
    lambda country: country.upper(), countries)

#2
num_double = map(lambda a:a**2, numbers)
# print(num_double)
print(list(num_double))

#3
names_upper = map(str.upper, names)
# print(names_upper)
print(list(names_upper))

#4 理解filter() 的判断函数最好直接返回True False
# def have_land(nation):
#     if 'land' in nation:
#         return nation

# nation_have_land = filter(have_land, countries)
# print(nation_have_land)
def have_land(nation):
    return 'land' in nation
nation_have_land = filter(have_land, countries)
print(list(nation_have_land))

#5
def name_long_6(nation):
    if len(nation) == 6:
        return nation
#更简洁
#  def name_long_6(nation):
#     return len(nation) == 6

nation_6_letter = filter(name_long_6, countries)
print(list(nation_6_letter))

#6
def name_long_6plus(nation):
    if len(nation) >= 6:
        return nation
# 推荐
# def name_long_6plus(nation):
#     return len(nation) >= 6
nation_6plus_letter = filter(name_long_6plus, countries)
print(list(nation_6plus_letter))

#7
def name_E(nation):
    if nation[0] == 'E':
        return nation
#推荐
# def name_E(nation):
#     return nation[0] == 'E'
nation_E = filter(name_E, countries)
print(list(nation_E))

#8 buhui
from functools import reduce

result = reduce(
    lambda x, y: x + y,
    filter(
        lambda x: x % 2 == 0,
        map(lambda x: x ** 2, numbers)
    )
)

print(result)

#9
def get_string_lists(lst):
    lst_str = []
    for i in lst:
        if type(i) == str:#更常用isinstance()
                           #if isinstance(item, str):
            lst_str.append(i)
    return lst_str
"Or"
def get_string_lists(items):
    return [item 
            for item in items 
            if isinstance(item, str)
            ]
#10
from functools import reduce
def add_two_nums(x, y):
    return x + y
sum_num = reduce(add_two_nums,numbers)
print(sum_num)

#11 mis
# countries[5] = 'and Iceland are north European countries'
# def connect_words(word1,word2):
#     return word1+','+word2
# sentence = reduce(connect_words,countries)
first_part = reduce(
    lambda x,y:x+', '+y,
    countries[:-1]
    )
sentence = (
    first_part
    + ', and '
    + countries[-1]
    + ' are north European countries.'
)

print(sentence)

#12 mis  让模式本身成为参数
# from countries import countries 
# def categorize_countries(nation):
#     return 'land' in nation
# countries_land = filter(categorize_countries,countries)

def categorize_countries(pattern):
    result = filter(
        lambda country: pattern.lower() in country.lower(),
        countries)
    return list(result)
#13 buhui
def count_countries_by_initial(countries):
    result = {}

    for country in countries:
        first_letter = country[0]

        if first_letter in result:
            result[first_letter] += 1
        else:
            result[first_letter] = 1

    return result

#14
def get_first_ten_countries():
    return countries[:10]

def get_first_ten_countries(countries):#推荐 因为函数不依赖外面的全局变量
    return countries[:10]
#15
def get_last_ten_countries():
    return countries[-10:]

#level three
from countries_data import countries
#1 reverse=True 表示倒序，所以国家名会按照： Z → A
def get_name(country):
    return country['name']
def nation_name_order(data):
    sorted_countries = sorted(
        data,
        key=get_name,
        #reverse = True
    )
    return sorted_countries
'Or'#简化
# def nation_name_order(data):
#     return sorted(data, key=get_name)

def get_city(country):
    return country['capital']
def capital_name_order(data):
    sorted_countries = sorted(
        data,
        key=get_city,
        # reverse = True
    )
    return sorted_countries
'Or'#简化
# def capital_name_order(data):
#     return sorted(data, key=get_city)

def get_population(population):
    return population['population']
def population_order(data):
    sorted_countries = sorted(
        data,
        key=get_population,
        reverse = True
    )
    return sorted_countries

#2
def languages_top10(data,num):
    language_count = {}

    for country in data:
        # for language in country:#遍历字典时得到的是 key
        for language in country['languages']:
            # if language in country['languages']:#判断对象写错了
            if language in language_count:
                # language_count['language'] += 1#'language' 是固定字符串。
                language_count[language] += 1
            else:
                language_count[language] = 1
    def get_count(items):
        return items[1]

    sorted_languages = sorted(
        language_count.items(),#忘记加()
        key= get_count,
        reverse=True
    )
    return sorted_languages[:num]

#3

# def get_population(population):前面定义过
#     return population['population']
def pop_top10(data,num):
    sorted_countries = sorted(
        data,
        key=get_population,
        reverse = True
    )
    population_top10 = sorted_countries[:num]#应改为num
    return population_top10


