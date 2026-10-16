#1
str_1 = 'Thirty'
str_2 = 'Days'
str_3 = 'Of'
str_4 = 'Python'
str_connection_1 = str_1 + ' ' + str_2 + ' ' + str_3 + ' ' + str_4
#2
str_5 = 'Coding'
str_6 = 'For'
str_7 = 'All'
str_connection_2 = str_5 + ' ' + str_6 + ' ' + str_7
#3
company = 'Coding For All'
#4
print(company)
#5  
print(len(company))
#6
print(company.upper())
#7
print(company.lower())
#8
print(company.capitalize())
print(company.title())
print(company.swapcase())
#9
print(company[0:6])
#10 buhui
print( company.find('Coding'))
#11 buhui
print(company.replace('Coding', 'Python'))
#12
text_1 = 'Python for Everyone'
print(text_1.replace('Everyone', 'All'))
#13
print(company.split())
#14
text_2 = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(text_2.split(', '))
#15
print(company[0])
#16 错误
#print(company[-1])
print(len(company) - 1)
#17
print(company[10])
#18 buhui
name = 'Python For Everyone'
words_1 = name.split()
first_letter = words_1[0][0]
second_letter = words_1[1][0]
third_letter = words_1[2][0]
acronym = first_letter + second_letter + third_letter
print(acronym)
#19
words_2 = company.split()
first_letter_2 = words_2[0][0]
second_letter_2 = words_2[1][0]
third_letter_2 = words_2[2][0]
acronym_2 = first_letter_2 + second_letter_2 + third_letter_2
print(acronym_2)
#20
print(company.index('C'))
#21
print(company.index('F'))
#22
text_3 = 'Coding For All People'
print(text_3.rfind('l'))
#23
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.index('because'))
#24
print(sentence.rindex('because'))
#25buhui
print(sentence[31:54])
#26
print(sentence.find('because'))
#27
#28
print(company.startswith('Coding'))
#29
print(company.endswith('coding'))
#30buhui
company_2 = '   Coding For All      '
print(company_2.strip())
#31buhui
print("30DaysOfPython".isidentifier())        # False
print("thirty_days_of_python".isidentifier()) # True
#32buhui
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' # '.join(libraries))
#33 buhui
sentence_2 = 'I am enjoying this challenge. I just wonder what is next.'
print("I am enjoying this challenge.\nI just wonder what is next.")
#34 buhui
print("Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")
#35 注意小数点
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area:.0f} meters square.")
#36 注意小数点
a = 8
b = 6
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print('{} / {} = {:.2f}'.format(a, b, a/b))
print('{} % {} = {}'.format(a, b, a % b))      
print('{} // {} = {}'.format(a, b, a//b))
print('{} ** {} = {}'.format(a, b, a**b))