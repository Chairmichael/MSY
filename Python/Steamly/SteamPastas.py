#!/usr/bin/env 
# SteamPastas.py

import os, textwrap
import tkinter as tk

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        self._create_widgets()
        # self._foo()

    def _create_widgets(self):
        # textbox with scrollbar
        self.scroll = tk.Scrollbar(self)
        self.textBox = tk.Text(self, height=6, width=50, font=("Sans", 12))
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.textBox.pack(side=tk.LEFT, fill=tk.Y)
        self.scroll.config(command=self.textBox.yview)
        self.textBox.config(yscrollcommand=self.scroll.set)

        # browse for file

    def _foo(self):
        self.textbox.insert(tk.END, 'wow')



def main():
    root = tk.Tk()
    app = App(master=root)
    app.mainloop()

if __name__ == '__main__':
    main()
