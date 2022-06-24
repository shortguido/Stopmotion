#Author Jakob Resch, Guido Kurz
#Dieses Programm wird am Raspberry Pi ausgeführt.

from picamera import PiCamera
from gpiozero import Button
import time
import random
from paho.mqtt import client as mqtt

seas = False
def on_message(client, userdata, message):
    empfang = str(message.payload.decode("utf-8"))  #Message wird decoded, ausgelesen und ausgegeben
    print("Message Received:" + empfang)
    if(empfang=="A"):
        seas = True



broker = "broker.hivemq.com"
print(broker)
client = mqtt.Client("Receiver")
client.connect(broker)
print("Connected")

client.loop_start()             #Start
client.subscribe("EMPFANGEN")   #Ist das gleiche Topic auf welches das die Androidapp published
client.on_message = on_message
camera = PiCamera()
camera.start_preview()
frame = 1

try:
    if (seas == True):  #Ein Foto wird geschossen wenn die Message von oben empfangen wird
        camera.capture('/home/pi/animation/frame%03d.jpg' % frame)
        frame += 1
        seas = False
except KeyboardInterrupt:
    camera.stop_preview()

