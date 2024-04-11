import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
import os
import sys
import pathlib

APP_TITLE = "ThunderRPC Reworked"
APP_VER = "v2.0"
APP_BARTEXT = f"{APP_TITLE} {APP_VER}"

def getPath(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = pathlib.Path(__file__).parent
    return os.path.join(base_path, relative_path)

root = ctk.CTk(fg_color="#0D1117")
root.title(APP_BARTEXT)
root.geometry("1000x600")
root.resizable(0, 0)
root.iconbitmap(getPath("imgs\\icon.ico"))

lb = getPath("imgs\\left_banner.png")
lbi = tk.PhotoImage(file=lb)
ctk.CTkButton(root, text="", image=lbi, corner_radius=0, fg_color="#5865F2", hover_color="#5865F2").place(relx=0, rely=0, anchor=ctk.NW)

tabview = ctk.CTkTabview(root, anchor="W", width=560, height=585, corner_radius=8, fg_color="#0D1117", border_width=1, border_color="#30363D", segmented_button_fg_color="#0D1117", segmented_button_selected_hover_color="#30363D", segmented_button_unselected_hover_color="#30363D", segmented_button_selected_color="#30363D", segmented_button_unselected_color="#0D1117")
tabview.place(relx=0.425, rely=0, anchor=ctk.NW)

stgs_tab = tabview.add("Assets")
btns_tab = tabview.add("Buttons")
tstp_tab = tabview.add("Timestamps")
crdt_tab = tabview.add("Credits")

# \\\\\\\\\ ASSETS TAB ///////// #

ctk.CTkLabel(stgs_tab, text="ThunderRPC is a portable software made\nin Python using PyPresence Lib. that allow\nyou to send RichPresence using a Client ID", font=("Helvetica", 20, "bold"), justify="left").place(relx=0.10, rely=0.10, anchor=ctk.NW)

INPUT_CLIENT = ctk.CTkEntry(stgs_tab, width=200, height=32, corner_radius=8, fg_color="#0D1117", border_width=1, border_color="#30363D", placeholder_text=" Client ID")
INPUT_CLIENT.place(relx=0.149, rely=0.3, anchor=ctk.NW)
BUTTON_CLIENT_IMAGE = getPath("icons\\id.png")
BUTTON_CLIENT_IMAGE_LOADED = tk.PhotoImage(file=BUTTON_CLIENT_IMAGE)
BUTTON_CLIENT = ctk.CTkButton(stgs_tab, text="", fg_color="#0D1117", hover_color="#0D1117", width=24, height=24, image=BUTTON_CLIENT_IMAGE_LOADED, corner_radius=0, border_width=1, border_color="#30363D")
BUTTON_CLIENT.place(relx=0.10, rely=0.3, anchor=ctk.NW)

INPUT_DETAIS = ctk.CTkEntry(stgs_tab, width=200, height=32, corner_radius=8, fg_color="#0D1117", border_width=1, border_color="#30363D", placeholder_text=" Details Text")
INPUT_DETAIS.place(relx=0.149, rely=0.4, anchor=ctk.NW)
BUTTON_DETAIS_IMAGE = getPath("icons\\title.png")
BUTTON_DETAIS_IMAGE_LOADED = tk.PhotoImage(file=BUTTON_DETAIS_IMAGE)
BUTTON_DETAIS = ctk.CTkButton(stgs_tab, text="", fg_color="#0D1117", hover_color="#0D1117", width=24, height=24, image=BUTTON_DETAIS_IMAGE_LOADED, corner_radius=0, border_width=1, border_color="#30363D")
BUTTON_DETAIS.place(relx=0.10, rely=0.4, anchor=ctk.NW)

INPUT_STATE = ctk.CTkEntry(stgs_tab, width=200, height=32, corner_radius=8, fg_color="#0D1117", border_width=1, border_color="#30363D", placeholder_text=" Statement Text")
INPUT_STATE.place(relx=0.149, rely=0.48, anchor=ctk.NW)
BUTTON_STATE_IMAGE = getPath("icons\\desc.png")
BUTTON_STATE_IMAGE_LOADED = tk.PhotoImage(file=BUTTON_STATE_IMAGE)
BUTTON_STATE = ctk.CTkButton(stgs_tab, text="", fg_color="#0D1117", hover_color="#0D1117", width=24, height=24, image=BUTTON_STATE_IMAGE_LOADED, corner_radius=0, border_width=1, border_color="#30363D")
BUTTON_STATE.place(relx=0.10, rely=0.48, anchor=ctk.NW)

INPUT_IMAGE = ctk.CTkEntry(stgs_tab, width=200, height=32, corner_radius=8, fg_color="#0D1117", border_width=1, border_color="#30363D", placeholder_text=" Image Asset Name")
INPUT_IMAGE.place(relx=0.149, rely=0.56, anchor=ctk.NW)
BUTTON_IMAGE_IMAGE = getPath("icons\\image.png")
BUTTON_IMAGE_IMAGE_LOADED = tk.PhotoImage(file=BUTTON_IMAGE_IMAGE)
BUTTON_IMAGE = ctk.CTkButton(stgs_tab, text="", fg_color="#0D1117", hover_color="#0D1117", width=24, height=24, image=BUTTON_IMAGE_IMAGE_LOADED, corner_radius=0, border_width=1, border_color="#30363D")
BUTTON_IMAGE.place(relx=0.10, rely=0.56, anchor=ctk.NW)

INPUT_THUMBNAIL = ctk.CTkEntry(stgs_tab, width=200, height=32, corner_radius=8, fg_color="#0D1117", border_width=1, border_color="#30363D", placeholder_text=" Thumbnail Asset Name")
INPUT_THUMBNAIL.place(relx=0.149, rely=0.64, anchor=ctk.NW)
BUTTON_THUMBNAIL_IMAGE = getPath("icons\\thumbnail.png")
BUTTON_THUMBNAIL_IMAGE_LOADED = tk.PhotoImage(file=BUTTON_THUMBNAIL_IMAGE)
BUTTON_THUMBNAIL = ctk.CTkButton(stgs_tab, text="", fg_color="#0D1117", hover_color="#0D1117", width=24, height=24, image=BUTTON_THUMBNAIL_IMAGE_LOADED, corner_radius=0, border_width=1, border_color="#30363D")
BUTTON_THUMBNAIL.place(relx=0.10, rely=0.64, anchor=ctk.NW)

# \\\\\\\\\ BUTTONS TAB ///////// #

ctk.CTkLabel(btns_tab, text="ThunderRPC is a portable software made\nin Python using PyPresence Lib. that allow\nyou to send RichPresence using a Client ID", font=("Helvetica", 20, "bold"), justify="left").place(relx=0.10, rely=0.10, anchor=ctk.NW)

CHECK_BUTTON_VALUE = ctk.StringVar(value="False")
CHECK_BUTTON = ctk.CTkCheckBox(btns_tab, text="Enable buttons?", border_width=1, border_color="#30363D", fg_color="#30363D", hover_color="#30363D", variable=CHECK_BUTTON_VALUE, onvalue="True", offvalue="False")
CHECK_BUTTON.place(relx=0.10, rely=0.3, anchor=ctk.NW)

INPUT_BUTTONTEXT = ctk.CTkEntry(btns_tab, width=200, height=32, corner_radius=8, fg_color="#0D1117", border_width=1, border_color="#30363D", placeholder_text=" Button Text")
INPUT_BUTTONTEXT.place(relx=0.149, rely=0.38, anchor=ctk.NW)
BUTTON_BUTTONTEXT_IMAGE = getPath("icons\\title.png")
BUTTON_BUTTONTEXT_IMAGE_LOADED = tk.PhotoImage(file=BUTTON_BUTTONTEXT_IMAGE)
BUTTON_BUTTONTEXT = ctk.CTkButton(btns_tab, text="", fg_color="#0D1117", hover_color="#0D1117", width=24, height=24, image=BUTTON_BUTTONTEXT_IMAGE_LOADED, corner_radius=0, border_width=1, border_color="#30363D")
BUTTON_BUTTONTEXT.place(relx=0.10, rely=0.38, anchor=ctk.NW)

INPUT_BUTTONURL = ctk.CTkEntry(btns_tab, width=200, height=32, corner_radius=8, fg_color="#0D1117", border_width=1, border_color="#30363D", placeholder_text=" Button URL")
INPUT_BUTTONURL.place(relx=0.149, rely=0.46, anchor=ctk.NW)
BUTTON_BUTTONURL_IMAGE = getPath("icons\\link.png")
BUTTON_BUTTONURL_IMAGE_LOADED = tk.PhotoImage(file=BUTTON_BUTTONURL_IMAGE)
BUTTON_BUTTONURL = ctk.CTkButton(btns_tab, text="", fg_color="#0D1117", hover_color="#0D1117", width=24, height=24, image=BUTTON_BUTTONURL_IMAGE_LOADED, corner_radius=0, border_width=1, border_color="#30363D")
BUTTON_BUTTONURL.place(relx=0.10, rely=0.46, anchor=ctk.NW)

# \\\\\\\\\ TIMESTAMP TAB ///////// #

ctk.CTkLabel(tstp_tab, text="ThunderRPC is a portable software made\nin Python using PyPresence Lib. that allow\nyou to send RichPresence using a Client ID", font=("Helvetica", 20, "bold"), justify="left").place(relx=0.10, rely=0.10, anchor=ctk.NW)

INPUT_TIMESTAMP = ctk.CTkEntry(tstp_tab, width=200, height=32, corner_radius=8, fg_color="#0D1117", border_width=1, border_color="#30363D", placeholder_text=" Timestamp Value*")
INPUT_TIMESTAMP.place(relx=0.149, rely=0.3, anchor=ctk.NW)
BUTTON_TIMESTAMP_IMAGE = getPath("icons\\timestamp.png")
BUTTON_TIMESTAMP_IMAGE_LOADED = tk.PhotoImage(file=BUTTON_TIMESTAMP_IMAGE)
BUTTON_TIMESTAMP = ctk.CTkButton(tstp_tab, text="", fg_color="#0D1117", hover_color="#0D1117", width=24, height=24, image=BUTTON_TIMESTAMP_IMAGE_LOADED, corner_radius=0, border_width=1, border_color="#30363D")
BUTTON_TIMESTAMP.place(relx=0.10, rely=0.3, anchor=ctk.NW)

ctk.CTkLabel(tstp_tab, text_color="#30363D", text="To automaticaly set the timestamp value\nto now, write a dollars sign like this '$'.", font=("Helvetica", 10, "bold"), justify="left").place(relx=0.10, rely=0.38, anchor=ctk.NW)

# \\\\\\\\\ CREDITS TAB ///////// #

ctk.CTkLabel(crdt_tab, text="Made by @lazzytim on Github", font=("Helvetica", 16, "bold"), justify="left").place(relx=0.10, rely=0.10, anchor=ctk.NW)

ctk.CTkLabel(crdt_tab, text="Find full source code and portable software on Github\nat https://github.com/lazzytim/thunder-rpc", font=("Helvetica", 14, "bold"), justify="left").place(relx=0.10, rely=0.18, anchor=ctk.NW)
