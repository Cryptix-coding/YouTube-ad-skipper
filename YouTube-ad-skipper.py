import os
import time
import numpy as np
import cv2
import pyautogui
import keyboard

# Settings
THRESHOLD = 0.7 
TEMPLATE_DIR = "ad-screenshots"

def load_templates(directory):
    # Load all .png templates from directory dynamically
    templates = []
    
    # Check if directory exists
    if not os.path.exists(directory):
        print(f"[Error] Directory '{directory}' not found.")
        return templates

    for filename in os.listdir(directory):
        # Process only .png files
        if filename.lower().endswith(".png"):
            filepath = os.path.join(directory, filename)
            
            # Load in grayscale
            img = cv2.imread(filepath, 0)
            
            # Verify image was read correctly
            if img is not None:
                templates.append(img)
                print(f"[Info] Successfully loaded: {filename}")
            else:
                print(f"[Warning] Failed to read image: {filename}")
                
    return templates

def find_and_click_button(screenshot, template):
    # Find template in screenshot and click if threshold is met
    res = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= THRESHOLD)

    if loc[0].size != 0:
        # Calculate the center of the first match
        top_left = list(zip(*loc[::-1]))[0]
        template_height, template_width = template.shape[:2]
        center_x = top_left[0] + template_width // 2
        center_y = top_left[1] + template_height // 2

        # Click at the center of the detected template
        pyautogui.click(center_x, center_y)
        return True

    return False

def main():
    print("Loading ad templates...")
    templates = load_templates(TEMPLATE_DIR)
    
    if not templates:
        print("[Error] No templates loaded. Exiting.")
        return

    print("Scanner started! Press and hold 'x' to stop.")

    while True:
        if keyboard.is_pressed('x'):
            print("Program stopped.")
            break
            
        time.sleep(0.5)
        
        # Capture screen in grayscale
        screenshot_pil = pyautogui.screenshot().convert(mode="L")
        screenshot_np = np.asarray(screenshot_pil)
        
        # Check all templates
        for template in templates:
            if find_and_click_button(screenshot_np, template):
                print("[Action] Ad skipped!")
                break 

if __name__ == "__main__":
    main()