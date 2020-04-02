import time, threading


def loop():
    print('thread %s is running' % threading.current_thread().name)
    n = 0
    while n < 5:
        print('thread %s is running >>> %s' % (threading.current_thread().name, n))
        n = n + 1
        # time.sleep(1)
    print("thread %s is end" % threading.current_thread().name)


# 设置执行方法，线程名称
t1 = threading.Thread(target=loop, name='loop-thread-1')
t2 = threading.Thread(target=loop, name='loop-thread-2')

t1.start()
t2.start()
# t1.join()
# t2.join()
print('thread %s is end' % threading.current_thread().name)

# 线程安全的lock
balance = 0


def change_it(n):
    global balance
    # print('thread %s do change', threading.current_thread().name)
    balance = balance + n
    balance = balance - n


def run_thread(n):

    lock = threading.Lock
    for i in range(100000):
        lock.acquire()
        try:
            print("thread %s do run_thread" % threading.current_thread().name)
            # print("1")
            change_it(n)
        finally:
            lock.release()


t3 = threading.Thread(target=run_thread, name='balance-thread-1', args=(10,))
t4 = threading.Thread(target=run_thread, name='balance-thread-2', args=(1,))
# t3.run()
# t4.run()
time.sleep(1)
# t3.join()
# t4.join()
print('balance...', balance)





