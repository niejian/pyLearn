# 我们来实现一个可变参数的求和。通常情况下，求和的函数是这样定义的：
def sum(*args):
  i = 0
  for n in args:
    i = i + n
  return i

# 但是，如果不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？可以不返回求和的结果，而是返回求和的函数：
def lazy_sum(*args):
  def sum():
    i = 0
    for n in args:
      i = i + n
    return i
  return sum
# 获取返回函数
f = lazy_sum(1,3,5,7,9)
# 返回函数结果
result = f()
print(result)