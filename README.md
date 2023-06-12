# Criminal Image Recognition 

![image](https://github.com/hope404alive/Crime-Detection/assets/94454699/e3672a98-4f27-48b7-bca9-60bf71b775aa)






Criminal Image Recognition is a Python-based application that performs facial recognition on criminal images. It allows you to create a criminal database, upload new images, and identify known criminals in real-time using a webcam.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [1. Open Database](#1-open-database)
  - [2. Upload Image](#2-upload-image)
  - [3. Face Recognition](#3-face-recognition)
  - [4. Database Entry](#4-database-entry)
- [Contributing](#contributing)


## Installation

1. Clone the repository to your local machine:
   ```
   git clone [https://github.com/your-username/criminal-image-recognition.git](https://github.com/hope404alive/Crime-Detection.git)
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

The application provides feature for** **Criminal Information Extraction** through Face Detection**

![image](https://github.com/hope404alive/Crime-Detection/assets/94454699/4598401c-916c-400d-98c8-3578f0b1167f)


### 1. Open Database

 It allows you to open the criminal database stored in the "Book1.csv" file. This file contains information about known criminals, including their names and corresponding face encodings. Clicking the "Open Database" button will open the database in a separate window, allowing you to view and modify the criminal records if needed.

### 2. Upload Image

The "Create Face Entry" functionality enables you to  either upload a picture or capture the face of a criminal from the application. Follow these steps to upload an image:

### 3. Face Recognition

The "Search" functionality utilizes the webcam to perform real-time facial recognition and identify known criminals from the uploaded images. Follow these steps to perform face recognition:

1. Click the "Search" button.
2. The application will activate your webcam and start capturing frames.
3. Detected faces will be compared with the face encodings of known criminals from the database.
4. If a match is found, the application will display the criminal's name and draw a rectangle around their face in the live video feed.
5. The Criminal Information from the database would be fetched


### 4. Database Entry
The "Create Database Entry" button opens a GUI form where you can enter the details of a criminal, including their name, contact information, Aadhaar card details, and the crime committed. The entered information is saved in the database for future reference.

![image](https://github.com/hope404alive/Crime-Detection/assets/94454699/4db43182-8534-4496-a754-9b633c43a107)




## Contributing

Contributions to this project are welcome. If you encounter any issues or have suggestions for improvements, please create an issue or submit a pull request.



