import json
import datetime
from GUI import main

# Global dictionary to store transactions
transactions = {}


# load transactions from json file
def load_transactions():
    try:
        global transactions
        file = open("transactions.json", "r")
        transactions = json.load(file)
        file.close()
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        pass


# save transactions to json file
def save_transactions(save_code):
    file = open("transactions.json", "w")
    json.dump(transactions, file)
    file.close()

    if save_code == 1:
        print("\n+++++Transaction(s) Saved Successfully!+++++")
    elif save_code == 2:
        print("\n+++++Transaction Deleted successfully!+++++")
    elif save_code == 3:
        print("\n+++++Transaction Updated successfully!+++++")


# add transactions to dictionary
def add_todictionary(expense_type, amount, date):
    trans_dict = dict(amount=amount, date=date)

    if expense_type in transactions:  # checks if transaction expense type already exist
        transactions[expense_type].append(trans_dict)
    else:
        transactions[expense_type] = [trans_dict]


# read transactions from text file and save to json file
def read_bulk_transactions_from_file(filename):
    try:
        filename = filename + ".txt"
        file = open(filename, "r")

    except FileNotFoundError:
        print("**File is not found!**")
        print("Check the file name is correct")

    else:
        # checks if the text file date format is correct
        def file_date_check():
            try:
                datetime.datetime.strptime(line[2].strip('\n, '), "%Y-%m-%d")
                return True
            except ValueError:
                return False

        line_count = 0  # to find which line Error happens
        file_er = []  # All the lines which were Error happed
        for lines in file:  # get transactions from file line by line
            line_count += 1
            line = lines.split(',')  # line element split and create lists

            if (len(line) == 3) and (line[1].isdigit()) and (file_date_check()):   # checks amount and date is valid format
                add_todictionary((line[0].lstrip()).rstrip(), int(line[1]), line[2].rstrip('\n, '))

            else:
                file_er.append(line_count)

        file.close()

        if not file_er:  # check error lines numbers available in the list
            pass
        else:
            word = ""
            for er_lines in file_er:
                word += str(er_lines) + ", "
            print(f"\n**Re-enter line(s) {word}on {filename} file.\nThose are not as correct FORMAT.**")
        save_transactions(1)


# get transaction date and checks if date is valid
def date_chek():
    while True:
        get_date = input("Enter transaction date (YYYY-MM-DD): ")
        try:
            datetime.datetime.strptime(get_date, "%Y-%m-%d")  # checks date format as YYYY-MM-DD
            return get_date
            break
        except ValueError:
            print("**Invalid Input!**")


# get transaction amount and checks if amount is valid
def amount_chek():
    while True:
        try:
            amount = int(input("Enter transaction amount-----------: "))
            return amount
            break
        except ValueError:
            print("**Invalid Input!**")


# collecting transactions data from user
def add_transaction():
    trans_expenses_type = input("\nEnter transaction expenses type----: ")
    trans_amount = amount_chek()
    trans_date = date_chek()

    add_todictionary(trans_expenses_type, trans_amount, trans_date)  # add to dictonary
    save_transactions(1)


# all transactions display in this section
def view_transactions():
    if not transactions:  # checks if transactions available
        print("\n----No Transactions!----")
    else:
        for key, value in transactions.items():
            print(f"\n---------{key}---------")

            count = 1
            for item in value:
                print(f"{count}. Amount: {item['amount']}  Date: {item['date']}")
                count += 1


# Update values
def change_value(key, dict_element, index):

    print(f"Current {dict_element}: {transactions[key][index][dict_element]}")  # Display current value

    if 'amount' == dict_element:
        new_value = amount_chek()  # amount validity checks and assign
    else:
        new_value = date_chek()  # date validity checks and assign

    transactions[key][index][dict_element] = new_value
    save_transactions(3)

# Select what you want to update (Amount or Date)
def choise(expense_type, row_no = 0):
    while True:
        change = input("Which one? 1.Amount 2.Date----: ")

        if change == "1":
            change_value(expense_type, 'amount', row_no)
            break

        elif change == "2":
            change_value(expense_type, 'date', row_no)
            break

        else:
            print("**Invalid Input!**")


# transactions update section
def update_transaction():
    if not transactions:
        print("\n----No Transactions!----")

    else:
        while True:
            expense_type = input("\nEnter transaction expense type: ")

            if expense_type in transactions:  # check if the user entered expense type in transactions
                if len(transactions[expense_type]) == 1:
                    choise(expense_type)
                    break

                else:
                    while True:
                        try:  # avoid getting ValueError for just press enter without enter any value
                            row_no = int(input("Which transaction (row no)----: "))
                            if (row_no >= 1) and (row_no <= len(transactions[expense_type])):  # check if the row number exist
                                choise(expense_type, row_no - 1)
                                break
                            else:
                                print(f"**Row number {row_no} doesn't exist**")
                        except ValueError:
                            print("**Invalid Input!**")
                    break

            else:
                print("**Transaction expense type doesn't exist**")


# transactions delete section
def delete_transaction():
    if not transactions:
        print("\n----No Transactions!----")

    else:
        while True:
            expense_type = input("\nEnter transaction expense type: ")
            if expense_type in transactions:  # check if user entered expense type in transactions
                if len(transactions[expense_type]) == 1:
                    del transactions[expense_type]
                    save_transactions(2)
                    break
                else:
                    while True:
                        try:
                            row_no = int(input("Which transaction(row no)? : "))
                            if (row_no >= 1) and (row_no <= len(transactions[expense_type])):  # check if the row number exist
                                del transactions[expense_type][row_no - 1]
                                save_transactions(2)
                                break
                            else:
                                print(f"**Row number {row_no} doesn't exist")

                        except ValueError:
                            print("**Invalid Input!**")
                    break

            else:
                print("**Transaction expense type doesn't exist")


# display summary of transactions
def display_summary():

    ex_types = len(transactions.keys())  # count all transactions expenses types
    elements = [value['amount'] for key, values in transactions.items() for value in values]  # get all transactons amount as a list

    print(f"\nExpenses types: {ex_types}")
    print(f"You have done {len(elements)} transactions")
    print(f"Total expenses amount is {sum(elements)}")


def main_menu():
    load_transactions()
    while True:
        print("\n+----------------------------+")
        print("|  Personal Finance Tracker  |")
        print("+----------------------------+")
        print("1.Add Transaction")
        print("2.Add Bulk Transaction")
        print("3.View Transactions via GUI")
        print("4.View Transactions via CLI")
        print("5.Update Transaction")
        print("6.Delete Transaction")
        print("7.Transactions Summary")
        print("8.Exit\n")


        choise = input("Enter your choise: ")

        if choise == "1":
            add_transaction()
        elif choise == "2":
            filename = input("\nEnter text file name: ")
            read_bulk_transactions_from_file(filename)
        elif choise == "3":
            main()
        elif choise == "4":
            view_transactions()
        elif choise == "5":
            update_transaction()
        elif choise == "6":
            delete_transaction()
        elif choise == "7":
            display_summary()
        elif choise == "8":
            break
        else:
            print("***Invalid Value is Entered***")


if __name__ == "__main__":
    main_menu()
