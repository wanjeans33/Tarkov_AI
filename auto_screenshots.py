import pyautogui
import time
import datetime
import os

def capture_screenshots(interval, duration, save_path):
    """Capture screenshots at a set interval for a specified duration.
    
    Args:
        interval (int): Time in seconds between each screenshot.
        duration (int): Total time in seconds to run the capture process.
        save_path (str): Path to save the screenshot files.
    """
    # Check if the save path exists, if not, create it
    if not os.path.exists(save_path):
        os.makedirs(save_path)
        print(f"Created directory {save_path}")    
    start_time = time.time()
    end_time = start_time + duration
    
    i = 0
    while time.time() < end_time:
        filename = f"{save_path}/screenshot_{i}.png"
        screenshot = pyautogui.screenshot()
        screenshot.save(filename)
        print(f"Screenshot saved as {filename}")
        time.sleep(interval)
        i += 1

if __name__ == "__main__":
    # Set the time interval between each screenshot (e.g., every 10 seconds)
    INTERVAL = 1
    # Set how long to run the capture (e.g., for 1 hour = 3600 seconds)
    DURATION = 60 * 10
    # Set the path to save the screenshots
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    SAVE_PATH = f"./data/screenshots/screenshot_{timestamp}"
    
    capture_screenshots(INTERVAL, DURATION, SAVE_PATH)
