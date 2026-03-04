import threading
import time
def task1():
    for i in range (2):
        print("Task 1 is running")
        time.sleep(4)
def task2():
    for i in range (2):
        print("Task 2 is running")
        time.sleep(4)
t1=threading.Thread(target=task1)
t2=threading.Thread(target=task2)
t1.start()
t2.start()
t1.join()
t2.join()
print("Both tasks completed!")