# Criminal Image Recognition 

![image](https://github.com/hope404alive/Crime-Detection/assets/94454699/e3672a98-4f27-48b7-bca9-60bf71b775aa)






Criminal Image Recognition is a Python-based application that performs facial recognition on criminal images. It allows you to create a criminal database, upload new images, and identify known criminals in real-time using a webcam.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [1. Open Database](#1-open-database)
  - [2. Upload Image](#2-upload-image)
  - [3. Face Recognition](#3-face-recognition)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Installation

1. Clone the repository to your local machine:
   ```
   git clone https://github.com/your-username/criminal-image-recognition.git
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

The application provides feature for Criminal Infromation Extraction through Face Detection.

### 1. Open Database

The "Open Database" functionality allows you to open the criminal database stored in the "Book1.csv" file. This file contains information about known criminals, including their names and corresponding face encodings. Clicking the "Open Database" button will open the database in a separate window, allowing you to view and modify the criminal records if needed.

### 2. Upload Image

The "Upload Image" functionality enables you to upload a picture of a criminal to the application. Follow these steps to upload an image:

1. Click the "Upload Image" button.
2. Select an image file (in PNG, JPG, or JPEG format) from your local system using the file dialog.
3. Enter the criminal's name in the provided text field.
4. The uploaded image will be displayed on the GUI, and the application will save it in the "Training_images" folder for further processing.

### 3. Face Recognition

The "Face Recognition" functionality utilizes the webcam to perform real-time facial recognition and identify known criminals from the uploaded images. Follow these steps to perform face recognition:

1. Click the "Face Recognition" button.
2. The application will activate your webcam and start capturing frames.
3. Detected faces will be compared with the face encodings of known criminals from the database.
4. If a match is found, the application will display the criminal's name and draw a rectangle around their face in the live video feed.

## Contributing

Contributions to this project are welcome. If you encounter any issues or have suggestions for improvements, please create an issue or submit a pull request.


## Acknowledgments

This project was built using the following libraries and resources:

- OpenCV: https://opencv.org/
- face_recognition: https://github.com/ageitgey/face_recognition


