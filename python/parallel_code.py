#run a series of functions in parallel

from threading import Thread
from queue import Queue

q = Queue()

worker_count = 2

#sample code, we will call a function that prints a string
#a real world example might be creating data lake file from 
#an rds

fruit_list = ['apple','banana','cherry','grape','kiwi','pear']

#place a list of items to process in a queue
for fruit in fruit_list:
    q.put(fruit)

#generic function that calsl a function for items in a queue
def run_tasks(function, q):
    while not q.empty():
        value = q.get()
        function(value)
        q.task_done()

#the function we wish to call for each queue item
def print_table(name):
    print (name)

#process the queue
for i in range(worker_count):
    t=Thread(target=run_tasks, args=(print_table, q))
    t.daemon = True
    t.start()

#block main thread until workers have completed
q.join()