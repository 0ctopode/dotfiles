#!/usr/bin/python3.10

"""
manageScriptsGUI.py - HRBush - 07/01/21
Graphical tool to add and remove entries in the rofi script launcher
"""
from tkinter import *
from tkinter.scrolledtext import *
import os

cmd_file = '/home/hrbush/.config/rofi/cmd.csv'

class Window:
    def __init__(self, parent):
        self.parent = parent
        parent.configure(bg='#1e2229')
        parent.title('Script Manager')  # Useless on i3 but oh well it's here

        self.AdditionLabel = Label(parent, text='Entry Addition', fg='white', bg='#1e2229', font=('monospace', '20', 'bold'))
        self.AddScriptLabel = Label(parent, text='Label: ', fg='white', bg='#1e2229', font=('monospace', '12', 'normal'))
        self.AddLabelEntry = Entry(parent, bd=0, bg='#e0e0e0', fg='black', width=50)
        self.AddScriptPath = Label(parent, text='Path: ', fg='white', bg='#1e2229', font=('monospace', '12', 'normal'))
        self.AddPathEntry = Entry(parent, bd=0, bg='#e0e0e0', fg='black', width=50)
        self.AdditionButton = Button(parent, text="Add Entry", command=self.add_entry, width=30)

        self.RemovalEntryLabel = Label(parent, text='Entry Removal', fg='white', bg='#1e2229', font=('monospace', '20', 'bold'))
        self.RemoveLabel = Label(parent, text='Label: ', fg='white', bg='#1e2229', font=('monospace', '12', 'normal'))
        self.RemoveLabelEntry = Entry(parent, bd=0, bg='#e0e0e0', fg='black', width=50)
        self.RemovalButton = Button(parent, text="Remove Entry", command=self.remove_entry, width=30)

        self.text = ScrolledText(parent, width=65, height=20, background='#2a2f38', wrap='word', fg='white')

        self.AdditionLabel.grid(column=0, row=0, columnspan=2, pady=(15, 5))
        self.AddScriptLabel.grid(column=0, row=1, pady=3, padx=(18, 2))
        self.AddLabelEntry.grid(column=1, row=1, pady=3)
        self.AddScriptPath.grid(column=0, row=2, pady=3, padx=(18, 2))
        self.AddPathEntry.grid(column=1, row=2, pady=3)
        self.AdditionButton.grid(column=0, row=3, columnspan=2, pady=3, padx=(18, 2))

        self.RemovalEntryLabel.grid(column=0, row=4, columnspan=2, pady=(14, 5))
        self.RemoveLabel.grid(column=0, row=5, pady=3, padx=(18, 2))
        self.RemoveLabelEntry.grid(column=1, row=5, pady=3)
        self.RemovalButton.grid(column=0, row=6, columnspan=2, pady=3, padx=(18, 2))

        self.text.grid(column=0, row=7, columnspan=2, pady=20, padx=18)

        self.update_text()

    def add_entry(self):
        label = self.AddLabelEntry.get()
        path = self.AddPathEntry.get()

        f = open(cmd_file, 'a')
        f.write(label + ',' + path + '\n')
        f.close()

        self.AddLabelEntry.delete(0, 'end')
        self.AddPathEntry.delete(0, 'end')
        self.update_text()

    def remove_entry(self):
        label = self.RemoveLabelEntry.get()

        with open(cmd_file, 'r') as f:
            lines = f.readlines()
        with open(cmd_file, 'w') as f:
            for line in lines:
                if not line.startswith(label):
                    f.write(line)

        self.RemoveLabelEntry.delete(0, 'end')
        self.update_text()

    def update_text(self):
        self.text.delete('1.0', END)

        with open(cmd_file, 'r') as f:
            lines = f.readlines()

        for line in lines:
            self.text.insert(INSERT, line)


def main():
    root = Tk()
    GUI = Window(root)
    root.mainloop()


if __name__ == '__main__':
    main()

