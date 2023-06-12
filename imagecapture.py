import tkinter as tk
from tkinter import filedialog
import cv2
import os
from PIL import Image, ImageTk

def imageupload():
    def upload_picture():
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            # Display the uploaded image on the GUI
            image = Image.open(file_path)
            image = image.resize((400, 400), Image.ANTIALIAS)

            # Convert the image to RGB mode
            image = image.convert("RGB")

            photo = ImageTk.PhotoImage(image)
            image_label.configure(image=photo)
            image_label.image = photo

            # Save the uploaded image in the "Training_Images" folder
            directory = "Training_images"
            if not os.path.exists(directory):
                os.makedirs(directory)
            file_name = entry.get() + ".jpg"
            image_path = os.path.join(directory, file_name)
            image.save(image_path)


    def take_picture():
        def update_frame():
            # Capture frame from the webcam
            ret, frame = camera.read()

            if ret:
                # Convert the frame to RGB format
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                # Resize the frame and convert it to ImageTk format
                image = cv2.resize(frame, (400, 400))
                image = Image.fromarray(image)
                photo = ImageTk.PhotoImage(image)

                # Update the image label with the new frame
                image_label.configure(image=photo)
                image_label.image = photo

            # Schedule the next frame update
            window.after(1, update_frame)

        # Open the webcam using the DirectShow backend
        camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

        # Start updating the frame
        update_frame()

        def save_image():
            # Capture the current frame from the webcam
            ret, frame = camera.read()

            if ret:
                # Convert the frame to RGB format
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                # Save the captured image in the "Training_Images" folder
                directory = "Training_Images"
                if not os.path.exists(directory):
                    os.makedirs(directory)
                file_name = entry.get() + ".jpg"
                image_path = os.path.join(directory, file_name)

                # Save the image using OpenCV
                cv2.imwrite(image_path, frame)

        # Create a button to save the captured image
        save_button = tk.Button(button_frame, text="Save Image", font=("Arial", 14), command=save_image)
        save_button.pack(side=tk.LEFT, padx=10)

        # Start the Tkinter event loop
        window.mainloop()

        # Release the webcam
        camera.release()

    # Create the main Tkinter window
    window = tk.Tk()
    window.title("Criminal Image Capture")
    window.geometry("500x600")

    # Create a label for the title
    title_label = tk.Label(window, text="Criminal Image Capture", font=("Arial", 20))
    title_label.pack(pady=10)

    # Create a label and entry for the criminal's name
    name_label = tk.Label(window, text="Criminal Name:", font=("Arial", 12))
    name_label.pack(pady=10)
    entry = tk.Entry(window, font=("Arial", 12))
    entry.pack(pady=5)

    # Create a frame to hold the buttons
    button_frame = tk.Frame(window)
    button_frame.pack(pady=20)

    # Create a button to upload a picture
    upload_button = tk.Button(button_frame, text="Upload Picture", font=("Arial", 14), command=upload_picture)
    upload_button.pack(side=tk.LEFT, padx=10)

    # Create a button to take a picture using the webcam
    take_button = tk.Button(button_frame, text="Take Picture", font=("Arial", 14), command=take_picture)
    take_button.pack(side=tk.LEFT, padx=10)

    # Create a label to display the uploaded/taken image
    image_label = tk.Label(window)
    image_label.pack()

    # Start the Tkinter event loop
    window.mainloop()


