import time
import random

from paho.mqtt import client as mqtt

def on_message(client, userdata, message):
    print("Message Received:" + str(message.payload.decode("utf-8")))

broker = "broker.hivemq.com"
print(broker)
port = "1883"
client = mqtt.Client("Receiver")
client.connect(broker)
print("Connected")

client.loop_start()
client.subscribe("EMPFANGEN")
client.on_message = on_message
time.sleep(30)
client.loop_stop()