
import paho.mqtt.client as mqtt
import logging




        # When in production change this to a non public one
host = 'broker.emqx.io'
port = 1883
keepalive = 60

topic = 'world'
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    print(f"Connected ? {client.is_connected()}")
    
    subscribe(topic)
    publish_message(topic, "Hello")
    while True:
        message  = input('msg: ')
        client.publish(topic, message)
        # publish_message(topic, msg)
        print(f'Prompt: {message}')

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    

def subscribe(topic):
    print(f'Subscribed to: {topic}')
    return client.subscribe(topic)

def publish_message( topic, message):
    client.publish(topic, message)
    print(f'Published msg: {message}, on: {topic}')
   

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message


client.connect(host, port, keepalive)
# client.publish(topic, 'Help')
client.loop_forever()
