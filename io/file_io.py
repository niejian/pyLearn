a = '1.w.4.5.699'
index = a.rfind('-')
print(index)
print(a[index + 1: len(a)])
file_name = '/Users/a/Downloads/87346.txt'
try:
    f = open(file_name, 'r')
    data = f.read()
    name = f.name

    # 读取文件内容
    # print(data)
finally:
    if f:
        f.close()

print("===========")
# 使用with open读取
# 调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，
# 所以，要保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容
with open(file_name, 'r') as f:
    lines = f.readlines()
    for line in lines:
        lines
    # 读取的内容
    # ff = f.read(1024)
    # print(ff)

    # while(ff.__sizeof__() > 0):
    #     print(ff)
    #
    #     ff = f.read(1024)

    # print(dir(f))
    # print(f.__sizeof__())
    # print(f.__hash__())
    # # print(f.seek())
    # print("===")
    # ff = f.read(1024)
    # print(ff.__sizeof__())
    # print(dir(ff.__sizeof__()))
