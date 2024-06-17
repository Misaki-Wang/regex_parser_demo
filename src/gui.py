import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from nfa import NFA, regex_to_nfa
from dfa import DFA, nfa_to_dfa

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
        self.display_image("nfa.png")

    def convert_to_dfa(self):
        regex = self.regex_entry.get()
        nfa = regex_to_nfa(regex)
        dfa = nfa_to_dfa(nfa)
        dfa.to_graphviz("dfa")
        self.result_label.config(text="DFA created. States: {}".format(dfa.states))
        self.steps_label.config(text="\n".join(dfa.steps))
        self.display_image("dfa.png")

    def display_image(self, image_path):
        img = Image.open(image_path)
        img = img.resize((600, 400), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(img)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

if __name__ == "__main__":
    root = tk.Tk()
    app = RegexParserGUI(root)
    root.mainloop()
