
from queue import Queue
import threading
import json
import time
import subprocess



class PingThread(threading.Thread):
    def __init__(self,thread_id,queue):
        super().__init__() 
        self.thread_id = thread_id  
        self.queue = queue
    
    def run(self):
        self.scheduler()
    # 模拟任务调度
    def scheduler(self):
        while True:
            if self.queue.empty(): #队列为空不处理
                break
            else:
               
                ipVal = self.queue.get()
                print('ping线程为：',self.thread_id," ip地址为",ipVal)
                try:
                    if mutex.acquire(1):
                       start = time.time()
                       out = subprocess.check_output('ping -w 1 %s'%ipVal)
                       if out is not None:                     
                           end = time.time()
                           res_time = end-start
                           global ipRes
                           ipRes.append('扫描线程:'+str(self.thread_id)+'ip:'+ipVal+'执行时间：'+str(res_time))
                           print('扫描器线程为：',self.thread_id,'执行时间为：',res_time)
                    mutex.release()
                except Exception as e:
                    print('ip 异常 :',ipVal,e)
                    mutex.release()


ipRes = [] #存放ping结果的队列
flag = False
mutex = threading.Lock()

if __name__ == '__main__':
    # 将结果保存到一个json文件中
    f = open('./ipresult.json','a+',encoding='utf-8') 

    # 任务队列，存放ip队列
    ipQueue = Queue(20) 
    for ipItem in range(120,125): 
        tempIp='61.135.169.'+str(ipItem)
        ipQueue.put(tempIp) 
    
    # ping线程
    ping_threads = []
    ping_name_list = ['ping_1','ping_2','ping_3'] 
    for thread_id in ping_name_list:
        thread = PingThread(thread_id,ipQueue)
        thread.start() 
        ping_threads.append(thread)

    # 结束ping线程
    for t in ping_threads:
        t.join()
    flag =True
    
    
    for iptemp in ipRes:
        print("ip:",iptemp)
        f.write(iptemp)

    f.close()
    
    