import cv2
import numpy as np
from matplotlib import pyplot as plt

def set_camera_properties(cap):
    """Function to adjust camera properties."""
    properties = {
        'Brightness': (-64, 64, 0, cv2.CAP_PROP_BRIGHTNESS),
        'Contrast': (0, 64, 32, cv2.CAP_PROP_CONTRAST),
        'Saturation': (0, 128, 64, cv2.CAP_PROP_SATURATION),
        'White Balance Auto': (0, 1, 0, cv2.CAP_PROP_AUTO_WB),
        'White Balance Manual': (2800, 6500, 2800, cv2.CAP_PROP_WB_TEMPERATURE),
        'Gamma': (72, 500, 100, cv2.CAP_PROP_GAMMA),
        'Sharpness': (0, 6, 3, cv2.CAP_PROP_SHARPNESS),
        'Gain': (0, 100, 0, cv2.CAP_PROP_GAIN),
        'Hue': (-40, 40, 0, cv2.CAP_PROP_HUE),
        'Exposure Auto': (0, 1, 0, cv2.CAP_PROP_AUTO_EXPOSURE),
        'Exposure Absolute': (1, 5000, 500, cv2.CAP_PROP_EXPOSURE),
        'Focus Auto': (0, 1, 0, cv2.CAP_PROP_AUTOFOCUS),
        'Focus Absolute': (1, 1023, 280, cv2.CAP_PROP_FOCUS),
    }

    for name, (min_val, max_val, default, prop) in properties.items():
        if 'Auto' in name:
            print(f"Setting {name} to {default} (On: 1, Off: 0)")
            cap.set(prop, default)
        else:
            print(f"Setting {name} to default value: {default}")
            cap.set(prop, default)

def create_trackbars(window_name):
    """Creates trackbars for adjusting camera properties."""
    cv2.createTrackbar('White Balance', window_name, 2800, 6500, lambda x: None)
    cv2.createTrackbar('Exposure', window_name, 1, 5000, lambda x: None)
    cv2.createTrackbar('Focus', window_name, 1, 1023, lambda x: None)

def get_trackbar_values(window_name):
    """Gets the current values from the trackbars."""
    white_balance = cv2.getTrackbarPos('White Balance', window_name)
    exposure = cv2.getTrackbarPos('Exposure', window_name)
    focus = cv2.getTrackbarPos('Focus', window_name)
    return white_balance, exposure, focus

def capture_frames():
    """Function to capture frames from the camera with slider controls."""
    cap = cv2.VideoCapture(2)

    if not cap.isOpened():
        print("Error: Could not open the camera.")
        return

    set_camera_properties(cap)

    window_name = 'Camera'
    cv2.namedWindow(window_name)
    create_trackbars(window_name)

    print("Press 'q' to quit.")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture an image.")
            break

        # Get trackbar values
        white_balance, exposure, focus = get_trackbar_values(window_name)

        # Set camera properties based on trackbar values
        cap.set(cv2.CAP_PROP_WB_TEMPERATURE, white_balance)
        cap.set(cv2.CAP_PROP_EXPOSURE, exposure)
        cap.set(cv2.CAP_PROP_FOCUS, focus)

        cv2.imshow(window_name, frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            print("Quitting.")
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_frames()