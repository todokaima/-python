import threading
import time

sharedctr = 0
lock = threading.Lock()
semaphore = threading.BoundedSemaphore(1)

def inc():
    global sharedctr
    while True:
        print("Trhead %s trying to acquire semaphore..." %threading.current_thread().name)
        semaphore.acquire()
        print("Thread %s acquired semaphore, control = %d" %(threading.current_thread().name,sharedctr))
        try:
            if sharedctr < 5:
                sharedctr +=1
            else:
                break
        finally:
            semaphore.release()

def thread1(p):
    print("\nThread %s started" %threading.current_thread().name)
    inc()

def thread2(p):
    print("\nThread s% started" %threading.current_thread().name)
    inc()

def main():
    t1 = threading.Thread(target=thread1, name='T1', args=(0,))
    t1.start()
    t2 = threading.Thread(target=thread2, name='T2', args=(0,))
    t2.start()
    t1.join()
    t2.join()

if __name__ == '__main__':
    main()