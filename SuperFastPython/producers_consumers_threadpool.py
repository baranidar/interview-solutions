#https://superfastpython.com/thread-producer-consumer-pattern-in-python/
# SuperFastPython.com
# example of producer and consumer thread pools
from random import random
from time import sleep
from threading import Thread
from multiprocessing.pool import ThreadPool
from queue import Queue
 
# producer task
def producer_task(queue):
    # generate a random number between 0 and 10
    value = random() * 10
    # block for a moment to simulate work
    sleep(value)
    # push data into queue
    queue.put(value)
 
# producer manager task
def producer_manager(queue):
    # create thread pool
    with ThreadPool(20) as pool:
        # use threads to generate items and put into the queue
        _ = [pool.apply_async(producer_task, args=(queue,)) for _ in range(20)]
        # wait for all tasks to complete
        pool.close()
        pool.join()
    # put a signal to expect no further tasks
    queue.put(None)
    # report a message
    print('>producer_manager done.')
 
# consumer task
def consumer_task(queue):
    # run until there is no more work
    while True:
        # retrieve one item from the queue
        value = queue.get()
        # check for signal of no more work
        if not value:
            # put back on the queue for other consumers
            queue.put(value)
            # shutdown
            return
        # block for a moment to simulate work
        sleep(value)
        # report the value
        print(f'Consumer got: {value}')
 
# consumer manager
def consumer_manager(queue):
    # create thread pool
    with ThreadPool(5) as pool:
        # start consumer tasks
        _ = [pool.apply_async(consumer_task, args=(queue,)) for _ in range(5)]
        # wait for all tasks to complete
        pool.close()
        pool.join()
    print('>consumer_manager done.')
 
# protect the entry point
if __name__ == '__main__':
    # create the shared queue
    queue = Queue()
    # run the consumer
    consumer = Thread(target=consumer_manager, args=(queue,))
    consumer.start()
    # run the producer
    producer = Thread(target=producer_manager, args=(queue,))
    producer.start()
    # wait for the producer to finish
    producer.join()
    # wait for the consumer to finish
    consumer.join()
    # report a final message
    print('>main done.')