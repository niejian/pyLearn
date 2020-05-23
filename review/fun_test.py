# python 函数
# 函数定义
def printme( str ):
    str += "call function:printme"
    print (str)
    return

# 调用函数
printme("调用用户自定义函数")
printme("再次调用")

# 函数传递不可变对象
def changeInt(a):
    a = 10
b = 2
changeInt(b)
print(b)

print('函数-传可变对象参数')
# 可变对象参数
def changeme(mylist):
    mylist.append([1,2,3,4])
    print('mylist：' , mylist)
    return

mylist = [10,20,30]
changeme(mylist)
print('调用后' , mylist) #[10, 20, 30, [1, 2, 3, 4]]
print("====关键字参数====")
# 关键字参数来确定传入的参数值
def test_key_param(str1, str2):
    print("关键字参数：%s" % str1, "str2:", str2)
    return
# 使用关键字参数，就可以不按照函数的声明顺序来调用了
test_key_param(str2="关键字参数2", str1="关键字参数1")
print("====默认参数====")
# 函数定义的时候给出默认值，在调用的时候如果没有传值，那么将会使用定义的那个默认值
def test_default_param(name, age=20):
    print("age: %d" % age, " name: %s" % name)
    return
test_default_param("zhangsan", 10)
test_default_param("lisi") # 参数age，使用函数定义的默认值
print("====函数-可变参数====")
def test_changeable_param(arg1, *vars):
    print("args： %s" % arg1)
    print("可变参数详细信息：")
    for var in vars:
        print(var)

    return

test_changeable_param(10, 'a', 'b', 'c')
# 匿名函数，lambda表达式
my_sum = lambda a, b: a + b
print('lambda表达式(两数相加结果)： %s' % my_sum(1, 2))
