import os
import random
from multiprocessing import Process, Manager, current_process
import time

def producer_task(q, fibo_dict):
    for i in range(15):
        value = random.randint(1, 20)
        fibo_dict[value] = None
        print("Producer [%s] putting value [%d] into queue.. " % (current_process().name, value))
        q.put(value)
        time.sleep(0.5)  # Add a small delay to simulate work

def consumer_task(q, fibo_dict):
    while not q.empty():
        value = q.get(True, 0.05)
        a, b = 0, 1
        for item in range(value):
            a, b = b, a + b
        fibo_dict[value] = a
        print("Consumer [%s] getting value [%d] from queue..." % (current_process().name, value))
        time.sleep(1)  # Add a delay to simulate processing time

if __name__ == '__main__':
    manager = Manager()
    fibo_dict = manager.dict()
    data_queue = manager.Queue()

    producer = Process(target=producer_task, args=(data_queue, fibo_dict))
    producer.start()

    number_of_cpus = os.cpu_count()
    consumer_list = []
    for i in range(number_of_cpus):
        consumer = Process(target=consumer_task, args=(data_queue, fibo_dict))
        consumer.start()
        consumer_list.append(consumer)

    producer.join()

    for consumer in consumer_list:
        consumer.join()

    print("Final contents of fibo_dict:")
    for key, value in fibo_dict.items():
        print(f"{key}: {value}")

