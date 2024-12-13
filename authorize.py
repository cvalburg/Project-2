import csv

def authorize_user(self):
    """
    Authorizes an existing user in the accounts.csv by their first name, last name
    and PIN

    Gets data from user input then stores it, makes sure you fill out all values, opens
    accounts.csv to update the GUI

    :param self:
    :return: None
    """

    # Collects the users input for first name, last name, and PIN
    first_name = self.input_first.get().strip()
    last_name = self.input_last.get().strip()
    pin = self.input_pin.get().strip()

    # Makes sure all values are filled
    if not first_name or not last_name or not pin:
        self.welcome_label.config(text='Please fill in all values')
        return

    try:
        # Opens accounts.csv file in read mode
        with open('accounts.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Checks to see if user input matches the existing account in accounts.csv
                if row['FirstName'] == first_name and row['LastName'] == last_name and row['PIN'] == pin:
                    self.user_data = row
                    # Updates the GUI with existing users first name and last
                    self.welcome_label.config(text=f'Welcome {first_name} {last_name}!')
                    # Updates the GUI with the current account balance for existing user
                    self.balance_label.config(text=f"Your account balance is: ${float(row['Balance']):.2f}")
                    return

            # Updates the GUI if no match is found or PIN is incorrect
            self.welcome_label.config(text='User not found or incorrect PIN')

    except FileNotFoundError:
        # Updates the GUI if there is no accounts.csv in users path directory
        self.welcome_label.config(text='accounts.csv is not found')