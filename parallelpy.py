#coding: utf-8
import logging, threading
from queue import Queue
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(message)s')
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)
fibo_dict = {}
shared_queue = Queue()
input_list = [3, 10, 5, 7]