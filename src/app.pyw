import window
import pypresence
import tkinter.messagebox as tkm
import time
import sys
import threading
 
def on_close():
    sys.exit(1)

def rpc_Updating():  
    GotClientID = window.APP_ClientID.get()
    rpc = pypresence.Presence(GotClientID)  
    rpc.connect()
    rpc.update(
        state=window.APP_State.get(),
        large_image=window.APP_LargeImage.get(),
        small_image=window.APP_SmallImage.get(),
        start=window.APP_EpochTimestamp.get(),
        details=window.APP_Details.get(),
    )

    tkm.showinfo(title=window.appTitle, message=f"ThunderRPC has sent the rich presence to specified client ID which is [{GotClientID}]")
    
    time.sleep(1)

def RPC_Threading():
    rpc_thread = threading.Thread(target=rpc_Updating)
    rpc_thread.start()

window.app.protocol("WM_DELETE_WINDOW", on_close)
    
window.ctk.CTkButton(
    master=window.mainFrame, 
    text="Apply RichPresence", 
    width=200, 
    height=30,  
    corner_radius=5, 
    font=('Velvetica', 12), 
    fg_color=window.MainColor, 
    hover_color=window.ButtonColor, 
    command=RPC_Threading
    ).place(relx=.10, rely=.8, anchor=window.ctk.W)

window.app.mainloop()
