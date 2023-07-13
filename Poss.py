print("MQTT with Adafruit IO, initiating ...")
import sys
from Adafruit_IO import MQTTClient
import time
import random
import requests

AIO_FEED_ID = "UNTER DEM BAUM"
AIO_USERNAME = "DevAda5usr"
AIO_KEY = "aio_pdQe29kpqF5dgV8WjpXb6h4EC4CD"

client = MQTTClient(AIO_USERNAME , AIO_KEY)

#Push up randomized data every ten seconds
def execute_every_tenseconds():
  while True:
    #Create randomized values
    value1 = random.randrange(756, 2000, 3)
    value2 = random.randrange(40, 100, 2)
    value3 = random.randrange(1, 7, 1)
    #publish randomized values
    client.publish("sensor1", value1)
    client.publish("sensor2", value2)
    client.publish("sensor3", value3)
    #Receive data
    print(client.subscribe("sensor1"))
    time.sleep(10)


mess = ""
def processData(data):
    data = data.replace("!", "")
    data = data.replace("#", "")
    splitData = data.split(":")
    print(splitData)

def init_global_equation():
    headers = {}
    aio_url = "Your URL"
    x = requests.get(url = aio_url, headers = headers, verify = False)
    data = x.json()
    global_equation = data["last_value"]
    print("Get latest value:", global_equation)

def connected(client):
    print("Successfully connected")
    client.subscribe("button1")
    client.subscribe("button2")
    client.subscribe("Equation")
    


def message(client, feed_id, payload):
   print("Received: " + payload)
   if(feed_id == "Equation"):
      global_equation = payload
      print(global_equation)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe successful ...")

def disconnected(client):
    print("Terminate connection ...")
    sys.exit (1)


client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe

client.connect()
client.loop_background()

execute_every_tenseconds()




#client.subscribe("sensor1")
#client.subscribe("sensor2")
#client.subscribe("sensor3")