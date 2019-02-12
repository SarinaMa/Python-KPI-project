# ip address task 
#inport modules
import numpy as np
import pandas as pd
import requests
import json
import csv
import urllib
import time



url1='http://api.ipinfodb.com/v3/ip-city/?key=f1a05d974e0e3e74318b40f8ff40e6b97373716f130180e7eed912eb373dd937&ip=79.253.199.198&format=json'
r1 = requests.get(url1)
dic1=r1.json()
print(dic1)
with open('output2-7.csv', 'w') as f:
    w = csv.DictWriter(f, dic1.keys())
    w.writeheader()
    f.close()
    

with open ('input2.csv','r')as data_file:
    file=csv.reader(data_file,delimiter=',')
    next(file)
    ips=[]
    for row in file:
        ip_id=row[1]
        ips.append(ip_id)
    

    for i in ips:
        time.sleep(0.51)
        url1='http://api.ipinfodb.com/v3/ip-city/?key=f1a05d974e0e3e74318b40f8ff40e6b97373716f130180e7eed912eb373dd937&ip='+ i+'&format=json'
        r1 = requests.get(url1)
        dic1=r1.json()
        print(dic1)
            
        with open('output2-7.csv', 'a') as f:
            w = csv.DictWriter(f, dic1.keys())
            w.writerow(dic1)
            f.close()

            
        
     


##ip_id='84.181.96.116'
##url1='https://ipapi.co/84.181.96.116/json/'
##r1 = requests.get(url1)
##dic1=r1.json()
##print(dic1)
##        
      


#data_file=pd.read_csv( r"C:\Users\mashu\Desktop\IP_API_Task.csv")

#print(data_file[0:3])



##i=0
###def SearchFunc():
###while i<=10:
##ip_id=data_file.iloc[i,1]
##print(ip_id)
##url1='http://ip-api.com/json/'+ ip_id.to_string
##r1 = requests.get(url1)
##dic1=r1.json()
      
    
    

#print(dic1)    
    
    
