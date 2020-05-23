import asyncio
import threading


@asyncio.coroutine
def hello():
    print('hello world')
    # 异步调用
    # yield from语法可以让我们方便地调用另一个generator
    r = yield from asyncio.sleep(1)
    print('hello again')


# 获取时间循环组（eventLoop）
event_loop = asyncio.get_event_loop()
# 执行协程
event_loop.run_until_complete(hello())
# event_loop.close()


print("====")


@asyncio.coroutine
def hello2():
    print('hello world! (%s)' % threading.current_thread())
    yield from asyncio.sleep(1)
    print('hello again (%s)' % threading.current_thread())


# 获取时间循环组（eventLoop）
event_loop2 = asyncio.get_event_loop()
tasks = [hello2(), hello2()]
# 执行协程
event_loop2.run_until_complete(asyncio.wait(tasks))
event_loop2.close()

"""
hello world! (<_MainThread(MainThread, started 140736285537152)>)
hello world! (<_MainThread(MainThread, started 140736285537152)>)
hello again (<_MainThread(MainThread, started 140736285537152)>)
hello again (<_MainThread(MainThread, started 140736285537152)>)

"""
