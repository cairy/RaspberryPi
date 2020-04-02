#!/usr/bin/env python
# encoding: utf-8

import time
import sys
# sys.path.append('/storage/.kodi/addons/virtual.rpi-tools/lib')
import RPi.GPIO

RPi.GPIO.setwarnings(False)
RPi.GPIO.setmode(RPi.GPIO.BCM)
RPi.GPIO.setup(2, RPi.GPIO.OUT)
pwm = RPi.GPIO.PWM(2,100)
RPi.GPIO.setwarnings(False)

#启动温度
start = 65000
#停止温度
stop = 45000
#速度
speed = 0
#是否停止状态
isstoped = True

try:
    while True:
        with open('/sys/class/thermal/thermal_zone0/temp') as tmpFile:
            cpu_temp = int(tmpFile.read())
        if cpu_temp>=start and isstoped: #从停止状态启动
            #启动时防止风扇卡死先全功率转0.1秒
            pwm.start(0)
            pwm.ChangeDutyCycle(100)
            time.sleep(.1)
            isstoped=False
            speed = min( cpu_temp/125-257 , 100 )
            pwm.ChangeDutyCycle(speed)
        elif cpu_temp>stop and not isstoped:
            speed = min( cpu_temp/125-257 , 100 )
            pwm.ChangeDutyCycle(speed)
        elif not isstoped :
            pwm.stop()
            isstoped = True
        time.sleep(10)
				
except KeyboardInterrupt:
		pass
pwm.stop()
