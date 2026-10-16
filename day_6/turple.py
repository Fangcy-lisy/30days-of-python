#1(level one)
tuple_1 = tuple()
tuple_1 = ()
#2
brothers = ("Tom", "Jack")
sisters = ("Anna", "Lucy")
#3 第二步要创建两个元组
siblings = brothers + sisters
print(siblings)
#4
print(len(siblings))
#5
# siblings_set = set(siblings)
# siblings_set.append(方春雨， 李书瑶)#set 没有 append() 方法，集合可以用add, append() 是列表（list）的方法。名字需要加引号
# family_members = tuple(siblings_set)
#不需要转换成集合，题目要求的是元组，可以直接使用 + 拼接。
parents = ("fcy", 'lsy')
family_members = siblings + parents
print(family_members)

#level two
#1 不理解解包的意思 解包就是将一个集合式的数据结构中的元素拆出来，分别赋值给变量。
*siblings, father, mother = family_members
print(siblings)
print(father)
print(mother)
#2
fruits = ('apple', 'banana')
vegetables = ('onion', 'tomato')
animals = ('dog', 'cat')
food_stuff_tp = fruits +vegetables + animals
print(food_stuff_tp)
#3
food_stuff_lt = list(food_stuff_tp)
#4 Slice out the middle item
# food_stuff_lt.remove[2:3]#remove是删除指定值，不是提取元素
# print(food_stuff_lt)
middle = food_stuff_lt[2:4]
print(middle)
#5 cuowu
# food_stuff_lt.remove[0:4]
# print(food_stuff_lt)
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
print(first_three)
print(last_three)
#6
del food_stuff_tp
#7
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia" in nordic_countries)
print('Iceland' in nordic_countries)



