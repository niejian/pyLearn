# 字符串编码问题
# ASCII unicode utf-8
# ord()  获取字符的整数标识， chr() 整数转字符串
print("0000")
zhong_encode = ord('中')
print('中对应的数字编码:', zhong_encode)
# // 数字编码转换为具体的字符
num_str = chr(20013)
print(num_str)
# 字符长度
length = len("avsf")
print("length", length)
# 格式化, 将字符串拼接
print('%s is %d year old' % ("niejian" , 10))
s1 = 72
s2 = 85
print('xiaoming has improve %f' % (s2 - s1))