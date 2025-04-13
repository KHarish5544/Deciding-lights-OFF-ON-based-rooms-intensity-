💡 Automatic Light Controller Based on Ambient Intensity

This Python program uses a webcam feed to detect ambient light intensity in real-time and decides whether a light should be turned **ON** or **OFF** based on a predefined intensity threshold. It can be integrated into smart home or IoT systems for energy-efficient lighting.

📸 Features

- Captures live video feed from the webcam.
- Converts each frame to grayscale and calculates average intensity.
- Compares intensity with a threshold to determine light status.
- Displays real-time camera feed.
- Simple logic for light control simulation: prints "ON" or "OFF".

 🧠 Logic Behind

The light intensity is calculated by converting the frame to grayscale and computing the average pixel intensity. If the average is **below 75**, the light is turned **ON**; otherwise, it remains **OFF**.

🛠️ Requirements

Make sure you have the following Python packages installed:

```bash
pip install opencv-python numpy
```

🚀 How to Run

Clone this repository and run the script:

```bash
python light_controller.py
```

Exit

- Press **`q`** to exit the video stream window.
- You can also use **Ctrl+C** to interrupt the program safely.

---

⚙️ Configuration

- **Intensity Threshold**: You can change the threshold value at the top of the script:
  ```python
  threshold = 75
  ```
- **Check Frequency**: Modify `time.sleep(3)` to control how often the intensity is checked.

---

📁 File Structure

```
├── light_controller.py  # Main script
├── README.md            # Project overview
```

---

🧩 Possible Extensions

- Connect with a real IoT light device using Raspberry Pi or Arduino.
- Log intensity data over time.
- Add a GUI to visualize changes.

---

📄 License

This project is open-source and free to use under the MIT License.

---

Let me know if you want to add a project logo, setup instructions for Raspberry Pi, or an IoT wiring diagram!
