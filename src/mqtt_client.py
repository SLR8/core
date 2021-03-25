import paho.mqtt.client as mqtt
import logging
import asyncio
from .executor import executor


class MqttClient():
    def __init__(self, *args, **kwargs):
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

        self.topic = 'hello'
        # When in production change this to a non public one
        self.host = "broker.emqx.io"
        self.port = 1883
        self.keepalive = 60

        # try:
        #     logging.info(f'Connecting to broker {self.host}')
        #     asyncio.run(self.connect())
        #     logging.info("Connected ...")
        #     client.loop_forever()
        # except:
        #     pass

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code "+str(rc))

        print(f"Connected ? {client.is_connected()}")

        self.subscribe(self.topic)

    def on_message(self, client, userdata, msg):
        print(msg.topic+" "+str(msg.payload.decode()))
        param = executor(msg.payload.decode())
        self.client.publish(topic, param)
        

    def connect(self):
        logging.info('Trying to connect')
        self.client.connect(
            self.host, port=self.port, keepalive=self.keepalive)
        # try:
        # except:
        # logging.error("Failed to connect to a broker")

    def subscribe(self, topic):
        self.client.subscribe(topic)
        print(f"Subscribed to: {topic}")

    def publish_message(self, topic, message):
        try:
            self.client.publish(topic, message)
        except:
            logging.error('Failed to publish message')

    def loop(self):
        return self.client.loop_forever()



mqtt_client = MqttClient()