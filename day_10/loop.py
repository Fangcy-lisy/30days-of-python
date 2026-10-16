#level one
#1
i = 0
while i <= 10:
    print(i)
    i = i + 1

for i in range(0, 11):#(0,11)我这里只是一个tuple 应为range(0,11)
    print(i)
    # i = i + 1#i = i + 1在 for 循环里也不需要。因为 for 会自动把下一个值赋给 i。

#2 butaihui
i = 10
while i >= 0:
    print(i)
    i = i - 1
#buhui
for i in range(10, -1, -1):
    print(i)

#3
i = 1
while i <= 7:
    print(i * '#')
    i = i+1

#4 buhui cuowu
for x in range(8,9): #忘记range
    for i in range(1, 9):
        print(x * '#')

for x in range(8):
    for i in range(8):
        print('#', end = '') #打印完 # 不换行，只加一个空格。
    print() #换到下一行 #print()缩进的话，生成64个#

#5 
for i in range(0,11):
    for j in range(0,11):
        if j == i:
            print(f'{i} x {j} = {i * j}')
            # print('i x j = ' i * j)#应使用占位符，这个会真的打印字母 i 和 j

#6
list_1 = ['Python', 'Numpy','Pandas','Django', 'Flask']
length = len(list_1)
i = 0
while i < length:
    print(list_1[i])
    i = i+1

for i in range(0, length):
    print(list_1[i])
# 更常见、更简单的写法是：
# for item in list_1: 遍历列表
# print(item)

#7
for i in range(0,101):
    if i % 2 == 0:
        print(i)

#8
for i in range(0,101):
    if i % 2 != 0:
        print(i)

#level two
#1 buhui  用一个变量不断累加
total = 0
for i in range(0,101):
    total = total + i
print(f'The sum of all numbers is {total}.')

#2
total_odd = 0
for i in range(0,101):
    if i % 2 != 0:
        total_odd = total_odd + i
print(f'The sum of all odd numbers is {total_odd}.')
total_even = 0
for i in range(0,101):
    if i % 2 == 0:
        total_even = total_even + i
print(f'The sum of all odd numbers is {total_even}.')
#简化写法：
# for i in range(0, 101):
#     if i % 2 == 0:
#         even_sum += i
#     else:
#         odd_sum += i

#level three
#1 使用文件方法
from countries import countries
for i in countries:
    if 'land' or 'Land' in i:
        print(i)


#2 buhui 和求和思路一样，创建一个空的，再累加
fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []
for i in range(3,-1,-1):
    reversed_fruits.append(fruits[i])
print(reversed_fruits)

#3
from countries_data import countries_data
#1 先创建一个空的，再累加，这题适合用集合去重
languages = set()
for i in countries_data:
    for j in countries_data['language']:
        languages.append(j)
print('语言总数：', len(languages))

#2 buhui
language_count = {}
for country in countries:
    for language in country['languages']:
        if language in language_count:
            language_count[language] += 1
        else:
            language_count = 1

most_used_language = max(
    language_count, 
    key=language_count.get
)

print(most_used_language)
print(language_count[most_used_language])

#3 buhui
def get_population(country):
    return country['population']


sorted_countries = sorted(
    countries_data,
    key=get_population,
    reverse=True
)

top_10 = sorted_countries[:10]

for country in top_10:
    print(country['name'], country['population'])


    