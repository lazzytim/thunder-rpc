import ressource_path
import tkinter as tk
import customtkinter as ctk
import PIL
import os
import sys

app = ctk.CTk()
appVersion = "v1.0"
appTitle = "ThunderRPC Reworked" + f" {appVersion}"

MainColor = "#5865F2"
BgColor = "#1E1E1E"
ButtonColor = "#539B56"
CrtiticalColor = "#7D3131"

ctk.set_appearance_mode("dark")
app.title(appTitle)
app.geometry("800x600")
app.resizable(0, 0)

iconRelativePath = ressource_path.resource_path(r"icon.ico")
app.iconbitmap(iconRelativePath)
 
imgRelativePath = ressource_path.resource_path(r"left_banner.png")
img = tk.PhotoImage(file=imgRelativePath)
ctk.CTkButton(master=app, text="", image=img, border_width=0, fg_color=MainColor, hover_color=MainColor, corner_radius=0).pack(side = ctk.LEFT)

mainFrame = ctk.CTkFrame(master=app, fg_color=BgColor, corner_radius=0, width=400, height=600)
mainFrame.pack()

ctk.CTkLabel(master=mainFrame, text="With ThunderRPC, customize your\nrich presence on Discord and more!", font=('Velvetica', 18), justify='left').place(relx=.10, rely=.1, anchor=ctk.W)
ctk.CTkLabel(master=mainFrame, text="For more information, please go on\nour Github Repository's Wiki", font=('Velvetica', 12), justify='left').place(relx=.10, rely=.18, anchor=ctk.W)
APP_ClientID = ctk.CTkEntry(master=mainFrame, placeholder_text="Client ID", width=200, height=30, corner_radius=5, border_width=0)
APP_Details = ctk.CTkEntry(master=mainFrame, placeholder_text="Details", width=200, height=30, corner_radius=5, border_width=0)
APP_State = ctk.CTkEntry(master=mainFrame, placeholder_text="Description Texte", width=200, height=30, corner_radius=5, border_width=0)
APP_LargeImage = ctk.CTkEntry(master=mainFrame, placeholder_text="Image Name", width=200, height=30, corner_radius=5, border_width=0)
APP_SmallImage = ctk.CTkEntry(master=mainFrame, placeholder_text="Thumbnail Name", width=200, height=30, corner_radius=5, border_width=0)
APP_EpochTimestamp = ctk.CTkEntry(master=mainFrame, placeholder_text="Start Timestamp", width=200, height=30, corner_radius=5, border_width=0)

APP_ClientID.place(relx=.10, rely=.3, anchor=ctk.W)
APP_Details.place(relx=.10, rely=.4, anchor=ctk.W)
APP_State.place(relx=.10, rely=.47, anchor=ctk.W)
APP_LargeImage.place(relx=.10, rely=.54, anchor=ctk.W)
APP_SmallImage.place(relx=.10, rely=.61, anchor=ctk.W)
APP_EpochTimestamp.place(relx=.10, rely=.68, anchor=ctk.W)