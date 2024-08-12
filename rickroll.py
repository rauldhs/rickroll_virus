"""
Cool python script to spam rickroll gif windows
"""
 
from tkinter import Toplevel, Label, Tk
from io import BytesIO
import random
import sys
import os
import requests
from PIL import Image, ImageTk, ImageSequence


def create_window(root, gif_frames):
    """Function to create and run a window with rickroll GIF animation"""
    window = Toplevel(root)
    window.attributes('-topmost', 1)
    window.overrideredirect(1)
    window.wm_attributes('-transparentcolor', 'white')

    x = random.randint(0, root.winfo_screenwidth() - gif_frames[0].width())
    y = random.randint(0, root.winfo_screenheight() - gif_frames[0].height())

    window.geometry(f"+{x}+{y}")

    label = Label(window, bg='white')
    label.pack()

    # TODO: check why tf updating the position slows down the calls for create window by half :/
    # update_window_position(window,label,x,y,gif_frames[0].width(),gif_frames[0].height())
    update_frame(0, label, gif_frames)

# TODO: fix this shit


def update_window_position(window, label, x, y):
    """Update the window's position with a random velocity"""
    x_velocity = random.randint(-10, 10)
    y_velocity = random.randint(-10, 10)

    screen_width, screen_height = window.winfo_screenwidth(), window.winfo_screenheight()
    window_w, window_h = window.winfo_width(), window.winfo_height()

    x = max(0, min(x + x_velocity, screen_width - window_w))
    y = max(0, min(y + y_velocity, screen_height - window_h))

    window.geometry(f"+{x}+{y}")

    label.after(100, update_window_position, window,
                label, x, y, window_w, window_h)


def update_frame(i, label, frames):
    """Loads next frame of the gif to the window"""
    frame = frames[i]
    i += 1
    if i >= len(frames):
        i = 0
    label.configure(image=frame)
    label.image = frame
    label.after(100, update_frame, i, label, frames)


def load_gif(gif_url, gif_file_name='rickroll.gif'):
    """
    Tries to load the gif image either from a local file or from a URL if the file is not 
    found locally. I know there could be more exception handling, but I prefer not to 
    write spaghetti code.
    """

    try:
        gif = Image.open(gif_file_name)
    except FileNotFoundError:
        response = requests.get(gif_url, timeout=1000)
        response.raise_for_status()
        gif = Image.open(BytesIO(response.content))

    return gif


def main():
    """Spams rickroll gif windows through create_window()"""

    root = Tk()
    root.withdraw()

    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(__file__)

    gif_path = os.path.join(base_path, 'rickroll.gif')

    gif = load_gif(
        "https://media.tenor.com/q0Ejci9EQhcAAAAj/rick-astley-rick-roll.gif", gif_path)

    gif_frames = [ImageTk.PhotoImage(frame.copy().convert(
        'RGBA')) for frame in ImageSequence.Iterator(gif)]

    def create_windows_periodically():
        create_window(root, gif_frames)
        root.after(10, create_windows_periodically)

    create_windows_periodically()
    root.mainloop()


if __name__ == "__main__":
    main()
