import tkinter as tk
#from PIL import Image, ImageTk

class StoryCreator:
    def __init__(self, root):
        self.root = root
        self.root.title("Story Creator")
        tk.geometry("500x500")
        self.counter = 0

        self.display_label = tk.Label(root, text="Hello, welcome to Story Creator", font=("Helvetica", 20))
        self.display_label.pack()

        self.display_label = tk.Label(root, text="First, chose a story genre", font=("Helvetica", 16))
        self.display_label.pack()

        self.button1 = tk.Button(root, text="Adventure", command=self.goto_adventureguide, font=("Helvetica", 14))
        self.button1.pack()

        self.button2 = tk.Button(root, text="Horror", command=self.goto_horrorguide, font=("Helvetica", 14))
        self.button2.pack()

        #self.history_listbox = tk.Listbox(root)
        #self.history_listbox.pack()

    def goto_adventureguide(self):
        adventure_guide = [
            "Let's create your adventure! What is your plot?",
            "The Quest",
            "Overcoming the Monster",
            "What's the setting?",
            "Medival Times",
            "The Future",
            "Who is your Hero?",
            "A young lad",
            "An unwilling Hero"
        ]

        for widget in self.root.winfo_children():
            widget.destroy()

        self.display_label = tk.Label(root, text=adventure_guide[self.counter], font=("Helvetica", 16))
        self.display_label.pack()

        self.button1 = tk.Button(root, text=adventure_guide[self.counter + 1], command=self.goto_adventureguide, font=("Helvetica", 14))
        self.button1.pack()

        self.button2 = tk.Button(root, text=adventure_guide[self.counter + 2], command=self.goto_adventureguide, font=("Helvetica", 14))
        self.button2.pack()

        self.counter = self.counter + 3

    def goto_horrorguide(self):
        horror_guide = [
            "Let's create your horror story! What is your plot?",
            "The Quest",
            "Overcoming the Monster",
            "What's the setting?",
            "A Haunted House",
            "A Dark Foggy Creek",
            "Who is your Hero?",
            "A young lad",
            "A teenager"
        ]
        
        for widget in self.root.winfo_children():
            widget.destroy()

        self.display_label = tk.Label(root, text=horror_guide[self.counter], font=("Helvetica", 16))
        self.display_label.pack()

        self.button1 = tk.Button(root, text=horror_guide[self.counter + 1], command=self.goto_horrorguide, font=("Helvetica", 14))
        self.button1.pack()

        self.button2 = tk.Button(root, text=horror_guide[self.counter + 2], command=self.goto_horrorguide, font=("Helvetica", 14))
        self.button2.pack()

        self.counter = self.counter + 3

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

root = tk.Tk()
story = StoryCreator(root)
root.mainloop()