#level one
#1 熟悉
def count_lines_and_words(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()#得到列表

    line_count = len(lines)

    word_count = 0

    for line in lines:
        words = line.split()
        word_count += len(words)

    return line_count, word_count
def count_lines_and_words(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()

    line_count = len(text.splitlines())
    word_count = len(text.split())

    return line_count, word_count#实际上返回的是一个 tuple 需要解包
# Obama
lines, words = count_lines_and_words(
    './data/obama_speech.txt'
)
print('Obama:', lines, '行', words, '个单词')
# Michelle Obama
lines, words = count_lines_and_words(
    './data/michelle_obama_speech.txt'
)
print('Michelle Obama:', lines, '行', words, '个单词')
# Donald
lines, words = count_lines_and_words(
    './data/donald_speech.txt'
)
print('Donald:', lines, '行', words, '个单词')
# Melina Trump
lines, words = count_lines_and_words(
    './data/melina_trump_speech.txt'
)
print('Melina Trump:', lines, '行', words, '个单词')

#2 
import json
def language_top(filename,num):
    with open(filename,'r',encoding='utf-8')as f:#mis：'filename'会变成字符串
        file_dct = json.load(f)    #应该写encoding='utf-8'
    language_count={}
    for nation in file_dct:
        for language in nation['languages']:
            if language in language_count:
                language_count[language] += 1
            else:#language_count是整个字典，不能让字典加1
                language_count[language] = 1
        #简化写法：
        # language_count[language] = language_count.get(language, 0) + 1
    def get_count(items):
        return items[1]
    sorted_language = sorted(
        language_count.items(),
        key=get_count,
        reverse=True
    )
    # return sorted_language[:num]#返回顺序需要改变
    result = []
    for language,count in sorted_language[:num]:
        result.append((count,language))
    return result
print(language_top('./data/countries_data.json',10))         
#调用：filename = './data/countries_data.json'，num = 10

#3 不会
def most_populated_countries(filename,num):
    with open(filename,'r',encoding='utf-8')as f:
            countries = json.load(f)
    def get_population(countries):#
        return countries['population']
    sorted_population = sorted(
        countries,
        key=get_population,
        reverse=True
    )
    result = []#
    for country in sorted_population[:num]:
        result.append({'country':country['name'],
                       'population':country['population']
                       })
    return result
print(
    most_populated_countries(
        './data/countries_data.json',
        10
    )
)

#level two
#1
import re
# regex_pattern=r'[a-z0-9]+@[a-z]+\.[a-z0-9]+'
regex_pattern=r'[a-z0-9]+@[a-z0-9]+\.[a-z]+'
with open('./data/email_exchanges_big.txt','r',encoding='utf-8')as f:
    text = f.read()
matches=re.findall(regex_pattern,text,re.I)
print(matches)

#2
def find_most_common_words(filename,num):
    with open(filename,'r',encoding='utf-8')as f:
        text=f.read()
    regex_pattern=r'\b[a-z]+\b'
    word_in_text=re.findall(regex_pattern,text,re.I)
    word_count={}
    for words in word_in_text:
        if words in word_count:
            word_count[words]+=1
        else:
            word_count[words]=1
        #word_count[word] = word_count.get(word, 0) + 1
    def get_word(word):
        return word[1]
    sort_word=sorted(
        word_count.item(),#错误 word_count遍历得到键
        key=get_word,
        reverse=True
    )
    result=[]
    for word,number in sort_word[:num]:
        result.append((number,word))#append一次接收一个参数，故加括号
    return result

#4
stop_words = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up',
              'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
