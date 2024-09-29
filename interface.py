import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from ttkbootstrap import Style
from PIL import ImageFont
import main 

# Folder select menu
def select_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        folder_path.set(folder_selected)

# Warning and finished messages
def download():
    url = url_entry.get()
    dest = folder_path.get()

    if not url:
        messagebox.showwarning("Warning", "Please enter the video URL")
        return
    
    if not dest:
        messagebox.showwarning("Warning", "Please select the destination folder")
        return

    # Message shown when download is finished
    result = main.download_audio(url, dest)
    messagebox.showinfo("Result", result)

# UI declaration
root = tk.Tk()
root.title("YT DLD")
root.geometry("700x200")
root.config(bg="#636363")

custom_font = ImageFont.truetype("./resources/fonts/monocraft/Monocraft.ttf", 12)

# App theme
style = Style(theme="vapor")
style.configure(".", font="Monocraft")

# Folder selection variable
folder_path = tk.StringVar()

# URL text
url_label = ttk.Label(root, text="Video URL:")
url_label.grid(row=0, column=0, padx=10, pady=10, sticky="")

# URL input
url_entry = ttk.Entry(root, width=40, font="Monocraft", foreground="#32fbe2")
url_entry.grid(row=0, column=1, sticky="swe", padx=10, pady=10)

# Folder selection button
folder_button = ttk.Button(root, text="Select folder", command=select_folder)
folder_button.grid(row=1, column=0, padx=10, pady=10)

# Folder path display
folder_display = ttk.Label(root, textvariable=folder_path, background="#30115e", justify="center", width=40)
folder_display.grid(row=1, column=1, padx=10, pady=10)

# Start download button
download_button = ttk.Button(root, text="Download audio", command=download)
download_button.grid(row=2, column=0, columnspan=2, pady=20)

root.mainloop()

if __name__ == "__main__":
    try:
        main.install_reqs()
        main()
    except Exception as e:
        print(f"An error ocurred: {e}")