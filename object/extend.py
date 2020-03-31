class Animal(object):
  def run(self):
    print("Animal is running")

# 继承
class Cat(Animal):
  def run(self):
    print("cat is running")

class Dog(Animal):
  def run(self):
    print("dog is running")

dog = Dog()
dog.run()