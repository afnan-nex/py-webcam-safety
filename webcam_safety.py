import cv2
import os
import time
import pystray
from PIL import Image, ImageDraw
import threading
import ctypes

# Minimize the console window
def minimize_console():
    if os.name == "nt":  # Check if the OS is Windows
        # Minimize the console window
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 6)  # 6 = SW_MINIMIZE

# Specify the directory on the D: drive where you want to save the photos
save_directory = "D:/webcam_captures"

# Create the directory if it doesn't exist
os.makedirs(save_directory, exist_ok=True)

# Initialize the webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Function to capture and save an image
def capture_image(frame_count):
    ret, frame = cap.read()
    if ret:
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(save_directory, f"capture_{timestamp}_{frame_count}.jpg")
        cv2.imwrite(filename, frame)
        print(f"Saved: {filename}")
    else:
        print("Error: Could not capture image.")

# Function to create a system tray icon
def create_system_tray_icon():
    def on_quit(icon):
        icon.stop()
        cap.release()
        cv2.destroyAllWindows()
        print("Webcam released and script ended.")

    # Create an image for the system tray icon
    image = Image.new("RGB", (64, 64), "white")
    draw = ImageDraw.Draw(image)
    draw.rectangle((16, 16, 48, 48), fill="blue")

    # Create the system tray icon
    icon = pystray.Icon("webcam_capture", image, "Webcam Capture", menu=pystray.Menu(
        pystray.MenuItem("Quit", on_quit)
    ))

    # Run the system tray icon
    icon.run()

# Function to start capturing images in a separate thread
def start_capture():
    def capture_loop():
        frame_count = 0
        while not stop_capture:
            capture_image(frame_count)
            frame_count += 1
            time.sleep(60)  # Wait for 1 minute

    global stop_capture
    stop_capture = False
    threading.Thread(target=capture_loop, daemon=True).start()

# Minimize the console window and start capturing images
minimize_console()
start_capture()

# Create and run the system tray icon
create_system_tray_icon()
