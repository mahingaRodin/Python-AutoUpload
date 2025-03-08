import paho.mqtt.client as mqtt
import base64

# Callback function for when the client connects to the broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker successfully.")
        client.subscribe("/instructor_gabriel")  # Subscribe to instructor's topic
    else:
        print(f"Failed to connect, return code {rc}")

# Callback function for when a message is received
def on_message(client, userdata, msg):
    print(f"Instructor Gabriel: {msg.payload.decode()}")  # Display messages from the instructor

# MQTT client setup
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
BROKER_ADDRESS = "82.165.97.169"
PORT = 1883

try:
    client.connect(BROKER_ADDRESS, PORT, 60)
    client.loop_start()  # Start network loop in a separate thread
except Exception as e:
    print(f"Failed to connect to MQTT broker: {e}")
    exit(1)

# Define the student's topic (replace 'your_name' with actual name)
student_topic = "/mahinga_rodin"

while True:
    option = input("Type 'text' to send a message or 'image' to send a picture: ").strip().lower()

    if option == "text":
        message = input("Enter your message: ").strip()
        client.publish(student_topic, message)  # Send text message
        print("Message sent successfully.")

    elif option == "image":
        image_path = input("Enter the image file path (e.g., 'picture.jpg'): ").strip()

        try:
            # Read and encode the image in Base64
            with open(image_path, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read()).decode("utf-8")

            # Send image as Base64 string
            client.publish(student_topic, f"image:{encoded_string}")
            print("Image sent successfully!")

        except FileNotFoundError:
            print("Error: File not found. Please check the file path.")
        except Exception as e:
            print(f"Error sending image: {e}")

    else:
        print("Invalid option. Please type 'text' or 'image'.")
