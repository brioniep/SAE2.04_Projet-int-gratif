import csv
import paho.mqtt.client as mqtt
from datetime import datetime

broker = "test.mosquitto.org"
topic = "IUT/Colmar2024/SAE2.04/Maison1"
port = 1883
messages = []
sensors = {}

#fonctions mqtt
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(topic)

def on_message(client, userdata, msg):
    message = msg.payload.decode('utf-8')
    print(msg.topic + " " + message)
    messages.append(message)
    process_message(message)

#fonctions csv
def process_message(message):
    data = {}
    for item in message.split(','):
        key, value = item.split('=')
        data[key.strip()] = value.strip()

    sensor_id = data['Id']
    piece = data['piece']
    timestamp = datetime.strptime(f"{data['date']} {data['time']}", "%d/%m/%Y %H:%M:%S")
    value = float(data['temp'])


    if sensor_id not in sensors:
        sensors[sensor_id] = {
            'Nom': sensor_id,
            'Piece': piece,
            'Emplacement': ''
        }


    write_data_to_csv(sensor_id, timestamp, value)

def write_data_to_csv(sensor_id, timestamp, value):
    with open("donnees.csv", "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([sensor_id, timestamp, value])

def write_sensors_to_csv():
    with open("capteurs.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'Nom', 'Piece', 'Emplacement'])
        for idx, (sensor_id, sensor_data) in enumerate(sensors.items(), start=1):
            writer.writerow([idx, sensor_data['Nom'], sensor_data['Piece'], sensor_data['Emplacement']])

#main loop
try:
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(broker, port)
    client.loop_forever()
except KeyboardInterrupt:
    print("Fin du programme")
    client.disconnect()
    write_sensors_to_csv()