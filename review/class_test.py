# 面向对象
class MyClass:
    # 构造方法, 构造方法中的参数在对象声明的时候给出
    def __init__(self, list):
        print("构造方法__init__被调用")
        self.data = list
    def f(self):
        print(self.data)

# 声明对象的时候，__init__被调用
myclass = MyClass([1,2,3,4])
myclass.f()

# 字段的可见性
class people:
    # 定义基本属性
    name = ""
    age = 0
    # 私有熟悉 _
    _weight = 0
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self._weight = weight
    
    def speak(self):
        print("%s 说：%d 岁, 体重：%d" % (self.name, self.age, self._weight))

p = people("张三", 10, 100)
p.age = 100
p._weight = 10
p.speak()


