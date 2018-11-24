import queue
import threading
import time 

exitFlag = 0 

class myThread (threading.Thread):
    def __init__(self,threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    
    def run(self):
        print("Starting " +self.name)
        process_data(self.name, self.q)
        print("Exiting "+ self.name)

def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print("%s processing %s " %(threadName, data))
        else:
            queueLock.release()
            time.sleep(1)


threadList = ["Thread-1","Thread-2","thread-3"]            
nameList=["one","two","three",'four','five']
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1 

# Create new threads
for tName in threadList:
    thread = myThread(threadID,tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

# fill queue
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

# wait for queue to empty 
while not workQueue.empty():
    pass
exitFlag = 1

# wait for thread all done 
for t in threads:
    t.join ()

print('done')


