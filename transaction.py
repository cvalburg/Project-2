def transaction(self):
    """
    Processes a transaction whether it be to withdraw or deposit from the users input

    Checks to see if the user entered an existing user before entering anything in
    the amount, checks if a valid amount is entered, checks if either withdraw or
    deposit is selected, checks for insufficient funds entered, then updates the
    accounts.csv file in the users balance
    :param self:
    :return: None
    """

    # Makes sure that user data exists before making transaction
    if not self.user_data:
        self.balance_label.config(text='Please search for a user first')
        return

    # Makes sure that a positive valid amount is entered
    try:
        amount = float(self.input_amount.get().strip())
        if amount <= 0:
            self.balance_label.config(text='Enter a valid amount')
            return
    except ValueError:
        self.balance_label.config(text='Enter a valid amount')
        return

    # Collects the current balance and type of transaction
    current_balance = float(self.user_data['Balance'])
    answer = self.radio_answer.get()

    # Makes sure that the amount withdrawn is not going to make current balance zero
    # Also subtracts the current balance and amount entered
    # Also stores new balance when successful for both withdraw and deposit
    if answer == 1:
        if amount > float(self.user_data['Balance']):
            self.balance_label.config(text='Insufficient balance')
            return
        self.user_data['Balance'] = str(current_balance - amount)
    # Adds the current balance and amount entered
    elif answer == 2:
        self.user_data['Balance'] = str(current_balance + amount)

    # Makes sure that the user is selecting either withdraw or deposit
    else:
        self.balance_label.config(text='Please select an action')
        return

    # Updates accounts.csv file with new balance for existing user
    self.update_csv()

    # Displays the updated balance to the GUI
    self.balance_label.config(text=f"Your account balance is: ${float(self.user_data['Balance']):.2f}")