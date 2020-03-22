# 自定义函数
def myabs(x):
  # 参数检查
  if not isinstance(x, (int, float)):
    raise TypeError('parameter,', x ,' is not a number')
  if x < 0 :
    return -x
  return x


print(myabs(1))
# 函数默认值, 计算某个数的n次方，默认是2次方
# 使用默认值的函数再被调用时可以不用赋值
def suqar(num, n = 2):
  result = 1
  while n > 0:
    result = result * num
    n = n - 1
  
  return result

num = input('请输入数字：')
num = float(num)
print("num 的平方：", suqar(num))
print("num 的平方：", suqar(num, 3))


# 可变参数的函数定义, 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple
# 计算数组中所有数字的平方和
def calc(*nums):
  sum = 0
  for num in nums:
    sum += num * num
  
  return sum
# sum = calc(1, 2, 3, 4, 5)
data = [1, 2, 3, 4, 5]
sum = calc(*data)

print("可变参数函数计算结果：", sum)
# 关键字参数, 与可变参数类似，传入的是个dict对象
# 关键参数的作用是扩展函数接收数据的广度，在调用该函数的时候，可以在关键参数中传入自定义的一些数据
def person(name, age, **kw):
  if not kw.get('height') == None:
    print("------in kw ---")
    if 'height' in kw and kw['height'] >= 175:
      print('身高：', kw['height'], " cm, 高个子")
    elif 'height' in kw and kw['height'] >= 170:
      print('身高：', kw['height'], " cm, 高个子")
    else:
      print('身高：', kw['height'], " cm, 个头偏低")

  print('name:', name, " age:", age, 'other:', kw)

person('niejian', 29)

other = {'height': 180, 'weight': 80}
# 传入关键参数
person('niejian', 29, **other)
# 命名关键字参数
# 只接受指定的参数, *后面的参数被视为命名关键字参数。使用key=value的方式传入
def person2(name, age, *, city, job):
  print(name, age, city, job)

person2('niejian', 10, city='gz', job='tester')

def product(*nums, n=1):
  result = float(1.0)
  for num in nums:
    result = result * num
  return result

print(product(5))
print(product(5, 6))
print(product(5, 6, 7))
print(product(5, 6, 7, 9))

