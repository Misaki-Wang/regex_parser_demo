'''
Author: misaki misakiwang74@gmail.com
Date: 2024-06-18 15:01:16
LastEditors: misaki misakiwang74@gmail.com
LastEditTime: 2024-06-18 15:59:32
FilePath: /regex_parser_demo/src/gui.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from src.nfa import NFA, regex_to_nfa
from src.dfa import DFA, nfa_to_dfa

result_dir = "./results/"

class RegexParserGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Regex Parser Demo")
        
        self.regex_label = tk.Label(master, text="Enter Regex:")
        self.regex_label.pack()
        self.regex_entry = tk.Entry(master)
        self.regex_entry.pack()
        
        self.nfa_button = tk.Button(master, text="Convert to NFA", command=self.convert_to_nfa)
        self.nfa_button.pack()
        self.dfa_button = tk.Button(master, text="Convert to DFA", command=self.convert_to_dfa)
        self.dfa_button.pack()
        
        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

        self.steps_label = tk.Label(master, text="")
        self.steps_label.pack()
        
        self.canvas = tk.Canvas(master, width=600, height=400)
        self.canvas.pack()

    def convert_to_nfa(self):
        regex = self.regex_entry.get()
        nfa = regex_to_nfa(regex)
        nfa.to_graphviz("nfa")
        self.result_label.config(text="NFA created. States: {}".format(nfa.states))
        self.steps_label.config(text="\n".join(nfa.steps))
        self.display_image(f"{result_dir}nfa.png")

    def convert_to_dfa(self):
        regex = self.regex_entry.get()
        nfa = regex_to_nfa(regex)
        dfa = nfa_to_dfa(nfa)
        dfa.to_graphviz("dfa")
        self.result_label.config(text="DFA created. States: {}".format(dfa.states))
        self.steps_label.config(text="\n".join(dfa.steps))
        self.display_image(f"{result_dir}dfa.png")

    def display_image(self, image_path):
        img = Image.open(image_path)
        img = img.resize((600, 400), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(img)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

def main():
    root = tk.Tk()
    app = RegexParserGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()