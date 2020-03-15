from classtest import classTest
from eventMaker import eventListener
from controller import eventReplayer
import os
import sys
from tkinter import Tk, Listbox, SINGLE, END, Button, Label, W, E, N, S, StringVar, Entry

class MyFirstGUI:
    def __init__(self, master):
        filename = 'events'
        dirPath = os.path.dirname(os.path.realpath(__file__)) 
        recordPath = dirPath + "/" + filename
        self.name = StringVar()
        self.errorText = StringVar()

        if sys.platform.startswith('win'):
            recordPath = dirPath + "\\" + filename
        if not os.path.exists(recordPath):
            try:
                os.mkdir(recordPath)
            except OSError:
                print ("Failed to create folder to store recordings.")
                sys.exit()


        self.master = master
        master.title("A simple GUI")
        self.label = Label(master, text="Python automation helper!")
        self.flist = os.listdir('./events')

        def play():
            selected = self.lb.curselection()
            if selected:
                filename = "./events/" + self.flist[selected[0]]
                eventReplayer(filename)

        def Record():
            selected = self.lb.curselection()
            eventListener(self.flist[selected[0]])
            self.errorText.set("Recording saved.")

        def addFile():
            fileToAdd = self.name.get() + '.txt'
            open("./events/" + fileToAdd, 'a').close()

            self.flist.append(fileToAdd)
            self.lb.delete(0, END) # clear
            self.flist = os.listdir('./events')
            for n in self.flist: self.lb.insert(END, n)
            self.errorText.set("Successfully created file.")


        def deleteFile():
            selected = self.lb.curselection()
            if selected:
                filename = self.flist[selected[0]]
                os.remove("./events/" + filename)
                self.lb.delete(0, END) # clear
                self.flist.remove(filename)
                for n in self.flist: self.lb.insert(END, n)
                self.errorText.set("Successfully deleted file.")

        self.lb = Listbox(root, selectmode=SINGLE)
        for n in self.flist: self.lb.insert(END, n) # put files in listbox

        # Create the elements of the GUI
        self.File_Entry = Entry(root, textvariable = self.name)
        self.play_button = Button(root, text='Play selected', command=play)
        self.record_button = Button(root, text='Record', command=Record)
        self.add_file_button = Button(root, text='Add file', command=addFile)
        self.delete_button = Button(root, text='Delete file', command=deleteFile)
        self.label = Label(master, text="Python automation helper!")
        self.error = Label(master, textvariable=self.errorText)

        # Create the layout
        self.label.grid(row=0, column=0)
        self.record_button.grid(row=1, column=1)
        self.play_button.grid(row=2, column=1, padx=5)
        self.lb.grid(row=1, column=0, rowspan=7)
        self.File_Entry.grid(row=8, column=0, pady=5)
        self.add_file_button.grid(row=8, column=1, pady=5)
        self.delete_button.grid(row=7, column=1)
        self.error.grid(row=9)



root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()