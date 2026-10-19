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
def read_file(filename):
    with open(filename,'r',encoding='utf-8')as f:
        text=f.read()
        return text
def clean_text(text):
    import re
    text=text.lower()
    # clean_text_lst=[]
    all_word = re.findall(r'\b[a-z]+\b',text,re.I)
    # for word in all_word: 
    #     if word not in clean_text_lst:#这里可以用set去重
    #         clean_text_lst.append(word)
    return all_word
def remove_support_words(text):
    # for word in text:#一边遍历列表，一边删除列表中的元素，可能会漏掉某些元素。
    #     if word in stop_words:#建议增加空列表
    #         text.remove(word)
    # return text
    result = []
    for word in text:
        if word not in stop_words:
            result.append(word)
    return result
'Or列表推导式'
'return [word for word in text if word not in stop_words]'
def check_text_similarity(text1,text2):
    set1 = set(text1)
    set2 = set(text2)
    all_have_word = set1 | set2#&|是集合的运算符
    common_word=set1&set2
    if len(all_have_word) == 0:
        return 0
    similarity = len(common_word) / len(all_have_word)
    return similarity
michelle_text = read_file(
    './data/michelle_obama_speech.txt'
)
melina_text = read_file(
    './data/melina_trump_speech.txt'
)
michelle_text_clean=clean_text(michelle_text)
melina_text_clean=clean_text(melina_text)
michelle_text_clean_remove_stopword=remove_support_words(michelle_text_clean)
melina_text_clean_remove_sotpword=remove_support_words(melina_text_clean)
similarity=check_text_similarity(michelle_text_clean_remove_stopword,melina_text_clean_remove_sotpword)
print(f"{similarity:.2}")
#6
import csv
python_count = 0
javascript_count = 0
java_count = 0
with open('./data/hacker_news.csv','r',encoding='tuf-8')as file:
    csv_reader=csv.reader(f)
    next(csv_reader, None)# 跳过表头（如果第一行是列名）
    for row in csv_reader:
        line = ' '.join(row).lower()
        if 'python' in line:
            python_count += 1
        if 'javascript' in line:
            javascript_count += 1
        if 'java' in line and 'javascript' not in line:
            java_count += 1
print('包含 Python 的行数:', python_count)
print('包含 JavaScript 的行数:', javascript_count)
print('包含 Java 但不包含 JavaScript 的行数:', java_count)