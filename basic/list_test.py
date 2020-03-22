# list test list有序的元素列表可以随时添加和删除
# 声明一个list信息，并打印出来
classmate = ['a', 'b', 'c']
print(classmate)
# 获取list长度
print('classmate has %d elements' % len(classmate))
# 获取list中最后一个元素，取索引是-1的
# 倒数第二个[-2], 倒数第3个, [-3]
last_element = classmate[-1]
print('list classmate laste element is %s' % last_element)
# 向末尾添加一个元素, append
classmate.append("d")
print(classmate)
# 指定位置添加元素, insert
classmate.insert(1, "f")
print(classmate)
# 删除末尾元素, pop
classmate.pop()
print(classmate)
# 删除指定位置的元素
classmate.pop(1)
print(classmate)
# 直接给指定位置元素赋值
classmate[1] = "niejian"
print(classmate)
# list中可以包含list
classmate.append(['niejian', 'wuqian'])
print(classmate)
print(classmate[-1])
print('二维数组元素',classmate[3][1])

###########
# tuple 有序的元素列表，与list类似，但是一旦初始化后就不能被修改
## 声明
print("==================tuple操作=====================")
t = ('a', 'b', 'c')
print(t)
print('tuple：t的长度：%d' % len(t))
# 数组切片(提取指定位置的元素，)
list = list(range(100))
# 截取list中前十个元素
print(list[:10])
# 从指定位置开始截取(截取3个元素后再充下标是1的开始截取)
print(list[1:4])
# 取后10个数
print(list[-10:])
