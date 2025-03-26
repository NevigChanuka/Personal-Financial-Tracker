import tkinter as tk
from tkinter import ttk, messagebox
import json


class FinanceTrackerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Finance Tracker")
        self.root.geometry("800x400")
        self.root.resizable(True, True)

        self.frame_top = tk.Frame(self.root)
        self.frame_mid = tk.Frame(self.root)
        self.table = ttk.Treeview(self.frame_mid, columns=("category", "amount", "date"), show="headings")
        self.entry_search = ttk.Entry(self.frame_top, width=50)

        self.create_widgets()
        self.transactions = self.load_transactions("transactions.json")
        self.sort = []


    def create_widgets(self):
        style = ttk.Style()

        self.frame_top.pack(pady=5)

        # Frame for table and scrollbar
        self.frame_mid.pack(padx=10, pady=10, fill="both", expand=True)

        # Treeview for displaying transactions
        self.table.heading("category", text="Category", anchor="w", command=lambda: self.sort_by_column("category"))
        self.table.heading("amount", text="Amount", anchor="w", command=lambda: self.sort_by_column("amount"))
        self.table.heading("date", text="Date", anchor="w", command=lambda: self.sort_by_column("date"))

        # Scrollbar for the Treeview
        scrollbar = ttk.Scrollbar(self.frame_mid, command=self.table.yview)
        self.table.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y", padx=2)
        self.table.pack(fill="both", expand=True)

        style.configure("Treeview.Heading", font=("Arial", 10, "bold"))

        # Search bar and button
        self.entry_search.pack(side="left")

        button_search = ttk.Button(self.frame_top, text="Search", command=self.search_transactions)
        button_search.pack(side="right", padx=20)

        # call the search_transactions function if you release any key
        self.entry_search.bind("<KeyRelease>", self.search_transactions)


    # loading transactions.json file
    def load_transactions(self, filename):
        try:
            with open(filename, "r") as file:
                return json.load(file)

        except FileNotFoundError:
            messagebox.showerror("Error", "transactions.json file is not found")
        except json.decoder.JSONDecodeError:
            return {}


    def display_transactions(self, transactions, search=False):

        # Remove existing entries
        for id in self.table.get_children():
            self.table.delete(id)

        # Add transactions to the treeview
        if transactions:
            for key, values in sorted(transactions.items()):
                for value in values:
                    self.table.insert('', index="end", values=(key, value['amount'], value['date']))

            self.sort += ["category", False] # for sorting
        else:
            if search:
                self.table.insert('', index="end", values=("", "No items match your search", ""))
            else:
                self.table.insert('', index="end", values=("", "No transactions", ""))


        # search transactions
        # if press enter or click search button, this happens
    def search_transactions(self, event="T"):

        search_value = self.entry_search.get().upper() # gets search bar value

        def is_available():
            transactions_dict={}
            if search_value.strip(): # checks entry have values
                for key, values in self.transactions.items():
                    if search_value == key.upper():  # checks category and user searched value is same
                        transactions_dict[key] = values

                    for index, value in enumerate(values):

                        if search_value == str(value["amount"]):  # checks amount and user searched value is same
                            transactions_dict[key] = [values[index]]

                        if search_value == value["date"]:   # checks date and user searched value is same
                            transactions_dict[key] = [values[index]]

                self.display_transactions(transactions_dict, True)
            else:
                self.display_transactions(self.transactions)



        try:
            if event.keysym == "Return":
                is_available()
            if not search_value.strip():
                is_available()
        except AttributeError:
            is_available()

    # sort transactions on table
    def sort_by_column(self, col):

        # checks the reverse attribute
        def sort_reverse(header_name):
            if self.sort[0] == header_name:
                self.sort[:] = [header_name, not self.sort[1]]
            else:
                self.sort[:] = [header_name, True]

        if col == "amount":  # if user click 'amount' column, this execute
            data = [(self.table.item(child)["values"][1], child) for child in self.table.get_children()]
            sort_reverse("amount")

        if col == "category":  # if user click 'category' column, this execute
            data = [(self.table.item(child)["values"][0], child) for child in self.table.get_children()]
            sort_reverse("category")

        if col == "date": # if user click 'date' column, this execute
            data = [(self.table.item(child)["values"][2], child) for child in self.table.get_children()]
            sort_reverse("date")

        # sorting transactions
        data.sort(reverse=self.sort[1])
        for index, (value, child) in enumerate(data):
            self.table.move(child, '', index)


def main():
    root = tk.Tk()
    app = FinanceTrackerGUI(root)
    app.display_transactions(app.transactions)
    root.mainloop()

if __name__ == "__main__":
    main()


