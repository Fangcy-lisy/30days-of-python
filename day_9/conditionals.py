# level one
#1 important: input()永远返回字符串 str。
user_age = int(input('Enter your age: ')) #mistake1: int
if user_age >= 18:
    print('You are old enough to learn to drive.')
else:
    missing_years = 18 - user_age
    print(f'You need {missing_years} more years to learn to drive.') #mistake2: 18 - user_age
#2
my_age = 23
your_age = int(input('Enter your age: '))#mistake3:int
if my_age > your_age:
    # if my_age - your_age == 1: 
        # print('year')#输出内容不完整
    # else:
            # print('years')
    difference = my_age - your_age
    if difference == 1:
        print(f'I am {difference} year older than you.')
    else:
        print(f'I am {difference} years older than you.')
elif my_age < your_age:
    # if your_age - my_age == 1:
    #     print('year')#same mistake
    # else:
    #     print('years')
    difference = your_age - my_age

    if difference == 1:
        print(f'You are {difference} year older than me.')
    else:
        print(f'You are {difference} years older than me.')
else:
    print("We're same old.")
#3
a = int(input('Enter number one: '))#mistake4:int
b = int(input('Enter number two: '))
if a > b:
    print(f'{a} is greater than {b}')#mistake5:应使用占位符
elif a < b:
    print(f'{a} is smaller than {b}')
else:
    print(f'{a} is equal to {b}')

#level two
#1
point = int(input("Enter student's grade: "))#mistake6:int
if point <= 100 and point >= 90:#可以简化：if 90 <= point <= 100:
    print('A')
elif point < 90 and point >= 80:
    print('B')
elif point < 80 and point >= 70:
    print('C')
elif point < 70 and point >= 60:
    print('D')
else:
    print('F')
#2
month = int(input('Enter month number: '))#mistake7:int

if month == 9 or month == 10 or month == 11:
    print("It's autumn")
elif month == 12 or month == 1 or month == 2:
    print("It's winter")
elif month == 3 or month == 4 or month == 5:
    print("It's spring")
elif month == 6 or month == 7 or month == 8:
    print("It's summer")
#输入月份名称
month = input('Enter month: ')

if month in ['September', 'October', 'November']:
    print("It's autumn")
elif month in ['December', 'January', 'February']:
    print("It's winter")
elif month in ['March', 'April', 'May']:
    print("It's spring")
elif month in ['June', 'July', 'August']:
    print("It's summer")
#3
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit_check = input("Enter the fruit: ")
if fruit_check not in fruits:
    fruits.append(fruit_check)
    print(fruits)
else:
    print('That fruit already exists in the list')

#level three
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
# if skills in person:# Python 会把：skills理解成一个变量。应修改为'skills'
    # print(person['skills'](len(int(person['skills'])/2)))#mistake8:person['skills']得到列表，需用[]索引
    # print('Python' in person['skills'])
if 'skills' in person:
    middle = len(person['skills']) // 2
    print(person['skills'][middle])
    print('Python' in person['skills'])
    
#这种写法意思是：skills 必须刚好等于['JavaScript', 'React']，而且顺序也要一样。
# if person['skills'] == ['JavaScript', 'React']:#mistake9:忘记了冒号
#     print('He is a front end developer')
# elif person['skills'] == ['Node', 'Python', 'MongoDB']:
#     print('He is a backend developer')
# elif person['skills'] == ['React', 'Node', 'MongoDB']:
#     print('He is a fullstack developer')
# else:
#     print('unknown title')
skills = person['skills']
if 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
    print('He is a fullstack developer')

elif 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
    print('He is a backend developer')


if person['is_married'] == True and person['country'] == 'Finland':
    print('Asabeneh Yetayeh lives in Finland. He is married.')
    print(f"{person['first_name']} {person['last_name']}" f'lives in {person['country']}. He is married.')


