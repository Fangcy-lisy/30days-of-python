import requests as re
import json

url = "https://api.restcountries.com/countries/v5"
#API 的访问地址，告诉程序去哪里请求数据
headers = {
    "Authorization": f"Bearer rc_live_demo"
}
response = re.get(url, headers=headers,timeout=10)#timeout:设置 10 秒的超时限制向 API 发送 GET 请求
print(response.status_code)#200
# response.raise_for_status()
data = response.json()#JSON 转换后的结果不一定是字典
# print(json.dumps(data, indent=2, ensure_ascii=False))
print(data.keys())
print(data["data"].keys())
# countries = data["data"]["objects"]
# print("第一条记录的字段：", countries[0].keys())
# print(countries[0])

# 第一步：获取所有国家的数据
countries = []
limit = 100 #这次最多返回 100 条，不指定要多少条数据，就使用默认值
offset = 0 #从第 0 个位置开始获取数据

while True:#表示持续循环，直到程序遇到 break 才停止
    params = {#告诉 API
        "limit": limit,
        "offset": offset
    }

    response = re.get(#re.get(...)：向 API 发送请求
        url,
        headers=headers,
        params=params,
        timeout=10
    )

    response.raise_for_status()#re.get(...)：向 API 发送请求
    data = response.json()#把服务器返回的 JSON 转换成 Python 数据结构

    # 取出当前页的国家列表
    page_countries = data["data"]["objects"]
    countries.extend(page_countries)#把另一个列表中的元素逐个添加进来
#为什么要分页：URL 是地址，不是数据列表本身。访问这个地址后，服务器才会返回数据
    # 查看是否还有下一页
    meta = data["data"]["meta"]
    if not meta.get("more", False):# more 是这个 API 专门用来表示是否还有后续数据的字段
        break
    offset += limit

print("获取到的国家/地区数量：", len(countries))

# 第二步：按照人口从大到小排序，取前十名
top10 = sorted(
    countries,
    key=lambda country: country.get("population") or 0,
    reverse=True
)[:10]

# 第三步：打印结果
print("\n人口最多的前十个国家：")
#enumerate()用来遍历列表时，同时获得序号和元素
for rank, country in enumerate(top10, start=1):
    name = country.get("names", {}).get("common", "未知")
    # 从 country 字典中获取 names 对应的值。如果没有 names 这个键，就返回一个空字典 {}
    # common 存在，就获取国家的常用名称；如果不存在，就返回 "未知"
    population = country.get("population") or 0

    print(f"{rank}. {name}：{population:,} 人")#:, 是数字格式化语法，1410000000  1,410,000,000

country_eng=[]
for country in countries:
    # if countries['names']['common']['language'] == 'English': #错误写法
# countries 是列表，不能直接使用字符串 'names' 作为索引
    languages = country.get("languages",[])
    for language in languages:
        if language.get("name")=='English':
            country_eng.append(country)
            break
for country in country_eng:
    name = country.get("names", {}).get("common", "未知")
    print(name)
print("包含英语的国家/地区数量：", len(country_eng))
# print(countries[0].get("languages"))

# english_countries = []
# for country in countries:
#     languages=country.get("languages",[])
#     for language in languages:
#         if language.get("name")=="English" or language.get("bcp47") == "en":
#             english_countries.append(country)
#             break
# for country in english_countries:
#     name=country.get("names",{}).get("common","未知")#使用.get() 可以提供默认值，让代码更安全
# print("包含英语的国家/地区数量：", len(english_countries))

top10_area = sorted(
    countries,
    key=lambda country: (country.get("area") or {}).get("kilometers") or 0,
    reverse=True
)[:10]

# 第二步：打印结果
print("面积最大的前十个国家/地区：")

for rank, country in enumerate(top10_area, start=1):
    name = country.get("names", {}).get("common", "未知")
    area = (country.get("area") or {}).get("kilometers") or 0

    print(f"{rank}. {name}：{area:,.0f} 平方公里")


# 第一步：定义一个函数，获取国家的首都名称
def get_capital(country):
    capitals = country.get("capitals") or []

    if capitals:
        return (0, capitals[0].get("name", "").casefold())
    else:
        return (1, "")


# 第二步：按照首都名称排序
sorted_countries = sorted(
    countries,
    key=get_capital
)

# 第三步：打印国家名称和首都
for country in sorted_countries:
    name = country.get("names", {}).get("common", "未知")
    capitals = country.get("capitals") or []

    if capitals:
        capital_name = capitals[0].get("name", "未知")
    else:
        capital_name = "无首都记录"

    print(f"首都：{capital_name}，国家：{name}")





