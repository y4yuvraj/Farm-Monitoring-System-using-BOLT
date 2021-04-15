"""
NAME:  YUVRAJ SINGH
DATE:  13 NOVEMBER 2019
PROJECT:  DESIGN A SYSYTEM FOR AGRICULTURE TO IMPROVE THE CROP PRODUCTIVITY.

"""
# HERE I AM IMPORTING ALL THE NECESSARY LIBRARIES.
import conf
import json, time, math, statistics,requests 
from boltiot import Sms, Bolt

def integromat(temp):
    URL = "https://hook.integromat.com/3ffxclp1jfaphgvhgvghvghtvrle2lljsmyr61"# REPLACE WITH CORRECT URL
    temp=temp/10.24 # converting temperature from ferhenite to celsius and round up the value
    response = requests.get(URL,data={'temp':temp})#sending sensor value with web request
    print(temp)
    print (response.text)
    

# I MADE A FUNCTION TO CALCULATE UPPER BOUND AND LOWER BOUND FOR OUR POLYNOMIAL REGRESSION. 

def compute_bounds(history_data,frame_size,factor):
    if len(history_data)<frame_size :
        return None

    if len(history_data)>frame_size :
        del history_data[0:len(history_data)-frame_size]
    Mn=statistics.mean(history_data)# calculating mean
    Variance=0
    for data in history_data :
        Variance += math.pow((data-Mn),2)#calculating variance
    Zn = factor * math.sqrt(Variance / frame_size)#calculating z-score
    High_bound = history_data[frame_size-1]+Zn
    Low_bound = history_data[frame_size-1]-Zn
    return [High_bound,Low_bound]#passing in a list

bolt = Bolt(conf.API_KEY, conf.DEVICE_ID)
history_data=[]
# SINCE WE WANT TO CONNTINUOUSLY MONITOR THE ANOMALY IN LIGHT WE ENCLOSE OUR LOGIC INSIDE AN INFINITE LOOP.

while True:
    response=bolt.serialRead('1')
    data=json.loads(response)# converting to dictionary
    sensor_value = list(data['value'].split("\n"))  #SINCE THE VALUE RETURNED IS IN DICTIONARY FORMAT.

    
    if data['success'] != 1 or len(sensor_value)<2:
        print("There was an error while retriving the data.")
        print("This is the error:"+data['value'])
        time.sleep(10)
        continue
    
    try:
        temp_value = int(sensor_value[-2])#extraction of temperature value from data
        print("Temperature value is "+str(temp_value))
    except e:
        print("There was an error while parsing the response: ",e)
        time.sleep(10)
        continue

    bound = compute_bounds(history_data,conf.FRAME_SIZE,conf.MUL_FACTOR)
    if not bound:
        required_data_count=conf.FRAME_SIZE-len(history_data)
        print("Not enough data to compute Z-score. Need ",required_data_count," more data points") # FOR PREDICTION.
        history_data.append(temp_value)
        time.sleep(10)
        continue

    try:
        if (temp_value) > bound[0]: #IF VALUE GREATER THAN HIGH_BOUND
            print ("Alert")
            integromat(temp_value)
        history_data.append(temp_value);
    except Exception as e:
        print ("Error",e)
    time.sleep(10) # LOOP WAITS FOR EVERY 10 SECOND BEFORE CONTINUING THE LOOP.