import tkinter as tk

class OptionsGUI:
    def __init__(self, options, title,param = None):
        self.options = options
        self.selected = []

        self.window = tk.Tk()
        self.window.title(title)

        self.label = tk.Label(self.window, text="Select "+str(title)+" :")
        self.label.pack()

        self.checkboxes = []
        for option in options:
            var = tk.BooleanVar()
            if param != None:
                checkbox = tk.Checkbutton(self.window, text=option[param], variable=var)
            else:
                checkbox = tk.Checkbutton(self.window, text=option, variable=var)
            checkbox.pack()
            self.checkboxes.append((option, var))

        self.button = tk.Button(self.window, text="Submit", command=self.submit)
        self.button.pack()

        self.window.mainloop()

    def submit(self):
        for option, var in self.checkboxes:
            if var.get():
                self.selected.append(option)

        self.window.destroy()

#options = {"Option 1": True, "Option 2": False, "Option 3": True}

