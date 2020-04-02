#
class Student(object):

    # @property负责把一个方法编程属性调用的，相当于get方法
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must inster')
        if value < 0 or value > 100:
            raise ValueError('score must 0 - 100')

        self._score = value


s = Student()
# 实际转化为s.set_score(60)
s.score = 11
# 实际转换成s.get_score
print(s.score)


class Screen(object):

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError('height must a number')
        if value <= 0:
            raise ValueError('height must 大于0')
        self._height = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise ValueError('height must a number')
        if value <= 0:
            raise ValueError('height must 大于0')
        self._width = value

    @property
    def resolution(self):
        return self._width * self._height


s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')



