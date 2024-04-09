import sys, time, random, re, requests
import concurrent.futures, multiprocessing
from multiprocessing import cpu_count, current_process, Manager

# Define a logger
import logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def producer_task(q, fibo_dict):
    for i in range(15):
        value = random.randint(1, 20)
        fibo_dict[value] = None

        logger.info("Producer [%s] putting value [%d] into queue.. " % (current_process().name, value))
        q.put(value)

def consumer_task(q, fibo_dict):
    while True:
        try:
            value = q.get(timeout=0.05)  # Use a timeout to prevent blocking indefinitely
        except queue.Empty:
            break  # Break if the queue is empty
        a, b = 0, 1
        for _ in range(value):
            a, b = b, a + b
        fibo_dict[value] = a
        logger.info("consumer [%s] getting value [%d] from queue..." % (current_process().name, value))

if __name__ == "__main__":
    number_of_cpus = multiprocessing.cpu_count()
    data_queue = multiprocessing.Queue()
    manager = Manager()
    fibo_dict = manager.dict()

    producer = multiprocessing.Process(target=producer_task, args=(data_queue, fibo_dict))
    producer.start()

    consumer_list = []
    for i in range(number_of_cpus):
        consumer = multiprocessing.Process(target=consumer_task, args=(data_queue, fibo_dict))
        consumer.start()
        consumer_list.append(consumer)

    producer.join()  # Wait for producer to finish

    # Add None to the queue for each consumer to signal them to exit
    for _ in range(number_of_cpus):
        data_queue.put(None)

    # Wait for consumers to finish
    for consumer in consumer_list:
        consumer.join()

    # Print fibonacci dictionary
    print("Fibonacci Dictionary:", fibo_dict)
