from basechange import BaseChange
from window import Window

from tkinter import Tk

app_title = "Base Changer"
geom = "250x250"


#   Define BaseChange window
class BaseChangeWindow (Window) :

    def convert_button (self) :
    #   Take string variable inputs from UI and convert into useable strings
        num = self.e1_text.get()
        base_a = self.e2_text.get()
        base_b = self.e3_text.get()

        #   Convert num from base_a to base_b
        conversion = BaseChange.basechange(num, base_a, base_b)

        #   Place output on screen
        self.lb1.delete(0)
        self.lb1.insert(0, conversion)

#   Run the App

if __name__ == "__main__" :

    window = Tk()

    BaseChangeWindow(window, app_title, geom)

    window.mainloop()