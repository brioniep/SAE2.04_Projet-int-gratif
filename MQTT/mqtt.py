import paho.mqtt.client as mqtt #pip install mysql-connector-python
import pymysql #pip install pymysql
from datetime import datetime

broker = "test.mosquitto.org"
topic = "IUT/Colmar2024/SAE2.04/Maison1"
port = 1883

# Connexion MySQL
db = pymysql.connect(
    host="localhost",
    user="siteusr",
    password="2503",
    database="SiteCollecte"
)
cursor = db.cursor()

sensors = {}

# Callback de connexion MQTT
def on_connect(client, userdata, flags, rc):
    print("Connecté avec le code de retour: " + str(rc))
    client.subscribe(topic)

# Callback de réception de message MQTT
def on_message(client, userdata, msg):
    message = msg.payload.decode('utf-8')
    print(f"Message reçu sur le topic {msg.topic}: {message}")
    process_message(message)

# Fonction pour traiter les messages reçus
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
        try:
            cursor.execute("INSERT INTO sensor (name, piece, emplacement) VALUES (%s, %s, %s)",
                           (sensor_id, piece, ''))
            db.commit()
            print(f"Capteur {sensor_id} inséré dans la base de données")
        except pymysql.Error as e:
            print(f"Erreur lors de l'insertion du capteur {sensor_id} : {e}")
            db.rollback()

    try:
        cursor.execute("INSERT INTO temperaturedata (sensor_id, timestamp, value) VALUES (%s, %s, %s)",
                       (sensor_id, timestamp, value))
        db.commit()
        print("Données insérées avec succès")
    except pymysql.Error as e:
        print(f"Erreur lors de l'insertion des données : {e}")
        db.rollback()

# Configuration et lancement du client MQTT
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, port, 60)

# Boucle de réception des messages MQTT
try:
    print("Démarrage de la boucle MQTT. Appuyez sur Ctrl+C pour arrêter.")
    client.loop_forever()
except KeyboardInterrupt:
    print("Interruption par l'utilisateur. Arrêt du programme.")
    client.disconnect()
    cursor.close()
    db.close()
