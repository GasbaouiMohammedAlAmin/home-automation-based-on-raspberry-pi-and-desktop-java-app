import socket
import time
import serial

UDP_IP_desktop = "192.168.1.200"
UDP_IP_rasp = "192.168.1.203"
UDP_PORT = 5007
test_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
running = True 

def Send_temperature() :
   global running
   running = True
   
   last_time = 0
   count=0
   print('running ',running)
   while running:
       try:
          current_time = time.time()
          if(current_time > last_time + 1):
              last_time = current_time
              ser=serial.Serial('/dev/ttyACM0',9600)
              read_serial=0
              read_serial=ser.readline().decode("utf-8")
              count=count+1
              c=str(read_serial)
              test_socket.sendto(c.encode(), (UDP_IP_desktop, UDP_PORT))
              print("temperature ",c)
          
          if count >7 : 
         
            running = False
       except Exception:
       
         running = False
         test_socket.close()
#         raise
   test_socket.close()
#test_socket.close()

