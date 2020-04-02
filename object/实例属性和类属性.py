# 实例和类
class Student(object):
    name = 'student'
    # 没创建一个实例，count就自动增加
    count = 0

    def __init__(self, name, score):
        self.name = name
        self.score = score
        Student.count = Student.count + 1


# stu 就是Student类的一个属性
stu = Student('a', 10)
# 打印实例属性
print(stu.name)
# 显示类属性
print(Student.name)
stu.name = 'bob'
print(stu.name)
print(Student.name)
# 删除实例属性
del stu.name
print(stu.name)
print(stu.count)
stu2 = Student('b', 10)
print(stu2.count)