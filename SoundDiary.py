from tkinter import Tk, scrolledtext, Menu, filedialog, messagebox, simpledialog
import tkinter.scrolledtext as ScrolledText
from tkinter import *
import os
import PyAudio, playsound, speech_recognition as sr
from gtts import gTTS

class SoundDictonary():

    def __init__(self):
        self.root = Tk(className=" Sound Diary")
        # Menu options
        self.menu = Menu(self.root)
        self.root.config(menu=self.menu)
        self.fileMenu = Menu(self.menu)
        self.menu.add_cascade(label="File...", menu=self.fileMenu)
        self.fileMenu.add_command(label="New", command=self.new_file)
        self.fileMenu.add_command(label="Open", command=self.open_file)
        self.fileMenu.add_command(label="Save", command=self.save_file)
        self.fileMenu.add_command(label="Find", command=self.find_in_file)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Exit", command=self.exit_root)

        self.menu.add_cascade(label="Sound for contents...", command=self.speak)

        self.textArea = ScrolledText.ScrolledText(self.root, width=100, height=80)
        self.textArea.pack(fill=BOTH)

        # Keep window open
        self.root.mainloop()


    def new_file(self):
        # There is content?
        if len(self.textArea.get("1.0", END + "-1c")) > 0:
            if messagebox.askyesno("Save?", "Do you wish to save?"):
                self.save_file()

            else:
                self.textArea.delete("1.0", END)

        self.root.title(" - TEXT EDITOR")


    def open_file(self):
        self.textArea.delete("1.0", END)
        self.file = filedialog.askopenfile(parent=self.root, title="Select a text file"
                                          , filetypes=(("Text file", "*.txt"), ("All files", "*.*")))

        self.root.title(os.path.basename(self.file.name) + " - TEXT EDITOR")

        if self.file != None:
            contents = self.file.read()
            self.textArea.insert("1.0", contents)
            self.file.close()


    def save_file(self):
        self.file = filedialog.asksaveasfile(mode="w", defaultextension=".txt"
                                        , filetypes=(("HTML file", "*.html"), ("Text file", "*.txt")
                                                     , ("All file", "*.*")))

        if self.file != None:
            # Slice off the last character from get, as an extra return (enter) is added
            self.data = self.textArea.get("1.0", END + "-1c")
            self.file.write(self.data)
            self.file.close()


    def find_in_file(self):
        self.findString = simpledialog.askstring("Find...", "Enter Text")
        self.textData = self.textArea.get("1.0", END)

        self.occurances = self.textData.upper().count(self.findString.upper())

        if self.textData.upper().count(self.findString.upper()) > 0:
            label = messagebox.showinfo("Results", self.findString + " has multiple occurances, " + str(self.occurances))

        else:
            label = messagebox.showinfo("Results", "Sorry")


    def speak(self):
        try:
            self.tts = gTTS(text=self.textArea.get("1.0", END), lang="en")
            self.soundfilename = "voice.mp3"
            self.tts.save(self.soundfilename)
            playsound.playsound(self.soundfilename)
        except:
            messagebox.showerror("Connection problem", "Check your internet connection")


    def exit_root(self):
        if messagebox.askyesno("Quit", "Are you sure you want to quit"):
            self.root.destroy()


    def about(self):
        self.label = messagebox.showinfo("About", "A Python alternative to Notepad!")


if __name__ == "__main__":
    SoundDictonary = SoundDictonary()