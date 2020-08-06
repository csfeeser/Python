#!/usr/bin/env python3
  
import netifaces

def act_inac():
     print(netifaces.interfaces)
     for i in netifaces.interfaces():
         print('\n****** details of interface - ' + i + ' ******')
         try:
             print('MAC: ', end='')
             print((netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]['addr'])
             print('IP: ', end='')
             print((netifaces.ifaddresses(i)[netifaces.AF_INET])[0]['addr'])
         except:          # This is a new line
             print('Could not collect adapter information')

act_inac()
