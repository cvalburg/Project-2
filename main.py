from gui import *

def main():
    """
    Main function to run ATM application

    This creates a Tkinter window, sets title, size for window, not
    resizable, and loops until window is closed

    :return: None
    """

    # Initializes the Tkinter window
    window = Tk()

    # Sets title of the window
    window.title('ATM')

    # Sets size of the window
    window.geometry('300x360')

    # Makes sure that window is not resizable
    window.resizable(False, False)

    # Creates instance of the GUI class to display the ATM interface
    Gui(window)

    # Loops to run the application
    window.mainloop()

if __name__ == '__main__':
    main()
