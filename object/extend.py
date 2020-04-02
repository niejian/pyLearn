# 类的继承
class Animal(object):
    def run(self):
        print("Animal is running")


# 继承
class Cat(Animal):
    def run(self):
        print("cat is running")

    def eat(self):
        print("cat eat")


class Dog(Animal):
    def run(self):
        print("dog is running")

    def eat(self):
        print("dog eat")


# 子类覆盖父类的方法
dog = Dog()
dog.run()

# 类型判断
a = list()
b = Animal()
c = Dog()

print(isinstance(a, list))
print(isinstance(b, Animal))
print(isinstance(b, Dog))
print(isinstance(c, Animal))

# 获取一个对象的所有方法
print(dir(Animal))
print(dir(Dog))

