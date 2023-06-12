from tkinter import *
import csv
import os
from PIL import ImageTk, Image
def image():
    
    def btn_clicked():
        name = entry0.get()
        contact_no = entry1.get()
        addhar_card = entry2.get()
        criminal_activities = entry3.get()

        # Open the CSV file in append mode
        with open('Book1.csv', 'a', newline='') as file:
            writer = csv.writer(file)

            # Check if the file is empty and write the headers if necessary
            if file.tell() == 0:
                writer.writerow(['index', 'criminal_name', 'Phone no', 'Adhaar', 'Criminal Activities'])

            # Get the current number of rows in the CSV file
            with open('Book1.csv', 'r') as csvfile:
                row_count = sum(1 for row in csvfile)

            # Write the data to the CSV file with an incremented index value
            writer.writerow([row_count - 1, name, contact_no, addhar_card, criminal_activities])

        print("Data saved to CSV file")

    window = Tk()

    window.geometry("839x494")
    window.configure(bg="#ffffff")
    canvas = Canvas(
        window,
        bg="#ffffff",
        height=494,
        width=839,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=9, y=5)

    # Load background image from the build folder
    background_img_path = os.path.join("build", "background.png")
    background_img = ImageTk.PhotoImage(Image.open(background_img_path))
    background = canvas.create_image(419, 247, image=background_img)


    entry0_bg = canvas.create_image(430, 150)

    entry0 = Entry(
        bd=0,
        bg="#d9d9d9",
        highlightthickness=0
    )
    entry0.place(x=430, y=150, width=391, height=40)


    entry1_bg = canvas.create_image(430, 220)

    entry1 = Entry(
        bd=0,
        bg="#d9d9d9",
        highlightthickness=0
    )
    entry1.place(x=430, y=230, width=391, height=40)


    entry2_bg = canvas.create_image(130, 360)

    entry2 = Entry(
        bd=0,
        bg="#d9d9d9",
        highlightthickness=0
    )
    entry2.place(x=430, y=310, width=391, height=40)

    entry3_bg = canvas.create_image(430, 350)

    entry3 = Entry(
        bd=0,
        bg="#d9d9d9",
        highlightthickness=0
    )
    entry3.place(x=430, y=400, width=391, height=40)

    img0 = PhotoImage(file="build/img0.png")
    b0 = Button(
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        command=btn_clicked,
        relief="flat"
    )
    b0.place(x=430, y=450, width=183, height=62)


    window.resizable(True, True)
    window.mainloop()
image()
