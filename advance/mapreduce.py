# map and reduce
## map()函数接收两个参数，一个是函数，一个是iterable，map将传入的函数依次作用到序列中的每个元素，并把结果作为新的iterable返回。举例说明，比如我们有一个函数f(x)=x2，要把这个函数作用在一个list [1, 2, 3, 4, 5, 6, 7, 8, 9]上，就可以用map()实现如下：
def f(x):
  return x * x;
r = map(f, [1,2,3,4,5,6,7,8,9,10])
# 通过list()函数将它整个序列计算返回出来，并返回一个list
print(list(r))
# print(list(map(f, range(10, 100))))

# reduce 函数也是接收两个参数
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
from functools import reduce
def fn(x, y):
  return x * 10 + y
i = reduce(fn, [1, 3, 5])
print(i)

def char2num(s):
  digits = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9 }
  return digits[s]

print(list(map(char2num, '12345')))



def prod(x, y):
  return x * y
result = reduce(prod, [3, 5, 7, 9])
print('result:', result)


def str2float(s):
  digits = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '.': '.' }
  return digits[s]
def fn2(x, y):
  index = y.index('.')
  # print("index: ", index)
  # 截取正数和负数
  sub1 = y[0:index]
  # 负数
  sub2 = y[index + 1: len(y)]
  sub2_len = len(sub2)

  data = int(sub1 + sub2)
  while sub2_len > 0:
    sub2_len = sub2_len - 1
    data = data / 10
  return data 
print(list(map(str2float, '124.23')))
result = reduce(fn2, map(str2float, '124.23'))


