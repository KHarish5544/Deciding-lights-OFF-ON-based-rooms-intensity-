import cv2
import numpy as np
import time

# Threshold value for intensity (adjust as needed)
threshold = 75

def calculate_avg_intensity(image):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Calculate the average intensity of the grayscale image
    avg_intensity = np.mean(gray_image)
    
    return avg_intensity

def light_decision(avg_intensity):
    # Decide whether to turn the light on or off based on intensity threshold
    if avg_intensity < threshold:
        return True  # Light should be ON
    else:
        return False  # Light should be OFF

def process_camera_input():
    # Capture video from the webcam
    cap = cv2.VideoCapture(0)

    # Check if the camera opened successfully
    if not cap.isOpened():
        print("Error: Unable to access the camera.")
        return
    
    try:
        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()
            
            if not ret:
                print("Failed to grab frame")
                break

            # Calculate the average intensity of the current frame
            avg_intensity = calculate_avg_intensity(frame)
            
            # Decide whether the light should be on or off
            light_status = light_decision(avg_intensity)

            # Display the result
            if light_status:
                print("ON")
            else:
                print("OFF")
            
            # Show the frame with a delay (you can remove this if you don't need to display the feed)
            cv2.imshow('Camera Feed', frame)
            
            # Wait for 0.5 minute (30 seconds) before checking again
            time.sleep(3)
            
            # Break the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    
    except KeyboardInterrupt:
        print("Program interrupted by user.")
    
    finally:
        # Release the capture and close all windows
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    process_camera_input()
