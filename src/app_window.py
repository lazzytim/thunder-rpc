from tkinter import *
from tkinter import ttk
from customtkinter import *
from PIL import Image, ImageTk

###########################
##     Window Config     ##
###########################

app = CTk()
appVersion = "v1.0"

MainColor = "#5865F2"
BgColor = "#1E1E1E"
ButtonColor = "#539B56"
CrtiticalColor = "#7D3131"

set_appearance_mode("dark")
app.title("ThunderRPC Reworked" + f" {appVersion}")
app.geometry("800x600")
app.resizable(0, 0)

##########################
##      Window Code     ##
##########################

img = PhotoImage(file="C:\\Users\delet\Desktop\ThunderRPC Reworked\src\left_banner.png")
CTkButton(master=app, text="", image=img, border_width=0, fg_color=MainColor, hover_color=MainColor, corner_radius=0).pack(side = LEFT)

mainFrame = CTkFrame(master=app, fg_color=BgColor, corner_radius=0, width=400, height=600)
mainFrame.pack()

CTkLabel(master=mainFrame, text="With ThunderRPC, customize your\nrich presence on Discord and more!", font=('Velvetica', 18), justify='left').place(relx=.10, rely=.1, anchor=W)
CTkLabel(master=mainFrame, text="For more information, please go on\nour Github Repository's Wiki", font=('Velvetica', 12), justify='left').place(relx=.10, rely=.18, anchor=W)
APP_ClientID = CTkEntry(master=mainFrame, placeholder_text="Client ID", width=200, height=30, corner_radius=5, border_width=0)
APP_Details = CTkEntry(master=mainFrame, placeholder_text="Details", width=200, height=30, corner_radius=5, border_width=0)
APP_State = CTkEntry(master=mainFrame, placeholder_text="Description Texte", width=200, height=30, corner_radius=5, border_width=0)
APP_LargeImage = CTkEntry(master=mainFrame, placeholder_text="Image Name", width=200, height=30, corner_radius=5, border_width=0)
APP_SmallImage = CTkEntry(master=mainFrame, placeholder_text="Thumbnail Name", width=200, height=30, corner_radius=5, border_width=0)
APP_EpochTimestamp = CTkEntry(master=mainFrame, placeholder_text="Start Timestamp", width=200, height=30, corner_radius=5, border_width=0)


APP_ClientID.place(relx=.10, rely=.3, anchor=W)
APP_Details.place(relx=.10, rely=.4, anchor=W)
APP_State.place(relx=.10, rely=.47, anchor=W)
APP_LargeImage.place(relx=.10, rely=.54, anchor=W)
APP_SmallImage.place(relx=.10, rely=.61, anchor=W)
APP_EpochTimestamp.place(relx=.10, rely=.68, anchor=W)