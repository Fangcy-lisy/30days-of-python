import requests
url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt'
response=requests.get(url)
print(response)
print(response.status_code)# 状态码，成功时为200
print(response.headers)
print(response.text)

url = "https://raw.githubusercontent.com/mledoze/countries/master/countries.json"
response = requests.get(url)
print(response) # 响应对象
print(response.status_code)  # 状态码，成功时为200
response.raise_for_status()#如果请求失败，就抛出异常 它会检查 HTTP 请求有没有失败。
countries = response.json()#状态码 200：请求成功 404：请求的资源不存在 403：服务器拒绝访问 500：服务器内部错误
# print(countries[:1])  # 我们只打印第一个国家信息，原始数据太大
for country in countries[:5]:
    name = country["name"]["common"]
    capital = country.get("capital", ["未知"])[0]
    print(f"国家：{name}，首都：{capital}")
#country 字典中获取首都。如果没有首都信息，就使用 "未知"，最后取出列表中的第一个元素
print("国家和地区总数：", len(countries))

from pprint import pp
url = 'http://api.worldbank.org/countries/et?format=json'  # 埃塞俄比亚经济数据API
response = requests.get(url)  # 打开网络并获取数据
print(response) # 响应对象
print(response.status_code)  # 状态码，成功时为200
response.raise_for_status()#如果请求失败，就抛出异常 它会检查 HTTP 请求有没有失败。
# 让我们改变响应的JSON格式
ethiopia_data = response.json()#解析json内容，转换成对应的python对象
pp(ethiopia_data) # 用pretty print打印数据
# countries[0]：取出一个元素。
# countries[:1]：切出一个新列表。