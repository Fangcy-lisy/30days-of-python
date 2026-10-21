# class Person: #理解
#     def __init__(self, name):
#         print("1. 收到参数:", name)
#         print("2. self 指向的对象:", self)

#         self.name = name

#         print("3. 对象的属性:", self.__dict__)
#                             #看到对象当前保存的属性
# p = Person('Asabeneh')
# print("4. 通过 p 读取:", p.name)

#1 多练习，很多不熟
# class Statistics:#(类构造函数)
#     def __init__(self,data=[]):
#         self.data=data
#     def count(self):
#         return len(self)
#     def sum(self):
#         return sum(self)
#     def min(self):
#         return min(self)
#     def max(self):
#         return max(self)

class Statistics:
    def __init__(self, data=None):
        self.data = [] if data is None else data
#如果没有传入数据，就创建一个新的空列表；
#如果传入了数据，就使用传入的数据
    def _check_data(self):#提前检查数据，并提供更清晰的错误提示
        if not self.data:
            raise ValueError("数据不能为空")
    def count(self):
        return len(self.data)
    def sum(self):
        total = 0
        for i in self.data:
            total+=i
        return total
    def min(self):
        self._check_data()
        return min(self.data)
    def max(self):
        self._check_data()
        return max(self.data)
    def range(self):
        return self.max()-self.min()
    def mean(self):
        return sum(self.data)/len(self.data)
        #self.sum() / self.count()
    def median(self):#先排序，再找中间位置
        self._check_data()
        numbers = sorted(self.data)
        n = len(numbers)
        middle = n // 2

        if n % 2 == 1:
            return numbers[middle]
        else:
            return (numbers[middle - 1] + numbers[middle]) / 2
        # if len(self.data)%2!=0:
        #     return self.data[len(self.data)/2]
        # else:
        #     return self.data[(len(self.data)/2)-1,(len(self.data)/2)+1]
    def mode(self):
        self._check_data()
        counts = {}

        for number in self.data:
            counts[number] = counts.get(number, 0) + 1

        max_count = max(counts.values())
        modes = [
            number for number, count in counts.items()
            if count == max_count
        ]

        # 只有一个众数时返回数字；多个众数时返回列表
        mode_value = modes[0] if len(modes) == 1 else modes
         #条件表达式，也叫三元表达式
        return {"mode": mode_value, "count": max_count}
    def variance(self):#方差
        self._check_data()
        # 使用精确平均值，避免四舍五入影响方差
        average = self.sum() / self.count()
        total = 0
        for number in self.data:
            total += (number - average) ** 2
        # 总体方差
        return total / self.count()
    def standard_deviation(self):#标准差
        return self.variance() ** 0.5
    def frequency_distribution(self):#频率分布
        if not self.data:
            return []
        counts = {}
        for number in self.data:
            counts[number] = counts.get(number, 0) + 1
        total = self.count()
        distribution = []
        for number, count in counts.items():
            percentage = count / total * 100
            distribution.append((percentage, number))
        return sorted(
            distribution,
            key=lambda item: (item[0], item[1]),
            reverse=True
        )
    def describe(self):
        self._check_data()

        return (
            f"Count: {self.count()}\n"
            f"Sum: {self.sum()}\n"
            f"Min: {self.min()}\n"
            f"Max: {self.max()}\n"
            f"Range: {self.range()}\n"
            f"Mean: {self.mean()}\n"
            f"Median: {self.median()}\n"
            f"Mode: {self.mode()}\n"
            f"Variance: {self.variance():.1f}\n"
            f"Standard Deviation: {self.standard_deviation():.1f}\n"
            f"Frequency Distribution: {self.frequency_distribution()}"
        )
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)   
print(data.describe())     

#2
class PersonAccount:                       #可变默认参数和对象引用
    def __init__(self,firstname,lastname,incomes=None,expenses=None):
        self.firstname=firstname                 #注意None的用法
        self.lastname=lastname    #创建了一个列表
        self.incomes=list(incomes) if incomes is not None else []
        self.expenses=list(expenses) if expenses is not None else []
    def add_income(self,amount):
        self.incomes.append(amount)
    def add_expense(self, amount):
        self.expenses.append(amount)
    def total_income(self):
        return sum(self.incomes)
    def total_expense(self):
        return sum(self.expenses)
    def account_balance(self):
        return self.total_income() - self.total_expense()
# incomes=None: 避免把同一个可变列表作为默认参数共享给多个对象
# list(incomes)	:复制传入的列表，避免外部列表与对象属性共享同一个列表
person = PersonAccount("Tom", "Lee")

person.add_income(3000)
person.add_income(1000)

person.add_expense(500)
person.add_expense(200)

print("总收入：", person.total_income())
print("总支出：", person.total_expense())
print("账户余额：", person.account_balance())

#level3 #1
class PrintProducts:
    def __init__(self,*args, **kwargs):#*args:接收任意数量的位置参数,收集成一个元组
        self.args=args                 #**kwargs:接收任意数量的关键字参数,收集成一个元组
        self.kwargs=kwargs
    def print_products(self):
        for product in self.args:
            print(product)
        print(self.kwargs)
        for key in self.kwargs:
            print(f"{key}: {self.kwargs[key]}")

p = PrintProducts("apple", "banana", "orange", vegetable="tomato", juice="orange")
p.print_products()