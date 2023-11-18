import paho.mqtt.client as paho
import time
import json
import schedule

current_scheduled_job = None
payload_publish = ''
client = paho.Client()
client.connect('broker.hivemq.com', 1883)

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed:")

def publish_file(client, file):
    client.publish
    
def on_message(client, userdata, msg):
    global current_scheduled_job
    schedule.cancel_job(current_scheduled_job)
    byte_message = msg.payload
    string_message = byte_message.decode('utf-8')
    print(string_message)
    parsed_data = json.loads(string_message)
    fileMessage = {}
    fileMessage['command'] = 'change'
    fileMessage['file_name'] = parsed_data['file']
    playMessage = {}
    playMessage['command'] = 'play'
    hour = parsed_data['hour']
    minute = parsed_data['minute']
    current_scheduled_job = schedule.every().day.at(hour+':' + minute).do(client.publish, '/hapt/provide',json.dumps(playMessage))
    (rc, mid) = client.publish('/hapt/provide', json.dumps(fileMessage), qos=1)


client.on_message = on_message

client.loop_start()
client.subscribe('/hapt/Pub', qos=1)

while True:
    schedule.run_pending()
    time.sleep(1)