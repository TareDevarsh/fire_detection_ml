# Fire detection Using TensorFlow Image classification Alert System

## Overview

This repository contains code for an image recognition model retrained to detect the presence of fire in a scene. When a potential fire hazard is identified, the system utilizes the Twilio library to send an automated message to a specified WhatsApp number, notifying about the detected fire.

## Features

- **Fire Detection Model:** The image recognition model has been retrained to accurately identify the presence of fire in images or video frames.
- **Twilio Integration:** The system is integrated with the Twilio library to enable automated messaging. In case of a fire detection, an alert message is sent to a designated WhatsApp number.
- **Real-time Monitoring:** The system can be used for real-time monitoring of an area, providing timely alerts in case of a fire hazard.

## Dependencies

- Python 3.x
- TensorFlow or PyTorch (depending on the model used)
- Twilio Python Library



[![Demo](fire_detect.gif)](https://youtu.be/Ef-9cuemNSs)

