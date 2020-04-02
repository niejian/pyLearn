from types import MethodType


# 一个空对象，创建实例后可以动态的给该对象绑定任何属性和方法，
class Student(object):
    pass


s = Student()
# 动态绑定属性
s.name = 'lilei'
print(s.name)

# 动态绑定方法


def set_age(self, age):

    self.age = age

# 动态给实例s绑定方法


s.set_age = MethodType(set_age, s)
s.set_age(35)
print(s.name, s.age)

# 给s动态添加的实例和方法只对实例s有效
s2 = Student()
# print(s2.name, s2.age)

# 给所有实例绑定方法和熟悉


def set_score(self, score):
    self.score = score


# 给所有实例添加方法
Student.set_score = set_score
s.set_score(100)
s2.set_score(1)
print(s.score, s2.score)

# 如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。
# 为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：


class Student2(object):
    __slots__ = ('name', 'score')

# 只允许动态添加 name、score这两个属性




