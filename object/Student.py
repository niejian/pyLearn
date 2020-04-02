class Student(object):
    def __init__(self, name, score, addr):
        self.name = name
        self.score = score
        # 私有成员变量 __
        self.__addr = addr

    def print_score(self):
        print(self.name, self.score, self.__addr)


stu = Student('nie', 10, "gz")
# 访问不到私有成员变量
stu.__addr = 'sd'
stu.name = "lisi"
stu.print_score()
