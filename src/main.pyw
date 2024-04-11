from win import *
import pypresence
import threading
import tkinter.messagebox as tkm
import pystray
from pystray import MenuItem as item
import time
import sys
 
def on_close():
    sys.exit(1)

def rpc_Update():  
    if INPUT_TIMESTAMP.get() == "":
        epoch = None
    elif INPUT_TIMESTAMP.get() == "$":
        epoch = time.time()
    else:
        epoch = INPUT_TIMESTAMP.get()
        
    if INPUT_STATE.get() == "":
        state = None
    else:
        state = INPUT_STATE.get()
        
    if INPUT_DETAIS.get() == "":
        details = None
    else:
        details = INPUT_DETAIS.get()
        
    if INPUT_IMAGE.get() == "":
        limage = None
    else:
        limage = INPUT_IMAGE.get()
        
    if INPUT_THUMBNAIL.get() == "":
        simage = None
    else:
        simage = INPUT_THUMBNAIL.get()
        
    if CHECK_BUTTON.get() == "True":    
        buttons = [
            {"label": INPUT_BUTTONTEXT.get(), "url": INPUT_BUTTONURL.get()}
        ]
    else:
        buttons = None
  
    try:
        GotClientID = INPUT_CLIENT.get()
        rpc = pypresence.Presence(GotClientID)  
        rpc.connect()
    except Exception as e:
        tkm.showerror(title=APP_BARTEXT, message=e)
        
    rpc.update(
        state=state,
        large_image=limage,
        small_image=simage,
        start=epoch,
        details=details,
        buttons=buttons,
    )

    tkm.showinfo(title=APP_BARTEXT, message=f"ThunderRPC has sent the rich presence to specified client ID which is [{GotClientID}]")

def RPC_Threading():
    rpc_thread = threading.Thread(target=rpc_Update)
    rpc_thread.start()
    
BUTTON_Submit_IMAGE = getPath("icons\\send.png")
BUTTON_Submit_IMAGE_LOADED = tk.PhotoImage(file=BUTTON_Submit_IMAGE)
BUTTON_Submit = ctk.CTkButton(stgs_tab, text="", fg_color="#0D1117", hover_color="#30363D", image=BUTTON_Submit_IMAGE_LOADED, width=125, command=RPC_Threading, corner_radius=8, border_width=1, border_color="#30363D")
BUTTON_Submit.place(relx=0.10, rely=0.9, anchor=ctk.NW)

def quit_window(icon, item):
    icon.stop()
    root.destroy()
    exit(1)

# Define a function to show the window again
def show_window(icon, item):
    icon.stop()
    root.after(0,root.deiconify())

# Hide the window and show on the system taskbar
def hide_window():
    root.withdraw()
    image=Image.open(getPath("imgs\\icon.ico"))
    menu=(item('Show', show_window), item('Exit ThunderRPC', quit_window))
    icon=pystray.Icon("name", image, APP_BARTEXT, menu)
    icon.run()

root.protocol('WM_DELETE_WINDOW', hide_window)

root.mainloop()