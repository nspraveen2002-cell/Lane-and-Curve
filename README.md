# 🛣️ Lane and Curve Detection

**Lane and Curve Detection** is a Python-based computer vision project that detects lanes on both **straight and curved roads**, estimates road curvature, and visualizes results with images and video outputs. This repository integrates classic CV techniques such as Hough Transform, perspective transforms, polynomial curve fitting, and thresholding to accurately find lane boundaries in road scenes.

---

## 🚀 Features

✔ Detect **straight lanes** using edge and line detection techniques
✔ Detect **curved lanes** using bird’s-eye perspective and polynomial fitting
✔ Compute **road curvature** for turn prediction
✔ Visualize results on images and video
✔ Includes scripts, example videos, and output images
✔ GUI support for running detection interactively
✔ Jupyter notebook exploration and debugging

---

## 📂 Repository Structure

```
├── Camera_cal_undistorted/         # Camera calibration images
├── Lane-Detection-code/            # Core lane detection code
├── Output-images/                  # Sample output visuals
├── AdvancedLaneFinding.ipynb       # Notebook for advanced methods
├── advanced_lane_find.py           # Python script for advanced detection
├── curved_lane_detection.py        # Script for detecting curved lanes
├── straight_lane_detection.py      # Script for detecting straight lanes
├── main_gui.py                     # Simple GUI interface
├── examples/                       # Example inputs
├── test-cases/                     # Test cases
├── challenge_video.mp4             # Challenge test video
├── project_video.mp4               # Input video
├── project_video_output.mp4        # Output video after detection
└── set_git.sh                      # Shell setup script
```

---

## 🧠 About

This project implements **lane detection and curve estimation** using traditional computer vision approaches. It is useful for understanding lane boundary extraction, road curvature computation, and visualization—foundations often used in autonomous driving perception pipelines.

It does *not* require deep learning, relying instead on algorithms such as:

* Canny edge detection
* Hough line transform
* Perspective warp to bird’s-eye view
* Polynomial curve fitting
* Region of interest masking
* Curvature estimation

Similar lane detection methods are widely used in academic projects and tutorials in autonomous vehicles and perception systems. ([GitHub][1])

---

## 🛠️ Requirements

Make sure you have the following installed:

```
Python 3.6+
OpenCV (cv2)
NumPy
Matplotlib (optional)
tkinter (for GUI)
```

Install dependencies:

```bash
pip install opencv-python numpy matplotlib
```

---

## ▶️ How to Run

### 🔹 Straight Lane Detection

```bash
python straight_lane_detection.py
```

Detects straight lane boundaries in predefined sample videos or images.

### 🔹 Curved Lane Detection

```bash
python curved_lane_detection.py
```

Performs perspective warp, thresholding, and polynomial curve fitting to extract road curvature.

### 🔹 Advanced Solution / GUI

Start the simple GUI:

```bash
python main_gui.py
```

Use the interactive interface to load videos and test case files.

---

## 🎥 Example Results

The repository already includes output demos:

| Video                        | Meaning                    |
| ---------------------------- | -------------------------- |
| `project_video.mp4`          | Input test video           |
| `project_video_output.mp4`   | Lane lines & visualization |
| `challenge_video.mp4`        | Harder road scenarios      |
| `challenge_video_output.mp4` | Output on challenge video  |

Additionally, sample output images in `Output-images/` show detection results.

---

## 📘 Key Scripts

* **straight_lane_detection.py** — Detects straight lane markings using edge detection + Hough.
* **curved_lane_detection.py** — Detects curved lines using perspective transform and polynomial fitting.
* **advanced_lane_find.py** / **AdvancedLaneFinding.ipynb** — Detailed methods and experimentation.
* **main_gui.py** — A simple graphical interface to run detection interactively.

---

## 📊 How It Works (Simplified)

1. **Preprocess Image**
   Convert image to grayscale → blur → edges.

2. **Region of Interest**
   Mask only the road area where lanes appear.

3. **Hough Lines / Warp**

   * For straight roads: Hough Transform identifies strong lines.
   * For curves: Warp image to bird’s-eye view and fit curves via polynomial regression.

4. **Curvature & Turn Prediction**

   * Fit a second-order polynomial to lane pixels.
   * Derive curvature and direction of road (left/right/straight).

---

## 📈 Limitations & Future Work

✔ Works on clear road images with visible lane lines
❌ May struggle with shadows, occlusions, or extreme lighting
❌ Does not use deep learning — heavier real-world variations are not robust
🔹 Future ideas: integrate ML models, improve GUI, support real-time video streams

---

## ❓ Related Projects & Context

Here are some similar open-source lane detection approaches:

* Classic lane detection with polynomial fitting and turn prediction. ([GitHub][1])
* Advanced pipelines with camera calibration, perspective warp, and vehicle position estimation. ([GitHub][2])
* Datasets and benchmarks for curved and multi-lane detection challenges. ([GitHub][3])

These resources provide additional insight into lane detection systems.

---

[2]: https://github.com/OanaGaskey/Advanced-Lane-Detection?utm_source=chatgpt.com "OanaGaskey/Advanced-Lane-Detection"
[3]: https://github.com/SoulmateB/CurveLanes?utm_source=chatgpt.com "CurveLanes is a new benchmark lane detection dataset ..."
