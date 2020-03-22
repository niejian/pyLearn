# 字典类，相当于java中的map
d = {'a': 100, 'b':101, 'c': 102}
print(d)
print(d['a'])
# 通过get当时获取, 不存在时返回None
print(d.get('ad'))
# 删除一个一个key pop
print(d.pop('c'))
print(d)
#### set, 与java中的set类似，存储的也是列表，列表中的元素不重复
print('-------set 集合-------')
list = [1, 2,3,4,5,4,2]

test_set = set(list)
print(test_set)
# set 添加/删除元素
test_set.add(6)
print(test_set)
test_set.remove(5)
print(test_set)
# 两个set球交集、并集
s1 = set([1,2,3,4,4,3])
s2 = set([1,4,5])
print('s1, s2 交集', s1 & s2)
print('s1, s2 并集', s1 | s2)

n1 = 25
n2 = 1000
print(hex(2))