import requests
import json
import sys
import time
import os
import threading

time_request_thread=[]
status_code_thread=[]
threads = []
threadLock = threading.Lock()


class myThread (threading.Thread):
   def __init__(self, threadID, name, callnumber,type,url):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.number= callnumber
      self.type = type
      self.url= url
   def run(self):
       time_requestT= time.time()
       startThread(self.name,self.number,self.type,self.url)
       time_endedT = time.time() - time_requestT
       print("finished "+ self.name+" Time: "+str(time_endedT))

def writeData(time,status):
    threadLock.acquire()
    time_request_thread.append(time)
    status_code_thread.append(status)
    threadLock.release()

def startThread(name,number,type,url):
    if type=="get":
        for i in range(0, number):
            time_request= time.time()
            status=getData(url)
            time_ended = time.time() - time_request
            print("thread:"+name+" Request Time:"+str(time_ended)+"  status:"+str(status))
            writeData(time_ended,status)
            print("Request number: "+str(i+1))

    elif type=="post":
        for i in range(0, number):
            time_request= time.time()
            status=postData(url)
            time_ended = time.time() - time_request
            print("thread:"+name+" Request Time:"+str(time_ended)+"  status:"+str(status))
            writeData(time_ended,status)
            print("Request number: "+str(i+1))

def getData(url):
    r = requests.get(url)
    return r.status_code

def postData(url):
    with open('data.json') as json_data:
        data= json.load(json_data)

    r= requests.post(url=url,json=data)
    return r.status_code


def main(argv):
    if int(argv[1])>1:
        nthreads = int(argv[1])
        for i in range(0,nthreads):
            thread = myThread(i+1,"thread-"+str(i),int(argv[2]),argv[3],argv[4])
            thread.start()
            threads.append(thread)
        for t in threads:
            t.join()
        totalMed=0
        countStatus=0
        for i in time_request_thread:
            totalMed= totalMed + i
        totalMed= totalMed/len(time_request_thread)
        for stat in status_code_thread:
            if stat== 200:
                countStatus= countStatus+1
        os.system('cls' if os.name=='nt' else 'clear')
        print("All done!")
        print("Biggest time waited:"+ str(max(time_request_thread)))
        print("Smallest time waited:"+ str(min(time_request_thread)))
        print("Average Time waited:"+str(totalMed))
        print("200 status code = "+ str(countStatus) +" in "+ str(len(status_code_thread)) )

    elif int(argv[1])==0:
        if argv[3]=="get":
            start_time = time.time()
            calls = int(argv[2])
            for i in range(0, calls):
                time_request= time.time()
                status=getData(argv[4])
                time_ended = time.time() - time_request
                os.system('cls' if os.name=='nt' else 'clear')
                print("Request Time:"+str(time_ended)+"  status:"+str(status))
                time_request_thread.append(time_ended)
                writeData(time_ended,status)
                print("Request number: "+str(i+1))
            elapsed_time = time.time() - start_time
            print("All done!")
            print("Final Time:"+str(elapsed_time))
            totalMed=0
            countStatus=0
            for i in time_request_thread:
                totalMed= totalMed + i
            totalMed= totalMed/len(time_request_thread)
            for stat in status_code_thread:
                if stat== 200:
                    countStatus= countStatus+1
            print("Biggest time waited:"+ str(max(time_request_thread)))
            print("Smallest time waited:"+ str(min(time_request_thread)))
            print("Average Time waited:"+str(totalMed))
            print("200 status code = "+ str(countStatus) +" in "+ str(len(status_code_thread)) )
        elif argv[3]=="post":
            start_time = time.time()
            calls = int(argv[2])
            for i in range(0, calls):
                time_request= time.time()
                status=postData(argv[4])
                time_ended = time.time() - time_request
                os.system('cls' if os.name=='nt' else 'clear')
                print("Request Time:"+str(time_ended) +"  status:"+str(status))
                time_request_thread.append(time_ended)
                writeData(time_ended,status)
                print("Request number: "+str(i+1))
            elapsed_time = time.time() - start_time
            print("All done!")
            print("Final Time:"+str(elapsed_time))
            totalMed=0
            countStatus=0
            for i in time_request_thread:
                totalMed= totalMed + i
            totalMed= totalMed/len(time_request_thread)
            for stat in status_code_thread:
                if stat== 200:
                    countStatus= countStatus+1
            print("Biggest time waited:"+ str(max(time_request_thread)))
            print("Smallest time waited:"+ str(min(time_request_thread)))
            print("Average Time waited:"+str(totalMed))
            print("200 status code = "+ str(countStatus) +" in "+ str(len(status_code_thread)) )
    else:
        print("Can't be lower than 0 or empty")
if __name__ == "__main__":
    main(sys.argv)
