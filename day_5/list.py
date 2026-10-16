# ages.sort()
# print(ages)
# print(ages.sort())
# None

#1
list_blank = []
#2
list_1 = [1, 2, 3, "fangchunyu", 'lishuyao', "forever" ]
#3
print(len(list_1))
#4 中间计算
print(list_1[0])
# 你的列表有 6 个元素，所以有两个中间元素
# print(list_1[len(list_1) // 2])
middle = len(list_1) // 2
print(list_1[middle - 1], list_1[middle])
print(list_1[-1])
#5
mixed_data_types = ['fangchunyu', 23, 178, "有老婆", "安徽滁州"]
#6
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
#7
print(it_companies)
#8
print(len(it_companies))
#9
print(it_companies[0])
print(it_companies[-1])
print(it_companies[len(it_companies) // 2])
#10buhui
it_companies[0] = 'Tencent'
print(it_companies)
#11buhui
it_companies.append('Uber')
#12buhui 
# it_companies.insert(3, 'Baidu')
# print(it_companies)
middle = len(it_companies) // 2

it_companies.insert(middle, "Baidu")
print(it_companies)
#13buhui cuo
# print(it_companies[0].upper()) # get TENCENT 只是打印了大写，没有修改列表
it_companies[0] = it_companies[0].upper()
print(it_companies)

#14 cuo
# str_1 = '#'
# print(it_companies + [str_1])

result = "#; ".join(it_companies)
print(result)

#15
print("Facebook" in it_companies)
#16buhui cuo
# print((it_companies).sort()) get None
it_companies.sort()
print(it_companies)
#17 cuo
# print((it_companies).reverse()) get None
it_companies.reverse()
print(it_companies)
#18 cuo
# print(it_companies.remove[0:3]) remove 不能切片
print(it_companies[:3])
#19 cuo
# print(it_companies.remove[-4:-1])
print(it_companies[-3:])
#20 cuo
# print(it_companies.remove[3:5])
n = len(it_companies)

if n % 2 == 0:
    print(it_companies[n // 2 - 1:n // 2 + 1])
else:
    print(it_companies[n // 2])
#21 cuo
# print(it_companies.remove[0])#remove() 删除的是“值”，不是索引
it_companies.pop(0)

print(it_companies)
#22 cuo
# print(it_companies.remove[3])
n = len(it_companies)

if n % 2 == 0:
    del it_companies[n // 2 - 1:n // 2 + 1]
else:
    del it_companies[n // 2]

print(it_companies)
#23 cuo
# print(it_companies.remove[-1])
it_companies.pop()

print(it_companies)
#24
print(it_companies.clear()) #清空是对的，但 print(clear()) 会打印 None
#25buhui cuo
# print(it_companies.pop())
del it_companies
#26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
joined = front_end + back_end
print(joined)

#27buhui cuo
full_stack = joined.copy()
# full_stack = front_end + back_end
# print(full_stack.append('Python', 'SQL'))append添加到最后面
index = full_stack.index('Redux')+1#a[i:i] = [...]   # 在索引 i 的位置插入多个元素
full_stack[index:index] = ["Python", "SQL"]#full_stack[5] = "Python"替换

print(full_stack)

#level 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# print(ages.sort()) get None
ages.sort()
print(ages)
print('最小年龄:', min(ages))
print('最大年龄:', max(ages))
# print(ages.append(min(ages)))
# print(ages.append(max(ages))) get None
ages.append(min(ages))
ages.append(max(ages))

print(ages)
#因为 append 之后列表顺序乱了，所以为了算中位数，重新排序：
ages.sort()
#年龄中位数不会
# print('中位数:', ages[len(ages) // 2])
median = (ages[5] + ages[6]) / 2
print(median)
#但不要硬写 5 和 6，应该动态计算：
n = len(ages)

if n % 2 == 0:
    median = (
        ages[n // 2 - 1] +
        ages[n // 2]
    ) / 2
else:
    median = ages[n // 2]

print("中位数:", median)
#可以用函数
# print('平均年龄:', (ages[0] + ages[1]+ ages[2]+ages[3]+ages[4]+ages[5]+ages[6]+ages[7]+ages[8]+ages[9])/10)
average = sum(ages) / len(ages)
print("平均年龄:", average)
print('年龄范围:', max(ages) - min(ages))
# print(abs(min(ages) - (ages[0] + ages[1]+ ages[2]+ages[3]+ages[4]+ages[5]+ages[6]+ages[7]+ages[8]+ages[9])/10) > abs(max(ages) - (ages[0] + ages[1]+ ages[2]+ages[3]+ages[4]+ages[5]+ages[6]+ages[7]+ages[8]+ages[9])/10))
average = sum(ages) / len(ages)
min_difference = abs(min(ages) - average)
max_difference = abs(max(ages) - average)
print(min_difference > max_difference)

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
];

print(len(countries))
print(countries[len(countries) // 2])
# countries_1 = countries[:len(countries) // 2]#notice第一组：97 第二组：98
# countries_2 = countries[len(countries) // 2:]
middle = (len(countries) + 1) // 2
countries_1 = countries[:middle]
countries_2 = countries[middle:]
print(len(countries_1))
print(len(countries_2))

countries_3 = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
# scandic_countries = countries_3[3:7]
China, RUssia, USA, *scandic_countries = countries_3
#a, b, *rest = [1, 2, 3, 4, 5]
