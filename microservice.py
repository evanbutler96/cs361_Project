# using tkinter to open the file explorer and upload the image path file names
import tkinter as tk
from tkinter import filedialog
import time

# we import Image from PIL to save the selected images to the new images directory.
from PIL import Image

# use os for handling the directories and making new images directory
import os
if __name__ == '__main__':

    while True:
# def photoupload():
    # here we read the text file to see if the request was sent
    # you will ofc need to changed this path for the text file
        path = "C:\\Users\\arest\\OneDrive\\Desktop\\School\\spring_2022\\cs361\\MVP\\cs361_Project\\ms.txt"

        f = open(path, "r+")
        line = f.read()

        # we then start the program if the request was sent
        if line == "request":

            # since we are not writing to the text file we can truncate and close the file immediately
            # This is because we are making a new directory
            f.truncate(0)
            f.close()

            # ROOT_DIR is the parent directory of all the child directories, this will come in handy when making the ->
            # -> images directory for the uploaded photos
            ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

            print(ROOT_DIR)
            # here we declare target, which is just appending 'images' to the end of the root directory path
            target = os.path.join(ROOT_DIR, 'images')

            # if the new directory images does not already exist, we will make the new directory images
            if not os.path.isdir(target):
                os.mkdir(target)

            # we use tkinter to obtain the image paths
            newwin = tk.Tk()
            newwin.withdraw()

            # here the variable files is assigned the selected file/image names
            files = filedialog.askopenfilenames(initialdir=ROOT_DIR, title="Upload Images",
                                                filetypes=[("JPEG", "*.jpg")])

            os.chdir(target)

            # we declare the image count, the image_count numbers will be the names/indices of the .jpg files.
            # we need to make sure we don't override existing photos with the same name in the images directory
            list = os.listdir(target)
            Image_number = len(list)
            if Image_number != 0:
                image_count = Image_number + 1
            else:
                image_count = 0

            # here we utilize the PIL imports to be able to select and save multiple photos to the images directory
            for file in files:
                image_count += 1
                im = Image.open(file)
                im = im.save(f"{image_count}.jpg")

            os.chdir(ROOT_DIR)

            line = ""
        # this is if the request was misspelled or not inputted into the text file
        else:
            time.sleep(2)
