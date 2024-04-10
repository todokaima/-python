import threading
import time
sharedctr = 0
lock = threading.Lock()
def inc():
    global sharedctr
    while True:
        print("Thread %s has called the function and is trying to acquire lock" %threading.current_thread().name)
        with lock:
            if sharedctr < 15:
                sharedctr += 1
            else:
                print("Thread %s has not been able to acquire lock, \n\n\ncontrol variable =  %d" % (threading.current_thread().name,sharedctr))
                break
            print("Thread %s has acquired lock, \ncontrol = %d" % (threading.current_thread().name,sharedctr))

def thread1(p):
    print("Thread1 has started %s" % threading.current_thread().name)
    inc()

def thread2(p):
    print("Thread2 has started %s" % threading.current_thread().name)
    inc()

def main():
    t1 = threading.Thread(target=thread1, name = 'T1',args=(0,))
    t1.start()
    t1.join()
    t2 = threading.Thread(target=thread2, name = 'T2',args=(0,))
    t2.start()

    t2.join()
if __name__ == '__main__':
    main()
