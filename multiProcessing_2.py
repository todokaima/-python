import sys, time, random, re, requests
import concurrent.futures, multiprocessing
from multiprocessing import cpu_count, current_process, Manager

def producer_task(q, fibo_dict):
    for i in range(15):
        value = random.randint(1,20)
        fibo_dict[value] = None

        logger.info("Producer [%s] putting value [%d] into queue.. " % (current_process().name, value))
        q.put(value)

def consumer_task(q, fibo_dict):
    while not q.empty():
        value = q.get(True, 0.05)
        a,b = 0, 1
        for item in range(value):
            a,b =b, a+b
            fibo_dict[value] = a
        logger.info("consumer [%s] getting value [%d] from queue..." % (current_process().name, value))

producer = multiprocessing.Process(target=producer_task, args=(data_queue,fibo_dict))
producer.start()
producer.join()

consumer_list = []
for i in range(number_of_cpus):
    consumer = multiprocessing.Process(target= consumer_task, args=(data_queue,fibo_dict))
    consumer.start()
    consumer_list.append(consumer)

[consumer.join() for consumer in consumer_list]
