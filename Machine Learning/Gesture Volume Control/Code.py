import cv2
import mediapipe as mp
import numpy as np
import pycaw

# Initialize the mediapipe hand detection model
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Initialize the volume controller
volume = pycaw.Pycaw()
volMin, volMax = volume.GetVolumeRange()

# Create a video capture object
cap = cv2.VideoCapture(0)

while True:
    # Capture a frame from the webcam
    ret, frame = cap.read()

    # Process the frame with the hand detection model
    results = hands.process(frame)

    # Check if any hands were detected
    if results.multi_hand_landmarks:
        # Get the landmarks for the first hand
        hand = results.multi_hand_landmarks[0]

        # Get the x and y coordinates of the thumb and index finger
        thumb_x, thumb_y = hand.landmark[4].x, hand.landmark[4].y
        index_x, index_y = hand.landmark[8].x, hand.landmark[8].y

        # Calculate the distance between the thumb and index finger
        length = np.hypot(thumb_x - index_x, thumb_y - index_y)

        # Map the distance to the volume range
        volume_level = np.interp(length, [30, 350], [volMin, volMax])

        # Set the volume level
        volume.SetMasterVolumeLevel(volume_level)

    # Display the frame
    cv2.imshow('Frame', frame)

    # Press 'q' to quit
    if cv2.waitKey(1) == ord('q'):
        break

# Release the video capture object
cap.release()

# Close all windows
cv2.destroyAllWindows()
