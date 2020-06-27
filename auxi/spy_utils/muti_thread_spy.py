# coding:utf-8

# from datetime import datetime
import threading
from queue import Queue

# TODO: 2020-6-27 阉割了内存共享、CPU加速等功能。


class ThreadWorker(threading.Thread):
    def __init__(self, queue, func=print):
        threading.Thread.__init__(self)
        self._queue = queue
        self.func = func

    def run(self):
        while not self._queue.empty():
            item = self._queue.get()
            try:
                self.func(item)
            except Exception as e:
                print(e)


# TODO 多线程运行的函数： 其中item_List是队列的列表
def muti_thread_run_local(item_list, func, thread_count=12):
    queue = Queue()
    for x in item_list:
        queue.put(x)
    threads = [ThreadWorker(queue, func=func) for i in range(thread_count)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()


def test(x):
    print(2**x)


if __name__ == '__main__':
    muti_thread_run_local(item_list=[x for x in range(200)], func=test)

