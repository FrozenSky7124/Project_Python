#!/usr/bin/python
import time
tempDown  = 48 # 起转温度(低于此温度风扇停转)
tempUp    = 60 # 高温温度(高于此温度风扇进入最高速)
speedBase = 50 # 基础转速(0~255)
speedTop  =200 # 最高转速(0~255)
ratio     =  5 # 转速系数
sleepTime = 30
 
while True:
    fo = open("/sys/class/thermal/thermal_zone0/temp","r")
    # thermal_zone1 是 CPU 温度
    # thermal_zone2 是 GPU 温度
    # thermal_zone0 是封装的温度
    thermal = int(fo.read(10))
    fo.close()
 
    thermal = thermal / 1000
    #print("Temperature: " + str(thermal))

    speed = speedBase

    if thermal < tempDown:
        speed = 0
    elif thermal >= tempDown and thermal < tempUp:
        speed = speedBase + (thermal - tempDown) * ratio
    elif thermal >= tempUp:
        speed = speedTop
    else:
        speed = speedBase

    if speed > 255:
        speed = 255
    speed = str(speed)
    print("Temperature: " + str(thermal) + "    FanSpeed: " + str(speed))
     
    fw=open("/sys/devices/pwm-fan/target_pwm","w")
    fw.write(speed)
    fw.close()
 
    time.sleep(sleepTime)
