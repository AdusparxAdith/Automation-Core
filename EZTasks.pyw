from tkinter import *
from tkinter import ttk,Frame,Entry,Tk
from subprocess import call
import pyautogui as pg

root = Tk()


mainFrame = ttk.Frame(root)
mainFrame.pack()
mainFrame.config(relief = GROOVE,borderwidth=50)

Widget_Label = ttk.Label(mainFrame, text="SCRIPTS")
Widget_Label.pack()

script1 = ttk.Button(mainFrame,text = "Extend Display",command = lambda:call(["python", "E:/CreationSQUARE/Personal Projects/Automation-Core/Scripts/ExtendDisplay.py"])) #EXTENDS DISPLAY
script1.pack(pady=10)
script2 = ttk.Button(mainFrame,text = "Single Display",command = lambda:call(["python", "E:/CreationSQUARE/Personal Projects/Automation-Core/Scripts/ShowOne.py"]))     #SINGLES DISPLAY
script2.pack(pady=10)
script3 = ttk.Button(mainFrame,text = "Setup Workspace One",command = lambda:call(["python", "E:/CreationSQUARE/Personal Projects/Automation-Core/Scripts/Workspace.py"]))  #READYS WORKSPACE
script3.pack(pady=10)
script3 = ttk.Button(mainFrame,text = "Setup Workspace Two",command = lambda:call(["python", "E:/CreationSQUARE/Personal Projects/Automation-Core/Scripts/Workspace2.py"]))  #READYS WORKSPACE
script3.pack(pady=10)
script4 = ttk.Button(mainFrame,text = "Play Playlist",command = lambda:call(["python", "E:/CreationSQUARE/Personal Projects/Automation-Core/Scripts/Playlist.py"])) #READYS YOUTUBE PLAYLIST
script4.pack(pady=10)
script3 = ttk.Button(mainFrame,text = "Play Dota",command = lambda:call(["python", "E:/CreationSQUARE/Personal Projects/Automation-Core/Scripts/Dota.py"]))
script3.pack(pady=10)
script6 = ttk.Button(mainFrame,text = "Quit", command= lambda: pg.hotkey('alt','f4'))
script6.pack(pady=10)



root.mainloop()
