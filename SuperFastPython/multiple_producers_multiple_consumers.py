#https://superfastpython.com/thread-producer-consumer-pattern-in-python/
# SuperFastPython.com
# example of multiple producers and multiple consumers with threads
from time import sleep
from random import random
from threading import Thread
from threading import Barrier
from queue import Queue
 
# producer task
def producer(barrier, queue, identifier):
    print(f'Producer {identifier}: Running')
    # generate items
    for i in range(10):
        # generate a value
        value = random()
        # block, to simulate effort
        sleep(value)
        # create a tuple
        item = (i, value)
        # add to the queue
        queue.put(item)
    # wait for all producers to finish
    barrier.wait()
    # signal that there are no further items
    if identifier == 0:
        queue.put(None)
    print(f'Producer {identifier}: Done')
 
# consumer task
def consumer(queue, identifier):
    print(f'Consumer {identifier}: Running')
    # consume items
    while True:
        # get a unit of work
        item = queue.get()
        # check for stop
        if item is None:
            # add the signal back for other consumers
            queue.put(item)
            # stop running
            break
        # block, to simulate effort
        sleep(item[1])
        # report
        print(f'>consumer {identifier} got {item}')
    # all done
    print(f'Consumer {identifier}: Done')
 
# create the shared queue
queue = Queue()
# create the shared barrier
n_producers = 3
barrier = Barrier(n_producers)
# start the consumers
consumers = [Thread(target=consumer, args=(queue,i)) for i in range(5)]
for consumer in consumers:
    consumer.start()
# start the producers
producers = [Thread(target=producer, args=(barrier,queue,i)) for i in range(n_producers)]
# start the producers
for producer in producers:
    producer.start()
# wait for all threads to finish
for producer in producers:
    producer.join()
for consumer in consumers:
    consumer.join()