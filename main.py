import imageio
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

canvas = tk.Tk()
canvas.geometry("400x300")
canvas.title("GIF Converter")
canvas.iconbitmap('images/icon.ico')
canvas.configure(bg='gray')

canvas.filename = ""


def gif_maker(input_path, target_format):
    if input_path == "":
        return
    output_path = os.path.splitext(input_path)[0] + target_format
    reader = imageio.get_reader(input_path)
    fps = reader.get_meta_data()['fps']
    writer = imageio.get_writer(output_path, fps=fps)

    for frames in reader:
        writer.append_data(frames)

    writer.close()
    messagebox.showinfo("Information", "File Conversion Successful! Output placed in Source folder")


def open_directory():
    canvas.filename = filedialog.askopenfilename(initialdir="C:/Users/Infinity/Documents", title="Select A File",
                                                 filetypes=(("MP4 Files", "*.mp4"), ("all files", "*.*")))
    gif_maker(canvas.filename, '.gif')


browse_button = tk.Button(canvas, text="Browse File", command=open_directory, font=("SAN_SERIF", 20, "bold"))
browse_button.pack(pady=100)

canvas.mainloop()
