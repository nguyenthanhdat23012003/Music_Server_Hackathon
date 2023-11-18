import paho.mqtt.client as paho
import json
import pyglet
import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload
from drive import Drive

file_name = "test.mp3"
downloader = Drive()
def on_message(client, userdata, msg):
    global file_name
    byte_message = msg.payload
    string_message = byte_message.decode('utf-8')
    parsed_data = json.loads(string_message)
    command = parsed_data['command']
    if command == "play":
        sound = pyglet.media.load(file_name)
        sound.play()
        pyglet.app.run()
    else:
        downloader.download_file(file_name)
    print(command) 


client = paho.Client()
client.connect('broker.hivemq.com', 1883)
client.subscribe('/hapt/provide', qos=1)
client.on_message = on_message

client.loop_forever()