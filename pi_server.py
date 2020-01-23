from socket import *
from time import ctime
import RPi.GPIO as GPIO
import time
import Send_thread_temp
#--------------------
GPIO.setmode(GPIO.BCM)
heater=26
light=23
fan=24
GPIO.setup(heater,GPIO.OUT)
GPIO.setup(light,GPIO.OUT)
GPIO.setup(fan,GPIO.OUT)
#intial the relay
GPIO.output(light,1) 
GPIO.output(fan,1) 
#---------------------
ctrCmd = ['heater_off','heater_on','light_on','light_off','fan_on','fan_off','temperature','stop']
print ('   welcome in application automation home base in raspberry  ')
time.sleep(1)
HOST ='' 
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST,PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

test=True
while test:
        print ('Waiting for connection')
        tcpCliSock,addr = tcpSerSock.accept()
        print ('...connected from :', addr)
        try:
                while True :
                        data = ''
                        data = tcpCliSock.recv(BUFSIZE).decode("utf-8")
                        print(data)
                        if not data:
                                break
                        if data == ctrCmd[0]:
                           GPIO.output(heater,0)   
                        if data == ctrCmd[1]:
                           GPIO.output(heater,1)
                        if data == ctrCmd[2]:
                           
                            GPIO.output(light,0)   
                        if data == ctrCmd[3]:
                            
                            GPIO.output(light,1)  
                        if data == ctrCmd[4]:
                            GPIO.output(fan,0)   
                        if data == ctrCmd[5]:
                            
                            GPIO.output(fan,1)  
                        if data == ctrCmd[6]:
                            Send_thread_temp.Send_temperature() 
                        if data == ctrCmd[7]:
                            test=False
                            print('thread was stopped')  
                                                    

        except KeyboardInterrupt:
               GPIO.cleanup()
tcpSerSock.close();
GPIO.cleanup()
