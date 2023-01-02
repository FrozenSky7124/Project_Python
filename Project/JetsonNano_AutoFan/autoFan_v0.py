#!/usr/bin/python
import time
downThres = 48
upThres = 58
baseThres = 40
ratio = 5
sleepTime = 30
 
while True:
    fo = open("/sys/class/thermal/thermal_zone0/temp","r")
    # thermal_zone1 是 CPU 温度
    # thermal_zone2 是 GPU 温度
    # thermal_zone0 是封装的温度
    thermal = int(fo.read(10))
    fo.close()
 
    thermal = thermal / 1000
    print("Temperature: " + str(thermal))

    if thermal < downThres:
        thermal = 0
    elif thermal >= downThres and thermal < upThres:
        thermal = baseThres + (thermal - downThres) * ratio
    else:
        thermal = thermal
 
 
    thermal = str(thermal)
     
    fw=open("/sys/devices/pwm-fan/target_pwm","w")
    fw.write(thermal)
    fw.close()
 
    time.sleep(sleepTime)