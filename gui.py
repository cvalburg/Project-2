from tkinter import *
from authorize import *
from transaction import *

class Gui:
    """
    This is the GUI used to input a users bank information and to make transactions
    """
    def __init__(self, window):
        """
        Initializes GUI layout

        :param window: Tkinter window to display the GUI
        """
        self.window = window

        self.user_data = {}

        # First Name input
        self.frame_first = Frame(self.window)
        self.label_first = Label(self.frame_first, text='First Name')
        self.input_first = Entry(self.frame_first, width=25)

        self.label_first.pack(side='left')
        self.input_first.pack(padx=50, side='left')
        self.frame_first.pack(anchor='w', padx=10, pady=5)

        # Last Name input
        self.frame_last = Frame(self.window)
        self.label_last = Label(self.frame_last, text='Last Name')
        self.input_last = Entry(self.frame_last, width=25)

        self.label_last.pack(side='left')
        self.input_last.pack(padx=50, side='left')
        self.frame_last.pack(anchor='w', padx=10, pady=5)

        # PIN input
        self.frame_pin = Frame(self.window)
        self.label_pin = Label(self.frame_pin, text='Enter PIN')
        self.input_pin = Entry(self.frame_pin, width=25, show='*')

        self.label_pin.pack(side='left')
        self.input_pin.pack(padx=50, side='left')
        self.frame_pin.pack(anchor='w', padx=10, pady=5)

        # Button for searching existence of users
        self.search_button = Button(self.window, text='SEARCH', command=lambda: authorize_user(self))
        self.search_button.pack(pady=10)

        # Welcome_label remains empty until existence of user is found
        self.welcome_label = Label(self.window, text='')
        self.welcome_label.pack()

        # Message label questioning
        self.mes_label = Label(self.window, text='What would you like to do?')
        self.mes_label.pack()

        # Radio button set up
        self.radio_answer = IntVar()
        # Default radio_answer
        self.radio_answer.set(0)
        radio_frame = Frame()
        radio_frame.pack(anchor='center', pady=10)
        # Radio button for withdrawing
        self.radio_withdraw = Radiobutton(radio_frame, text='Withdraw', variable=self.radio_answer, value=1)
        # Radio button for depositing
        self.radio_deposit = Radiobutton(radio_frame, text='Deposit', variable=self.radio_answer, value=2)
        self.radio_withdraw.pack(side='left', padx=10)
        self.radio_deposit.pack(side='left', padx=10)

        # Amount input
        self.frame_amount = Frame(self.window)
        self.label_amount = Label(self.frame_amount, text='Amount')
        self.input_amount = Entry(self.frame_amount, width=25)

        self.label_amount.pack(side='left')
        self.input_amount.pack(padx=50, side='left')
        self.frame_amount.pack(anchor='w', padx=10, pady=5)

        # Balance label remains empty until user has successfully or failed to make a transaction
        self.balance_label = Label(self.window, text='')
        self.balance_label.pack()

        button_frame = Frame()
        button_frame.pack(pady=10)
        # Enter button for transaction to occur
        self.enter_button = Button(button_frame, text='ENTER', command=lambda: transaction(self))
        self.enter_button.pack(side='left', padx=10)
        # Exit button closes the GUI and program
        self.exit_button = Button(button_frame, text='EXIT', command=self.window.quit)
        self.exit_button.pack(side='left', padx=10)

    def update_csv(self):
        """
        If transaction was successful whether it be from withdrawing or depositing in transaction.py
        Then update_csv will update the balance from that users row in accounts.csv

        :return: None
        """
        user_data = self.user_data
        user_data['Balance'] = f"{float(user_data['Balance']):.2f}"
        rows = []

        # Opens accounts.csv in read mode to check if user data matches what is in accounts.csv
        with open('accounts.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['FirstName'] == user_data['FirstName'] and row['LastName'] == user_data['LastName'] and \
                        row['PIN'] == user_data['PIN']:
                    row['Balance'] = user_data['Balance']
                rows.append(row)

        # Opens accounts.csv in write mode to update the new transaction in users row
        with open('accounts.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['FirstName', 'LastName', 'PIN', 'Balance'])
            writer.writeheader()
            writer.writerows(rows)
