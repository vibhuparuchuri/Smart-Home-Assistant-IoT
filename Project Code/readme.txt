INTRODUCTION
------------
Smroom is an home/room monitoring/automation system that makes traditional appliances into smart devices.
Current implementation monitors air quality, humidity and temperature. It controls appliances such as fan,
humidifier, lights and air purifier. 

Requirements
------------
1) Hardware: Raspberry Pi, Grove Pi Kit, Grove Air Quality Sensor, Grove DHT11 sensor, Grove Light Intensity Sensor,
		  Camera,Grove Ultrasonic Sensor, Grove LED
2) Edge Services: Node-RED, Influx DB and Grafana
3) Cloud Services: Azure Cognitive Services ( Text to Speech, Speech to Text, Custom Vision)
4) Python Libraries: grovepi, pyaudio, picamera

Included Files/Folder
---------------------
1) Node-RED-MainFlow.json - The main flow of the application.
2) Node-RED-GrafanaFlow - The flow which stores data into Influxdb for the Grafana Dashboard to access.
3) Node-RED-AzureFlow - The flow which periodically sends data to Azure Iot Central Hub.
4) cam.py - python script to taka a picture for the Azure Custom Vision to access.
5) airQuality.py - python script to access the readings from the air quality sensor
6)mic.py - python script to capture sound from the microphone
7) tcss573 - Directory that contains all the above-mentioned python scripts. Paste this file in the Desktop of the Raspberry Pi.

Installation
------------
1) Update and Upgrade the Pi OS
2) Install Node-RED 
3) Install InfluxDB and Grafana servers
4) Install the above mentioned python libraries

Configuration
-------------
1) Start the Node-RED, InfluxDB and Grafana Servers.
2) Access Node-RED at the machine IP address through a browser and import the following files:
	i)Node-RED-MainFlow.json
	ii) Node-RED-GrafanaFlow.json
	iii) Node-RED-AzureFlow.json
Note: Install the necessary nodes if not already installed.
3) Deploy the flow.
4) Access the Node-RED dashboard UI to monitor and control the system.
5) Build and access the Grafana (Smroom-Grafana-Dashboard.json) and Azure Central Iot Application dashboards.

Note
----
If keys are missing in nodes, please replace with the following keys:
1)Azure Custom Vision Model
	i)Prediction URL: https://assignment1-prediction.cognitiveservices.azure.com/customvision/v3.0/Prediction/fb2797fa-9c4a-4545-a20b-5ddfc2abaebe/classify/iterations/Iteration2/image
	ii) Prediction- Key: bc6a57279acb40b6ae6635f23b2999bf
	
2) Azure Speech Service:
	i)Ocp-Apim-Subscription-Key = []
	ii) URL: https://westus.api.cognitive.microsoft.com/sts/v1.0/issueToken
