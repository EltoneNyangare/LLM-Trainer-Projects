import pyautogui
import os
import time
from datetime import datetime
import csv

# Configuration
SAVE_DIR = os.path.join(os.path.expanduser("~"), "ScreenLogger")
METADATA_FILE = os.path.join(SAVE_DIR, "metadata.csv")
INTERVAL = 30  # seconds
COUNT = 5      # number of screenshots

os.makedirs(SAVE_DIR, exist_ok=True)

def capture_screenshots():
    with open(METADATA_FILE, "w", newline="") as csvfile:
        fieldnames = ["filename", "timestamp", "width", "height"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for i in range(COUNT):
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"screenshot_{timestamp}.png"
            path = os.path.join(SAVE_DIR, filename)

            screenshot = pyautogui.screenshot()
            screenshot.save(path)

            writer.writerow({
                "filename": filename,
                "timestamp": timestamp,
                "width": screenshot.width,
                "height": screenshot.height
            })
            print(f"Saved {filename}")
            time.sleep(INTERVAL)

if __name__ == "__main__":
    print("Starting screenshot logger...")
    capture_screenshots()
    print("All screenshots saved in:", SAVE_DIR)