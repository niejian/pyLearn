# 多线程
# 多线程的定义：thread.start_new_thread(function(), [args])
import time
import threading
import queue
def print_time(thradName, delay):
    count = 0
    while (count < 5) :
        count += 1
        print("%s, %s" % (thradName, time.ctime(time.time())))


def start_thread_1():
    try:
        t1 = threading.Thread(target=print_time, name="thread-1", args=("thread-1", 10, ))
        t2 = threading.Thread(target=print_time, name="thread-2", args=("thread-2", 20, ))
        t1.start()
        t2.start()
    except Exception:
        print("执行线程任务失败。")
start_thread_1()
# 线程同步（java中的锁）
thradLock = threading.Lock()

class lock_thrad(threading.Thread):
    def __init__(self, threadId, threadName, counter):
        threading.Thread.__init__(self)
        self.theadId = threadId
        self.threadName = threadName
        self.counter = counter
    def run(self):
        print("开启线程 %s" % self.threadName)
        # 获取锁
        thradLock.acquire()
        thread_print_time(self.threadName, 1, 3)
        thradLock.release()


def thread_print_time(threadName, delay, counter):
    while counter > 0 :
        # time.sleep(delay)
        print("%s, %s" % (threadName, time.ctime(time.time())))   
        counter -= 1
# 创建新线程
thread1 = lock_thrad(1, "thrad-1", 1)
thread2 = lock_thrad(2, "thrad-2", 2)
thread1.start()
thread2.start()
threads = []
threads.append(thread1)
threads.append(thread2)
# 阻塞主线程，使子线程全部执行完再执行主线程
for my_thread in threads:
    my_thread.join()
print("退出主线程")

# 线程优先级队列
print("=======")
print("线程优先级队列(Queue)")
print("=======")
exitFlag = 0
queueLock = threading.Lock()
workQueue = queue.Queue(10)

class thread_queue(threading.Thread):
    def __init__(self,theadId, name, q):
        threading.Thread.__init__(self)
        self.name = name
        self.threadId = theadId
        self.q = q
    def run(self):
        print("开启线程：" + self.name)
        process_data(self.name, self.q)
        print("退出线程：" + self.name)


def process_data(threadName, q):
    # print("exitFlag %d" % exitFlag)
    while not exitFlag:
        # print(workQueue)
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            print("data:" + data)
            queueLock.release()
            print("%s processing, data: %s" % (threadName, data))
        else:
            # print("queue is empty")
            queueLock.release()

threadList = ["thrad-1", "thrad-2", "thrad-3"]
nameList = ["1", "2", "3", "4", "5"]
threads = []
threadId = 1
for tName in threadList:
    thread = thread_queue(threadId, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadId += 1
# 填充队列
queueLock.acquire()
for w in nameList:
    workQueue.put(w)
queueLock.release()

# 等待队列清空
while not workQueue.empty():
    pass

exitFlag = 1
for t in threads:
    t.join()
print("退出主线程-queue")





