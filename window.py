from tkinter import *

class Window:
    '''
    Base class for other windows. Do not instantiate from this class.
    '''
    def __init__ (self, window, app_title, geom):
        self.window = window
        self.title_font = ("Helvetic", 24)

        self._config_window(app_title, geom)
        self._interface()


    def _config_window (self, app_title, geom):
        self.window.wm_title(app_title)
        self.window.resizable(False, False)
        self.window.geometry(geom)

        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_columnconfigure(1, weight=1)
        self.window.grid_columnconfigure(2, weight=1)

        self.title1 = Label(self.window, text=app_title, font = self.title_font, justify=CENTER)
        

    def _interface (self):
        #   Input number entry box
        self.e1_text = StringVar()
        self.e1 = Entry(self.window, textvariable=self.e1_text, justify=CENTER)

        #   Input number Label
        self.e1_label = Label(self.window, text="Number", justify=CENTER)

        #   Input base entry box
        self.e2_text = StringVar()
        self.e2 = Entry(self.window, textvariable=self.e2_text, justify=CENTER)

        #   Input base Label
        self.e2_label = Label(self.window, text="Base a", justify=CENTER)

        #   Convert Button
        self.convert = Button(self.window, text="CONVERT", command=self.convert_button)

        #   Output Listbox
        self.lb1 = Listbox(self.window, height=1)

        #   Output number Label
        self.lb1_label = Label(self.window, text="Result", justify=CENTER)

        #   Output Base entry box
        self.e3_text = StringVar()
        self.e3 = Entry(self.window, textvariable=self.e3_text, justify=CENTER)

        #   Output Base Label
        self.e3_label = Label(self.window, text="Base b", justify=CENTER)

        #   Place everything in the window
        self.title1.grid(row=0, column=0, columnspan=3, rowspan=1, pady = 10)
        
        self.e1_label.grid(row=1, column=1, padx=5)
        self.e1.grid(row = 2, column = 1, padx=10)

        self.e2_label.grid(row=3, column=0, padx=5)
        self.e2.grid(row=4, column=0, padx=10)

        self.e3_label.grid(row=3, column=2, padx=5)
        self.e3.grid(row=4, column=2, padx=10)

        self.convert.grid(row=4, column=1, padx=10, pady=10)

        self.lb1_label.grid(row=5, column=1, padx=5, pady=5)
        self.lb1.grid(row=6, column=1, padx=10)

        #   Add default values
        self.e1.insert(0, "101")
        self.e2.insert(0, "2")
        self.e3.insert(0, "10")
        self.convert_button()


    def convert_button (self) :
        '''Implemented in subclass.'''
        raise NotImplementedError
