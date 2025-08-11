# **py-webcam-safety**

**py-webcam-safety** is a Python-based tool that automatically captures images from your webcam at regular intervals and saves them locally. It’s designed for personal security, workspace monitoring, and other ethical purposes.

⚠ **Disclaimer:** This tool is intended **only** for legal and ethical use. Unauthorized or non-consensual surveillance is strictly prohibited and may be illegal in your jurisdiction.

## **📖 Features**

*   Captures images from your webcam at 1-minute intervals.  
    
*   Saves photos with timestamped filenames.  
    
*   Runs quietly in the background with a system tray icon.  
    
*   Option to stop the capture from the tray menu.  
    
*   Automatically creates a save folder if it doesn’t exist.  
    

## **📂 Save Location**

By default, images are saved in:
```
D:/webcam_captures
```
You can change this in the code by modifying:
```
save_directory = "D:/webcam_captures"
```
## **🛠 Prerequisites**

Make sure you have **Python 3.7+** installed.  
Install the required dependencies:

bash

CopyEdit

pip install opencv-python pystray pillow

## **▶ Usage**

1.  Clone this repository:  
```
git clone https://github.com/afnan-nex/py-webcam-safety
cd py-webcam-safety
```
1.  Run the script:
```
python webcam_safety.py
```
1.  The console window will minimize, and a tray icon will appear.  
    
2.  To stop, right-click the tray icon and select **Quit**.  
    

## **⚖ Legal & Ethical Use**

*   **Do:** Use it to monitor your own workspace or personal area.  
    
*   **Do Not:** Use it to capture images without consent.  
    
*   **Note:** The author is not responsible for any misuse of this tool.  
    

## **📜 License**

This project is licensed under the MIT License.
