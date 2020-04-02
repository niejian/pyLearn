from enum import Enum, unique
import logging
logging.basicConfig(level=logging.INFO)
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
print(type(Month))
for name, member in Month.__members__.items():

    print(name, '=>', member, ',', member.value)


# 检查没有重复值
@unique
class WeekDay(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


# 获取code
print(WeekDay.Sun)
# 获取value
print(WeekDay.Sun.value)
print(WeekDay(1))


@unique
class Gender(Enum):
    Male = 1
    Female = 0


class Student(object):

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')


