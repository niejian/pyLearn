def add(x, y):
    return x + y


# lambda表达式，函数的简写，冒号前面微函数参数，后面为计算返回值
g = lambda x, y: x + y
print('调用add：%d' % add(1, 2))
print('调用lambda：%d' % g(1, 2))

# filter，通过第一个函数返回
list1 = list(filter(None, [1, 0, True, False]))
print(list1)

temp = range(10)
show = list(filter(lambda x: x % 2 == 0, temp))
print(show)
str = "ab:c:sd"
(split, s) = str.split(":", 1)
print(split)
print(s)
# 数组截取
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters[2:len(letters):2])
# 字典
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
# 输出格式化
print('tinydict keys: %s' % tinydict.keys())
print(tinydict.keys())
# 三引号
hi = ''' hello
world'''
print(hi)

