import threading
import asyncio

#加在函数前面=标注该函数是一个协程coroutine
#@asyncio.coroutine
async def hello():
    print('Hello world! (%s)' % threading.currentThread())
    #yield from也是一个coroutine，所以主线程不会等待sleep，而是去执行eventloop里面的其他可执行的语句，相当于是多线程进行了。

    r=await asyncio.sleep(3)
    print('Hello again! (%s)' % threading.currentThread())

#@asyncio.coroutine
async def python():
    print('Learn Python (%s)'% threading.currentThread())

    r=await asyncio.sleep(5)
    print('Day Python (%s)'% threading.currentThread())

loop = asyncio.get_event_loop()
tasks = [asyncio.ensure_future(hello()), asyncio.ensure_future(python())]
#loop.run_until_complete(hello())
loop.run_until_complete(asyncio.wait(tasks))
loop.close()


#整个过程是一个线程执行，线程号是一样的，但是实现的异步IO