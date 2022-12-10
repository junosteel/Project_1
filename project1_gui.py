from tkinter import *
import csv
import re

votes_dict = {'Voter ID': 'Candidate'} #Dictionary to store voter ids with the candidate they voted for

def new_window() -> None:
    '''
    Function to create a second window.
    '''
    window2 = Toplevel()
    window2.geometry('325x175')
    window2.resizable(False, False)

    widgets2 = Candidates(window2)
    window2.mainloop()

class Voting:
    '''
    A class representing details for the voting screen.
    '''
    def __init__(self, window) -> None:
        '''
        Constructor to create the first window's widgets.
        :param window: Name of window being modified.
        '''
        self.window = window

        self.frame_intro = Frame(self.window)
        self.label_intro = Label(self.frame_intro, text='----------------- VOTE MENU -----------------')
        self.label_intro.pack()
        self.frame_intro.pack(anchor='c', pady=10)

        self.frame_option = Frame(self.window)
        self.label_option = Label(self.frame_option, text='Option:')
        self.radio_option = IntVar()
        self.radio_option.set(0)
        self.radio_vote = Radiobutton(self.frame_option, text='Vote', variable=self.radio_option, value=0)
        self.radio_exit = Radiobutton(self.frame_option, text='Exit', variable=self.radio_option, value=1)
        self.label_option.pack(padx=5, side='left')
        self.radio_vote.pack(padx=5, side='left')
        self.radio_exit.pack(padx=5, side='left')
        self.frame_option.pack(anchor='c', pady=20)

        self.frame_select = Frame(self.window)
        self.button_select = Button(self.frame_select, text='SELECT', command=self.select)
        self.button_select.pack()
        self.frame_select.pack(anchor='c', pady=20)

    def select(self) -> None:
        '''
        Function to check which radio has been selected, and then close the program or create a second window depending on results.
        '''
        option = self.radio_option.get()

        if option == 0:
            new_window()
        else:
            exit()

class Candidates:
    '''
    A class representing details for the candidate screen.
    '''
    def __init__(self, window2) -> None:
        '''
        Constructor to create the second window's widgets.
        :param window2: Name of window being modified.
        '''
        self.window2 = window2

        self.frame_names = Frame(self.window2)
        self.label_names = Label(self.frame_names, text='----------------- CANDIDATES -----------------')
        self.label_names.pack()
        self.frame_names.pack(anchor='c', pady=10)

        self.frame_voter = Frame(self.window2)
        self.label_id = Label(self.frame_voter, text='Voting ID:')
        self.entry_id = Entry(self.frame_voter)
        self.label_id.pack()
        self.entry_id.pack()
        self.frame_voter.pack(anchor='c', pady=5)

        self.frame_candidate = Frame(self.window2)
        self.label_candidate = Label(self.frame_candidate, text='Candidate:')
        self.radio_candidate = IntVar()
        self.radio_candidate.set(0)
        self.radio_first = Radiobutton(self.frame_candidate, text='Jane', variable=self.radio_candidate, value=0)
        self.radio_sec = Radiobutton(self.frame_candidate, text='John', variable=self.radio_candidate, value=1)
        self.label_candidate.pack(padx=5, side='left')
        self.radio_first.pack(side='left')
        self.radio_sec.pack(side='left')
        self.frame_candidate.pack(anchor='c', pady=10)

        self.frame_vote = Frame(self.window2)
        self.button_vote = Button(self.frame_vote, text='VOTE', command=self.vote)
        self.button_vote.pack()
        self.frame_vote.pack()

    def vote(self) -> None:
        '''
        Function to check which radio has been selected and grab user input, and then display the results while updating the dictionary and sending the information to a csv file before closing the window.
        '''
        vote = self.radio_candidate.get()
        id = self.entry_id.get()

        if id == '':
            self.label_id['text'] = 'Required. Enter voting ID:'
        elif id in votes_dict:
            self.label_id['text'] = 'Already voted. Enter new ID:'
            self.entry_id.delete(0, END)
        elif vote == 0:
            votes_dict.update({id: 'Jane'})
            self.label_names['text'] = 'Voted Jane'
            self.frame_candidate.destroy()
            self.button_vote.destroy()
            self.window2.after(2000, lambda: self.window2.destroy())
        else:
            votes_dict.update({id: 'John'})
            self.label_names['text'] = 'Voted John'
            self.frame_candidate.destroy()
            self.button_vote.destroy()
            self.window2.after(2000, lambda: self.window2.destroy())

        with open('votes.csv', 'w', newline='') as votes_csv:
            content = csv.writer(votes_csv)
            for key, value in votes_dict.items():
                content.writerow([key] + [value])