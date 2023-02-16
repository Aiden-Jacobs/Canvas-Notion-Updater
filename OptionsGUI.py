import tkinter as tk

class OptionsGUI:
    """
    A class to create a GUI that allows the user to select options.
    Attributes:
    - options (list): A list of options to display in the GUI.
    - selected (list): A list to store the selected options.
    - window (Tk): The main window of the GUI.
    - label (Label): A label that displays the title of the options.
    - checkboxes (list): A list of tuples, each containing an option and a BooleanVar that indicates if it is selected.
    - button (Button): A button that submits the selected options.

    Methods:
    - __init__(self, options, title, param=None): Initializes the GUI with the given options, title and an optional parameter.
    - submit(self): Retrieves the selected options and stores them in self.selected. Closes the GUI.
    """
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


