#普通嵌套循环的压缩写法。
#1
# numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
# positive_num = [num for num in numbers if num>0]
# print(positive_num)

# #2
# list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
# flattened_list = [number for row in list_of_lists for num in row for number in num]
# print(flattened_list)

# #3 numbers = [(i, i * i) for i in range(11)]
# lst_tuple = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
# print(lst_tuple)

#4 不熟 解包
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened_list = [[country.upper(), country[:3].upper(),capital.upper()] 
                  for row in countries #理解for前面是想得到的结果
                  for country, capital in row]
print(flattened_list)

#5
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened_list = [{'country': country.upper(), 'city': city.upper()}
                  for row in countries
                  for country, city in row]
print(flattened_list)
#6 buhui
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
full_name = [f'{first_name} {last_name}' #'first_name' 有引号，Python 会把它当成固定字符串，故用f-string
             for row in names           #或者first_name + ' ' + last_name
             for first_name, last_name in row]
print(full_name)

#7 截距的写法
slope = lambda x1, y1, x2, y2: (y2 - y1)/(x2 -x1)
y_intercept = lambda x, y, m: y- m*x #点：(2, 7) 斜率：3
