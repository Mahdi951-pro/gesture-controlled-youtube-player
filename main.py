import cv2
import mediapipe as mp
import pyautogui
import pygetwindow as gw
import time

# Initialize MediaPipe Hands and drawing utilities
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Webcam feed
cap = cv2.VideoCapture(0)

# Gesture Control Settings
gesture_delay = 1.5  # seconds to avoid rapid gesture switching
last_gesture_time = 0  # track last gesture time
last_gesture = None  # track last gesture


# Advanced gesture detection logic
def detect_gesture(landmarks):
    thumb_tip = landmarks[4]
    index_tip = landmarks[8]
    middle_tip = landmarks[12]
    ring_tip = landmarks[16]
    pinky_tip = landmarks[20]

    # Detect pinch gesture for play/pause
    if thumb_tip.y < index_tip.y < middle_tip.y and abs(thumb_tip.x - index_tip.x) < 0.05:
        return "play_pause"

    # Detect volume up/down gestures based on hand movement
    if index_tip.y < middle_tip.y < ring_tip.y < pinky_tip.y:  # all fingers upwards
        if thumb_tip.y < index_tip.y:  # Volume up
            return "volume_up"
        elif thumb_tip.y > pinky_tip.y:  # Volume down
            return "volume_down"

    # Detect seek forward/backward based on hand moving horizontally
    if thumb_tip.x < pinky_tip.x:  # Moving right
        return "forward"
    elif thumb_tip.x > pinky_tip.x:  # Moving left
        return "backward"

    # Detect mute/unmute gesture (palm facing the camera)
    if abs(thumb_tip.x - pinky_tip.x) < 0.05 and abs(index_tip.x - ring_tip.x) < 0.05:
        return "mute"

    return None


# Gesture control function for YouTube
def control_youtube(gesture):
    global last_gesture_time, last_gesture
    current_time = time.time()

    # Debounce gestures (avoid triggering the same gesture multiple times quickly)
    if gesture == last_gesture and (current_time - last_gesture_time) < gesture_delay:
        return

    last_gesture_time = current_time
    last_gesture = gesture

    # Activate YouTube window
    youtube_windows = [w for w in gw.getWindowsWithTitle('YouTube') if w.isActive]
    if youtube_windows:
        window = youtube_windows[0]
        window.activate()
    else:
        print("YouTube window not found!")

    # Perform actions
    if gesture == "play_pause":
        pyautogui.press('space')
    elif gesture == "volume_up":
        pyautogui.press('volumeup')
    elif gesture == "volume_down":
        pyautogui.press('volumedown')
    elif gesture == "forward":
        pyautogui.press('right')
    elif gesture == "backward":
        pyautogui.press('left')
    elif gesture == "mute":
        pyautogui.press('m')


# Main loop
while True:
    success, img = cap.read()
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get landmarks
            landmarks = hand_landmarks.landmark
            gesture = detect_gesture(landmarks)

            # Perform YouTube control based on detected gesture
            if gesture:
                control_youtube(gesture)
                cv2.putText(img, f"Gesture: {gesture}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2,
                            cv2.LINE_AA)

    # Display the live video feed with gesture feedback
    cv2.imshow('Advanced Hand Gesture YouTube Control by MAHDI', img)

    if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
        break

cap.release()
cv2.destroyAllWindows()
