from app_window import *
from pypresence import Presence
import tkinter.messagebox as tkm
from time import *
from threading import *

#######################
##     Main Code     ##
#######################

def RPC_Updating():
    NewClientID = APP_ClientID.get()
    RPC = Presence(NewClientID)
    RPC.connect()
    RPC.update(
        state=APP_State.get(),
        large_image=APP_LargeImage.get(),
        small_image=APP_SmallImage.get(),
        start=APP_EpochTimestamp.get(),
        details=APP_Details.get(),
    )

    tkm.askokcancel(title='ThunderRPC', message=f'Successfully sent your rich presence to ID: "{APP_ClientID.get()}" !')
    
    while True:
        sleep(3)

def RPC_Threading():
    rpc_thread = Thread(target=RPC_Updating)
    rpc_thread.start()
    

CTkButton(master=mainFrame, text="Apply RichPresence", width=200, height=30, corner_radius=5, font=('Velvetica', 12), fg_color=MainColor, hover_color=ButtonColor, command=RPC_Threading).place(relx=.10, rely=.8, anchor=W)


###########################
##   Windows Main Loop   ##
###########################

app.mainloop()
