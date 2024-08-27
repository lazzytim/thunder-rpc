import pypresence
import os
import threading

PROMPT = '>>> '

os.system('cls')
os.system('title ThunderRPC CLI v0.0')
print('ThunderRPC ©️ 2024\nCLI Version for Windows, MacOS and Linux\nRequire at least Python 3.12 to work.\n\n')

PRESENCE_TITLE = None
PRESENCE_DESC = None
PRESENCE_IMAGE = None
PRESENCE_THUMBNAIL = None
PRESENCE_EPOCH = None
PRESENCE_BUTTON = None

while True:
    
    ic = input(PROMPT)
    pc = ic.split(' ')
    
    if pc[0] == 'help':
        print()
        print('help ....................... Open this help menu.')
        print('clear ...................... Clear the command prompt.')
        print('idep ....................... Install all python dependencies required for ThunderRPC to work well.')
        print('connect <APP ID> ........... Remotly connect to the specified Discord®️ Application.')
        print('edit <OPTION> <VALUE> ...... Open this help menu.')
        print('update ..................... Update the Discord®️ Rich Presence with the current settings.')
        print('exit ....................... Exit the program and close the connection to the app.')
        print()
        
    elif pc[0] == 'clear':
        os.system('cls')
        os.system('title ThunderRPC CLI v0.0')
        print('ThunderRPC ©️ 2024\nCLI Version for Windows, MacOS and Linux\nRequire at least Python 3.12 to work.\n\n')
        
    elif pc[0] == 'idep':
        os.system('pip install pypresence')
        os.system('pip install customtkinter')
        os.system('pip install pystray')
        os.system('pip install pathlib')
        os.system('pip install pillow')
    
    elif pc[0] == 'connect':
        try:
            PRESENCE = pypresence.Presence(pc[1])
            PRESENCE.connect()
        except Exception as e:
            print('An error happend, please retry or watch the log below.')
            print('\n\n' + e)
        else:
            print()
            print(f'Operation successful!\nApplication under ID {pc[1]} successfully connected.')
            print()
    
    elif pc[0] == 'edit':
        
        if pc[1] == 'title':
            PRESENCE_TITLE = pc[2]
            print()
            print(f'Operation successful!\nOption {pc[1]} changed to value {pc[2]}!')
            print()
        
        elif pc[1] == 'description':
            PRESENCE_DESC = pc[2]
            print()
            print(f'Operation successful!\nOption {pc[1]} changed to value {pc[2]}!')
            print()
            
        elif pc[1] == 'image':
            PRESENCE_IMAGE = pc[2]
            print()
            print(f'Operation successful!\nOption {pc[1]} changed to value {pc[2]}!')
            print()
            
        elif pc[1] == 'thumbnail':
            PRESENCE_THUMBNAIL = pc[2]
            print()
            print(f'Operation successful!\nOption {pc[1]} changed to value {pc[2]}!')
            print()
            
        elif pc[1] == 'epoch':
            PRESENCE_EPOCH = pc[2]
            print()
            print(f'Operation successful!\nOption {pc[1]} changed to value {pc[2]}!')
            print()
            
        elif pc[1] == 'button':
            PRESENCE_BUTTON = pc[2]
            print()
            print(f'Operation successful!\nOption {pc[1]} changed to value {pc[2]}!')
            print()
        
        else:
            print()
            print(f'This is not recongnized as a correct option or value.')
            print()
        
    elif pc[0] == 'update':
        
        def rpc_Update():
            PRESENCE.update(
                state=PRESENCE_TITLE,
                large_image=PRESENCE_IMAGE,
                small_image=PRESENCE_THUMBNAIL,
                start=PRESENCE_EPOCH,
                details=PRESENCE_DESC,
                buttons=PRESENCE_BUTTON
            )
            
        rpc_thread = threading.Thread(target=rpc_Update)
        rpc_thread.start()
    
    elif pc[0] == 'exit':
        exit()