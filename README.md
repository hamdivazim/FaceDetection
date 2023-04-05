# FaceDetection - cv2 ROI detection
A Python program to detect faces in images.

## Prerequisites
You will need Python and `cv2`.
### Download Python
- Go to [python.org](https://python.org) and download the latest version, remembering to tick 'Add to PATH'.
### Download `cv2`
In the terminal, type:
```
$ pip install opencv-python
```

## How it works
Using trained haarcascades (`haarcascade_frontalfrace_default.xml`, `haarcascade_eye.xml`) you can detect faces and eyes in an image. This is called the ROI (Region of Interest). It will output the result to `Merged.jpg` and will also open a new window with the detected faces.

`live.py` uses your live camera footage and detects faces in the same way. It needs the same trained haarcascades.
