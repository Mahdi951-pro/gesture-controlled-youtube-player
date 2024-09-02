# Gesture-Controlled YouTube Player

## Project Overview

This project enables you to control YouTube playback using hand gestures detected by your webcam. With this system, you can perform various actions like play/pause, volume control, seeking, and more, simply by showing specific hand gestures to the camera.

## Features

- **Play/Pause**: Show your open palm facing the camera.
- **Volume Up**: Give a thumbs-up gesture.
- **Volume Down**: Give a thumbs-down gesture.
- **Seek Forward**: Move a closed fist from left to right across the camera frame.
- **Seek Backward**: Move a closed fist from right to left across the camera frame.
- **Fullscreen Toggle**: Show your index and middle fingers pointing upwards.
- **Subtitles Toggle**: Show a peace sign (V sign) gesture.
- **Mute/Unmute**: Show a closed fist facing the camera.

## Technologies Used

- **Python 3.x**
- **OpenCV**: For capturing and processing video frames from the webcam.
- **Mediapipe**: For hand tracking and gesture recognition.
- **PyAutoGUI**: For controlling the system's mouse and keyboard actions.

## Installation and Setup

### Prerequisites

- **Python 3.x** installed on your system.
- A **webcam** to capture your hand gestures.

### Step 1: Clone the Repository

Clone this repository to your local machine using the following command:

bash
git clone https://github.com/Mahdi951-pro/gesture-controlled-youtube-player.git
### Step 2: Install Required Libraries
Navigate to the project directory and install the required Python libraries:

bash
Copy code
pip install opencv-python mediapipe pyautogui
### Step 3: Run the Script
You can run the project script with the following command:

bash
Copy code
python gesture_controlled_youtube.py
### Step 4: Use the Gestures
Once the script runs, use the specified hand gestures in front of the camera to control YouTube playback.

Running the Project in PyCharm
### Step 1: Open the Project in PyCharm
Open PyCharm and navigate to File > Open.
You can just select the project directory you cloned earlier.
### Step 2: Install the Required Libraries
Open the Terminal in PyCharm.
Run the following command to install the necessary libraries:
bash
Copy code
pip install opencv-python mediapipe pyautogui
### Step 3: Run the Script
Right-click on the gesture_controlled_youtube.py file in the Project Explorer.
Select Run 'gesture_controlled_youtube.py'.
The script will start, and you can use the gestures to control YouTube playback.
Gesture Definitions
Gesture	Action	Description
Open Palm	Play/Pause	Show your open palm facing the camera.
Thumbs Up	Volume Up	Give a thumbs-up gesture.
Thumbs Down	Volume Down	Give a thumbs-down gesture.
Swipe Right (Closed Fist)	Seek Forward	Move a closed fist from left to right across the camera frame.
Swipe Left (Closed Fist)	Seek Backward	Move a closed fist from right to left across the camera frame.
Two Fingers Up	Fullscreen Toggle	Show index and middle fingers pointing upwards.
Peace Sign	Subtitles Toggle	Show a peace sign (V sign) gesture.
Fist	Mute/Unmute	Show a closed fist facing the camera.
Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Special thanks to OpenCV, Mediapipe, and PyAutoGUI developers for their amazing libraries.

