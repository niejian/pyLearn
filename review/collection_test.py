# python 集合相关知识
# 列表的声明
list = ['a', 'b', 'c', 1, 2, 3]
print(list)
print("====访问列表元素===")
print("list中的首个元素 %s" % list[0])
print("list中的末尾元素 %s" % list[-1])
print("截取某一段的元素信息： %s" % list[1:3] )
# 添加元素
list.append("google")
print("添加元素：", list)
# 删除元素
del list[1]
print("删除元素：", list)
# 比较两个列表中的元素
list2 = [1, 2, 4, 'a']
# 元组
# 元组与列表类似，元组中的元素不能修改
tup1 = (1,2, 3, 4, 'a', 'b', 'c')
print('元组：', tup1)
# 尝试修改元组
#tup1[1] = 'google' #TypeError: 'tuple' object does not support item assignment
#print('修改后的元组信息：', tup1)
# 同样也不能删除元组的某个元素
# del tup1[1]
# 只能情况元组中的所有信息
# del tup1

