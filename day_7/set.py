# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#level one
#1
print(len(it_companies))
#2
it_companies.add('Twitter')
print(it_companies)
#3
it_companies_add = ['Nvidia', 'X', "Insgram"]
it_companies.update(it_companies_add)
print(it_companies)
#4
it_companies.remove('X')
print(it_companies)
it_companies.pop()
print(it_companies)
#5
#如果找不到该元素，`remove() ` 方法会抛出错误，因此最好先检查该元素是否存在于给定的集合中。而 ` discard()`方法则不会抛出任何错误。
it_companies.discard('Ali')
print(it_companies)

#level two
#1 不可以用+号，三种方法union, |, update
# A.union(B)
# print(A)  #  C = A.union(B)
C = A.union(B)
print(C)
# A|B #  C = A|B
# D = A|B
# print(D)
#使用 update()
# A.update(B)
# print(A)
#2 intersection交集运算返回两个集合中都存在的元素集合
print(A.intersection(B))
#3 子集：issubset() 超集：issuperset
print(A.issubset(B))
#4
print(A.isdisjoint(B))
#5 update()修改A,但不返回新的集合,故返回值是 None, 推荐使用union
# print(A.update(B))
# print(B.update(A))
A_copy = A.copy()
B_copy = B.copy()

A_copy.update(B)
B_copy.update(A)

print(A_copy)
print(B_copy)

#6
print(A.symmetric_difference(B))
print(A ^ B)#还可以这样
#7
del A
del B

#level three
#1
age_st = set(age)
print(len(age) > len(age_st))
#2
#字符串不能用来存储数据，通常以''or""的格式。列表的格式为[]，可以存储不同类型的数据，包括字符串，整数，浮点数。元组的格式为()，元组内的元素不可修改。集合的格式为{}，不包含重复元素，且具有随机性。
#字符串当然可以存储数据，它用于存储文本。集合不是随机性（random），而是无序性（unordered）。
#3 小问题：people. 包含句号，Python 会把它当作完整的字符串。
sentence = 'I am a teacher and I love to inspire and teach people.'
sentence_word = sentence.replace('.', '').split(' ')#split() 的作用是把一个字符串拆分成列表（list）
sentence_word_st = set(sentence_word)
print(sentence_word_st)
print(len(sentence_word_st))

