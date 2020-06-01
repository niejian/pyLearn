# 导入模块(文件路径.py名)
import model_test.fibo
# 调用模块
model_test.fibo.fib(10)
model_test.fibo.fib2(10)

# 在 /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages 
# 添加calc即本项目的路径信息(全路径)
from calc import math
print("===")
print(math.add(1, 2))
