# 条件判断
# for ...in 循环，从list或者tuple中拿出元素进行
nums = [1, 4, 6, 6]
total = 0
for num in nums:
  total += num

print('nums total: %d' % total)
# list(range(5))函数，等价于[0, 1, 2, 3, 4]
print(list(range(5)))
# 计算1-100的总和
sum = 0
for num in list(range(101)):
  sum += num
print('1-100, sum:', sum)
# while 循环
sum = 0
count = 0
while sum < 10:
  sum += 1
print(sum)
