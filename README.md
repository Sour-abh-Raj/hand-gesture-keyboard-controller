# Hand Gesture Keyboard Controller 👐💻

This Python project utilizes computer vision and hand tracking techniques to control your keyboard using hand gestures. It allows you to perform various keyboard actions by detecting the orientation and movement of your hands.

## Features 🌟

- Control keyboard actions with hand gestures
- Supports both left and right hands
- Recognizes vertical and horizontal hand orientations
- Provides real-time visualization of hand tracking

## Prerequisites 📋

Make sure you have the following libraries installed:

- cv2 (OpenCV)
- cvzone
- pynput
- numpy
- keyboard

You can install them using requirements.txt file:

```
pip install -r requirements.txt
```

## Usage 🚀

1. Connect a webcam to your computer.
2. Run the Python script.
3. A live video stream will open with hand tracking enabled.
4. Perform the following gestures with your hand:
   - ### Left Hand (Vertical):
     - Open Palm: Presses the Up arrow key
     - Closed Palm: Presses the Down arrow key
   - ### Right Hand (Vertical):
     - Open Palm: Presses the Right arrow key
     - Closed Palm: Presses the Left arrow key
   - ### Any Hand (Horizontal):
     - Open Palm: No action
     - Closed Palm: No action
5. To exit the program, press Q.

## Notes 📝

- Adjust the webcam resolution by uncommenting the cap.set() lines and setting your desired values.
- You can modify the gesture-based actions in the main() function according to your preferences.
