# YouTube Ad Skipper

A Python automation script that uses computer vision to automatically detect and skip YouTube ads while they are playing.

## Features
* Automatically detects and skips ads using image recognition
* Dynamically loads target button images from an `ad-screenshots` folder
* Runs in the background and simulates mouse clicks exactly where needed
* Built-in fail-safe: press and hold the 'x' key to instantly stop the program

## Usage
Run the Python script to start the background scanner. Make sure you have screenshots of the current YouTube "Skip Ad" buttons saved as `.png` files inside the `ad-screenshots` directory. The program will continuously scan your screen. Press and hold the `x` key at any time to safely stop the execution. 

## Required Python Packages

* `opencv-python` (`cv2`) - Used for computer vision and template matching to find the buttons on screen
* `PyAutoGUI` - Takes screen captures and simulates the actual mouse clicks
* `keyboard` - Monitors keystrokes to provide the emergency stop hotkey
* `numpy` - Processes the image data arrays required by OpenCV

## Important Note for Non-English YouTube Users

If your YouTube interface is not set to English, the default screenshots in the `ad-screenshots` folder may not work. You may need to replace them with your own screenshots of the "Skip Ad" buttons in your language. Additionally, you can add more screenshots to improve detection accuracy for different button styles.