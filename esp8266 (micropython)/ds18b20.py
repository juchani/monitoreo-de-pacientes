
from time import sleep
from urequests import get as rq
import network
import ujson as json
from machine import Pin
import ds18x20,onewire

nic = network.WLAN(network.STA_IF)
nic.active(True)
user="host"
psw="contraseña"
nic.connect(user, psw)
led=Pin(2,Pin.OUT,value=0)
ow = onewire.OneWire(Pin(4))
ds = ds18x20.DS18X20(ow)
roms = ds.scan()
while True:
    try:
        sleep(2)
        ds.convert_temp()
        sleep(0.7)
        for rom in roms:
            temp=ds.read_temp(rom)
        print('Temperatura:',temp)
        print('Humedad: ' ,hum)
    except OSError as e:
        print('Failed to read sensor.')
    try:
        h=rq(url='https://api.thingspeak.com/update?api_key=R88V9IMH0YVGY3G9&field1={}'.format(temp))
        h=None
    except:
        led.on()
        nic = network.WLAN(network.STA_IF)
        nic.active(True)
        nic.connect(user,psw)
        sleep(3)
        led=Pin(2,Pin.OUT,value=0)
        
        
        

