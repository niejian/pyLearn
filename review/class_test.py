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

# 类的继承
class student(people):
    grade = ""
    def __init__(self, n, a, w, g):
        people.__init__(self, n, a, w)
        self.grade = g
    
    # 重写父类方法
    def speak2(self):
        print("%s 说：%d 岁, 体重：%d, %s 年级" 
        % (self.name, self.age, self._weight, self.grade))
s = student('ken',10,60,3)
# 子类调用父类方法
s.speak()

# 多继承
class speaker:
    topic = ""
    name = ""
    def __init__(self, name, topic):
        self.name = name
        self.topic = topic
    
    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s"%(self.name,self.topic))
    
# 多继承
class sample(speaker, student):
    a = ""
    def __init__(self, n, a, w, g, t):
        student.__init__(self, n, a, w, g)
        speaker.__init__(self, n, t)

test = sample("Tim",25,80,4,"Python")
test.speak()
# 类属性和私有方法 __开头标识私有属性和方法
import sys
print(sys.path)




