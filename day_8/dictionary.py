#1
dog = {}
#2
dog['name'] = 'Tom'
dog['color'] = 'white'
dog['breed'] = 'alaskan'
dog['legs'] = '4'
dog['age'] = 'seven'
#3 错误：字典里的每一项之间必须有 ,
student = {
    'last_name':'lsy',
    'first_name':'李',
    'gender':'male',
    'age':'23',
    'marital status':False,
    'skills':['manage', 'econamic'],
    'country':'China',
    'city':'ShangHai',
    'address':'闵行区'
    }
#4
print(len(student))
#5 buhui 错误 student('skill')表示：调用 student 这个函数。字典取值要用：[]
# print(type(student('skills')))
print(type(student['skills']))
#6 错误 []的用法，append() 一次只能添加 一个元素。如果想一次加两个，可以使用：.extend
# student('skills').append('art', 'sing')
student['skills'].append('art')
student['skills'].append('sing')
#7 buhui 没有转换成列表
keys = list(student.keys())
print(keys)
#8 没有转换成列表
print(list(student.values()))
#9
print(list(student.items()))
#10
student.pop('age')
#11 清空和删除不一样
del student