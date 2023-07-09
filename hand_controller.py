import cv2
from cvzone.HandTrackingModule import HandDetector
from pynput.keyboard import Key, Controller
import numpy as np
import keyboard

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
# cap.set(3, 1920)
# cap.set(4, 1080)

detector = HandDetector(detectionCon=0.7, maxHands=2)
keyboard = Controller()

def checkHandClosed(hand):
    """
    Determines if the hand is closed based on the position of the fingers.
    """
    fingers = detector.fingersUp(hand)
    return sum(fingers) == 0

def get_hand_orientation(hand):
    """
    Calculates the orientation of the hand based on the position of the fingers.
    Returns either "Vertical" or "Horizontal".
    """
    fingers = detector.fingersUp(hand)
    if fingers[1:] == [1, 1, 1, 1]:
        return "Vertical"
    elif fingers[:2] == [0, 0] and fingers[2:]:
        return "Horizontal"
    else:
        return None

def main():
    while True:
        _, img = cap.read()
        hands, img = detector.findHands(img)

        if hands:
            for hand in hands:
                orientation = get_hand_orientation(hand)

                # Determine if left or right hand is detected
                if hand['type'] == "Left":
                    # Left hand detected
                    if orientation == "Vertical":
                        # Palm is open
                        if all(finger == 1 for finger in detector.fingersUp(hand)):
                            keyboard.press(Key.up)
                            keyboard.release(Key.down)
                        else:
                            keyboard.release(Key.up)
                            keyboard.release(Key.down)
                    else:
                        # Palm is closed
                        if checkHandClosed(hand):
                            keyboard.press(Key.down)
                            keyboard.release(Key.up)
                        else:
                            keyboard.release(Key.down)
                            keyboard.release(Key.up)
                else:
                    # Right hand detected
                    if orientation == "Vertical":
                        # Palm is open
                        if all(finger == 1 for finger in detector.fingersUp(hand)):
                            keyboard.press(Key.right)
                            keyboard.release(Key.left)
                        else:
                            keyboard.release(Key.right)
                            keyboard.release(Key.left)
                    else:
                        # Palm is closed
                        if checkHandClosed(hand):
                            keyboard.press(Key.left)
                            keyboard.release(Key.right)
                        else:
                            keyboard.release(Key.left)
                            keyboard.release(Key.right)
        else:
            keyboard.release(Key.up)
            keyboard.release(Key.down)
            keyboard.release(Key.left)
            keyboard.release(Key.right)

        cv2.imshow("Tracker", img)
        if cv2.waitKey(1) == ord("q"):
            break 
        
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()