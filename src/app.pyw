import window
import pypresence
import tkinter.messagebox as tkm
import pystray
from pystray import MenuItem as item
import time
import sys
import threading
 
def on_close():
    sys.exit(1)

def rpc_Updating():  
    if window.APP_EpochTimestamp.get() == "":
        epoch = None
    elif window.APP_EpochTimestamp.get() == "$":
        epoch = time.time()
    else:
        epoch = window.APP_EpochTimestamp.get()
        
    if window.APP_State.get() == "":
        state = None
    else:
        state = window.APP_State.get()
        
    if window.APP_Details.get() == "":
        details = None
    else:
        details = window.APP_Details.get()
        
    if window.APP_LargeImage.get() == "":
        limage = None
    else:
        limage = window.APP_LargeImage.get()
        
    if window.APP_SmallImage.get() == "":
        simage = None
    else:
        simage = window.APP_SmallImage.get()
    
    GotClientID = window.APP_ClientID.get()
    rpc = pypresence.Presence(GotClientID)  
    rpc.connect()
    rpc.update(
        state=state,
        large_image=limage,
        small_image=simage,
        start=epoch,
        details=details,
    )

    tkm.showinfo(title=window.appTitle, message=f"ThunderRPC has sent the rich presence to specified client ID which is [{GotClientID}]")
    
    time.sleep(1)

def RPC_Threading():
    rpc_thread = threading.Thread(target=rpc_Updating)
    rpc_thread.start()
    
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

def quit_window(icon, item):
   icon.stop()
   window.app.destroy()
   exit(1)

# Define a function to show the window again
def show_window(icon, item):
   icon.stop()
   window.app.after(0,window.app.deiconify())

# Hide the window and show on the system taskbar
def hide_window():
   window.app.withdraw()
   image=window.Image.open(window.getPath("img\\icon.ico"))
   menu=(item('Show', show_window), item('Exit ThunderRPC', quit_window))
   icon=pystray.Icon("name", image, f"ThunderRPC Reworked {window.appVersion}", menu)
   icon.run()

window.app.protocol('WM_DELETE_WINDOW', hide_window)

window.app.mainloop()
