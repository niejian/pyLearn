import os
# 迭代
# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：
l = []
print(len(l))
def findMinAndMax(L):
  if None == L or len(L) == 0:
    return(None, None)
  min = max = L[0]
  for num in L:
    if num <= min:
      min = num
    if num >= max:
      max = num
  return (min, max)


print(findMinAndMax([]))
print(findMinAndMax([7]))
print(findMinAndMax([7, 1]))
print(findMinAndMax([7, 1, 3, 9, 5]))


# if findMinAndMax([]) != (None, None):
#     print('测试失败!')
# elif findMinAndMax([7]) != (7, 7):
#     print('测试失败!')
# elif findMinAndMax([7, 1]) != (1, 7):
#     print('测试失败!')
# elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
#     print('测试失败!')
# else:
#     print('测试成功!')

for dir in os.listdir("/Users/a"):
  print(dir)