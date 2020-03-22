# 斐波那契数列
# 1, 1, 2, 3, 5, 8, 13, 21, 34
# 获得斐波那契数列的
def fib(max):
  num1, num2 = 1, 1
  n = 0
  result = [num1, num2]
  # max = max - 2
  while max > n:
    # print(num2)
    # 这就是定义generator的另一种方法。如果一个函数定义中包含yield关键字，
    # 那么这个函数就不再是一个普通函数，而是一个generator：
    yield num2
    tmp = num1 + num2
    result.insert(n + 2, tmp)
    num1 = num2
    num2 = tmp
    n = n + 1
  # return result


# print(fib(1))
# genetor当时调用
f = fib(7)
# f.next()  2.x的写法
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())

print("----")
def fab(max): 
    n, a, b = 0, 0, 1 
    while n < max: 
        yield b      # 使用 yield
        # print b 
        a, b = b, a + b 
        n = n + 1

f2 = fab(7)
print(f2.__next__())
print(f2.__next__())
print(f2.__next__())
print(f2.__next__())
print(f2.__next__())

# 带有 yield关键字的函数就是generator，
# 生成一个generator（f = fab() ）看起来像是函数调用，但不执行任何代码，
# 直接对其调用__next()___(就是在调用循环中的方法)。
# 虽然执行流程仍按函数的流程执行，但每执行到一个 yield 语句就会中断，并返回一个迭代值，下次执行时从 yield 的下一个语句继续执行。看起来就好像一个函数在正常执行的过程中被 yield 中断了数次，每次中断都会通过 yield 返回当前的迭代值。
# yield 的好处是显而易见的，把一个函数改写为一个 generator 就获得了迭代能力，比起用类的实例保存状态来计算下一个 next() 的值，不仅代码简洁，而且执行流程异常清晰。

print('-----判断函数是否是generator-----')
## 判断函数是否是generator, 
import types
print(isinstance(fab, types.GeneratorType))
print(isinstance(fab(5), types.GeneratorType))

