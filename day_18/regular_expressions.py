# txt = 'a'
# print(re.findall(r'a.*', txt))返回['a']
# print(re.findall(r'a.+', txt))返回[]
#level one
"""
什么是正则表达式？
正则表达式（RegEx）是一种特殊的文本字符串，
有助于在数据中查找模式。RegEx可用于检查不同数据类型中是否存在某种模式。
正则表达式的变量是什么？
用于存储正则表达式匹配模式的变量
"""
regex_pattern = r'talent'#匹配完整单词 推荐：r'\btalent\b'  \b：单词边界
regex_pattern = r'\b\d{2}-\d{2}-\d{4}\b'
regex_pattern = r'ing'#只能匹配ing，应写r'\b[a-zA-Z]+ing\b' +:表示前面的字母出现一次或多次

#level two
#1 不会
# regex_pattern = r'\bPython\b'
import re
import keyword

name = 'student_name'

valid = (
    re.match(r'^[A-Za-z_][A-Za-z0-9_]*$', name)# $表示到字符串结尾
    and not keyword.iskeyword(name)
)

#2 理解错了，是删除<>
import re
text = '''
HTML
Hypertext Markup Language (HTML) is the standard markup language for documents designed to be displayed in a web browser. It can be assisted by technologies such as Cascading Style Sheets (CSS) and scripting languages such as JavaScript.

Web browsers receive HTML documents from a web server or from local storage and render the documents into multimedia web pages. HTML describes the structure of a web page semantically and originally included cues for the appearance of the document.

HTML elements are the building blocks of HTML pages. With HTML constructs, images and other objects such as interactive forms may be embedded into the rendered page. HTML provides a means to create structured documents by denoting structural semantics for text such as headings, paragraphs, lists, links, quotes and other items. HTML elements are delineated by tags, written using angle brackets. Tags such as <img /> and <input /> directly introduce content into the page. Other tags such as <p> surround and provide information about document text and may include other tags as sub-elements. Browsers do not display the HTML tags, but use them to interpret the content of the page.

HTML can embed programs written in a scripting language such as JavaScript, which affects the behavior and content of web pages. Inclusion of CSS defines the look and layout of content. The World Wide Web Consortium (W3C), former maintainer of the HTML and current maintainer of the CSS standards, has encouraged the use of CSS over explicit presentational HTML since 1997.
'''
regex_pattern=r'<[^>]+>'
# <       找到 <
# [^>]    匹配不是 > 的任意字符
# +       一个或多个
# >       找到 >
matches=re.sub(regex_pattern, '',text)
print(matches)

#level 3
#1
paragraph = '''I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'''
regex_pattern = r'\b[A-Za-z]+\b'
matches=re.findall(regex_pattern,paragraph)#应全部小写
def words_count(lst,number):
    word_count= {}
    for item in lst:#可以简化成这样;word_count[item] = word_count.get(item, 0) + 1
        if item in word_count:
            word_count[item] += 1
        else:
            word_count[item] = 1
    def get_count(items):
        return items[1]

    sorted_words_count = sorted(
        word_count.items(),#word_count.items(),这样才能取出键值对
        key=get_count,
        reverse=True
    )
    return sorted_words_count[:number]
print(words_count(matches,3))

#3
email_address = '''
asabeneh@gmail.com
alex@yahoo.com
kofi@yahoo.com
doe@arc.gov
asabeneh.com
asabeneh@gmail
alex@yahoo
'''
# regex_pattern=r'\b[a-z]+@[a-z]+.?[a-z]+\b'#正则里的.是匹配任意一个字符，应用\.
regex_pattern = r'\b[a-z]+@[a-z]+\.[a-z]{2,}\b'#{2,}:至少两个字母

#4
text = '''
The position of some particles on the horizontal x-axis are -12, -4, -3 and -1
in the negative direction, 0 at origin, 4 and 8 in the positive direction.
'''

# 提取整数，包括负数
points = re.findall(r'-?\d+', text)

print(points)