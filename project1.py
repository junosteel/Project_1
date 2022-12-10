from gui import *

def main() -> None:
    '''
    Function to call on the gui file and create a window.
    '''
    window = Tk()
    window.geometry('325x175')
    window.resizable(False, False)

    widgets = Voting(window)
    window.mainloop()


if __name__ == '__main__':
    main()