# The Intelligent Disaster Management System with Alternative Energy and AI-Powered (Earlier version of the document)

### Objective
The objective of our project is to transition from a human-based observation to a camera-based system. Cameras have a much longer viewing distance than humans, and our system provides notifications much faster than manual methods, helping to avoid danger more effectively.

![](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/8veayyzala670qn96dwm.png)

---

### How Does It Work?
Our project has three main components:

1. **Wildfire Detection Pole**: This pole is set up in the forest to detect fires.
2. **Data Center**: It receives information from the Wildfire Detection Pole and sends it to the internet, allowing users to monitor the temperature and other data around the pole.
3. **Application**: A mobile app that provides essential wildfire-related features and notifications.

---

### Application Features
Our application includes five key features:

1. **Wildfire Location**
   - The app displays the locations of active wildfires. For example, if there are wildfires in three places, it lists those locations for easy reference.

2. **Hotline Call**
   - Users can directly call emergency hotlines from within the app.

3. **Location Sharing**
   - Users can share their current location with others. For instance, someone in the forest during a wildfire can send their location to request help.

4. **Environmental Data**
   - The app provides real-time data, including temperature, humidity, and gas levels around the pole.

5. **Alert System**
   - If a wildfire is detected, a red circle appears on the map to indicate the affected area. Users within this red circle receive a notification sound, prompting them to evacuate the danger zone.

![](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/5nnes5t0qy5qq33iyv17.png)

---

### The Wildfire Detection Pole
The Wildfire Detection Pole integrates the following components:

- **Raspberry Pi Pico Board**: Handles environmental sensors and initial data processing.
- **Raspberry Pi 5 Board**: Controls the camera and processes image data for object detection.
- **Camera System**: Rotates back and forth to scan the environment and detect wildfires.

#### How It Works
1. The Raspberry Pi 5 connects to the Raspberry Pi Pico and the camera, controlling the camera's rotation.
2. The camera uses an object detection system to identify wildfires. When a wildfire is detected:
   - The camera stops rotating and captures images of the wildfire.
   - These images and temperature and humidity data are sent to the Data Center.
3. If no wildfires are detected:
   - The camera continues rotating and pauses for 30 seconds after completing a full rotation.
   - Temperature and humidity data are sent every 30 minutes.

#### Data Transmission
- Data is encoded in two stages for efficiency
  1. **Run-Length Encoding (RLE)**: Compresses the data to reduce size.
  2. **Alphabet Replacement Encoding**: Further compresses the RLE data for transmission.
- The encoded data is sent to the Data Center via the NRF module.


![](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/l2i4m9xpfjubv2indmda.png)
