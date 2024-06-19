import mysql.connector
import paho.mqtt.client as mqtt
import re

# Paramètres de connexion au broker MQTT
broker = "test.mosquitto.org"
topic = "IUT/Colmar2024/SAE2.04/Maison1"
port = 1883

# Paramètres de connexion à la base de données MySQL
db_host = "localhost"
db_user = "votre_utilisateur"
db_password = "votre_mot_de_passe"
db_name = "votre_base_de_donnees"

# Connexion à la base de données MySQL
def connect_to_db():
    return mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )

# Callback lors de la connexion au broker MQTT
def on_connect(client, userdata, flags, rc):
    print("Connecté avec le code de retour: " + str(rc))
    client.subscribe(topic)

# Fonction pour extraire les données du message
def parse_message(message):
    pattern = r'Id=(\w+),piece=(\w+),date=(\d{2}/\d{2}/\d{4}),heure=(\d{2}:\d{2}:\d{2}),temp=(\d+),(\d+)'
    match = re.match(pattern, message)
    if match:
        mqtt_id = match.group(1)
        piece = match.group(2)
        date = match.group(3)
        heure = match.group(4)
        temp_integer = match.group(5)
        temp_fraction = match.group(6)
        temperature = f"{temp_integer}.{temp_fraction}"
        return mqtt_id, piece, date, heure, temperature
    else:
        return None

# Fonction pour vérifier et insérer un capteur s'il n'existe pas
def check_and_insert_sensor(sensor_id, piece):
    connection = connect_to_db()
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT ID FROM Capteurs WHERE Nom = %s", (sensor_id,))
        result = cursor.fetchone()
        if result:
            sensor_db_id = result[0]
        else:
            cursor.execute("INSERT INTO Capteurs (Nom, Piece, Emplacement) VALUES (%s, %s, %s)", (sensor_id, piece, piece))
            connection.commit()
            sensor_db_id = cursor.lastrowid
        return sensor_db_id
    except mysql.connector.Error as err:
        print(f"Erreur: {err}")
    finally:
        cursor.close()
        connection.close()

# Callback lors de la réception d'un message MQTT
def on_message(client, userdata, msg):
    print(f"Message reçu sur le topic {msg.topic}: {msg.payload.decode()}")
    data = msg.payload.decode()
    parsed_data = parse_message(data)
    if parsed_data:
        mqtt_id, piece, date, heure, temperature = parsed_data
        sensor_db_id = check_and_insert_sensor(mqtt_id, piece)
        insert_data_into_db(mqtt_id, sensor_db_id, f"{date} {heure}", temperature)

# Fonction pour insérer les données dans la base de données MySQL
def insert_data_into_db(mqtt_id, sensor_id, timestamp, value):
    connection = connect_to_db()
    cursor = connection.cursor()
    try:
        sql = """
            INSERT INTO Donnees (ID, CapteurID, Timestamp, Valeur)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(sql, (mqtt_id, sensor_id, timestamp, value))
        connection.commit()
        print("Données insérées avec succès")
    except mysql.connector.Error as err:
        print(f"Erreur: {err}")
    finally:
        cursor.close()
        connection.close()

# Création d'un client MQTT
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Connexion au broker MQTT
client.connect(broker, port, 60)

# Boucle réseau MQTT
client.loop_forever()