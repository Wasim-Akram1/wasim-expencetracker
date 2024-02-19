import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import Calendar
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class ExpenseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")
        self.root.configure(bg="#87CEEB")

        self.expenses = []

        self.date_label = ttk.Label(self.root, text="Select Date:")
        self.date_label.grid(row=0, column=0, padx=10, pady=10)

        self.cal = Calendar(self.root, selectmode='day', date_pattern='yyyy-mm-dd')
        self.cal.grid(row=0, column=1, padx=10, pady=10)

        self.expense_label = ttk.Label(self.root, text="Enter Expense:")
        self.expense_label.grid(row=1, column=0, padx=10, pady=10)

        self.expense_entry = ttk.Entry(self.root, width=30)
        self.expense_entry.grid(row=1, column=1, padx=10, pady=10)

        self.category_label = ttk.Label(self.root, text="Enter Category:")
        self.category_label.grid(row=2, column=0, padx=10, pady=10)

        self.category_entry = ttk.Entry(self.root, width=30)
        self.category_entry.grid(row=2, column=1, padx=10, pady=10)

        self.add_expense_button = ttk.Button(self.root, text="Add Expense", command=self.add_expense)
        self.add_expense_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.view_expense_button = ttk.Button(self.root, text="View Expenses", command=self.view_expenses)
        self.view_expense_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def add_expense(self):
        selected_date = self.cal.get_date()
        expense = self.expense_entry.get()
        category = self.category_entry.get()

        if selected_date and expense and category:
            self.expenses.append({'date': selected_date, 'expense': expense, 'category': category})
            messagebox.showinfo("Success", "Expense added successfully.")
            self.clear_inputs()
        else:
            messagebox.showerror("Error", "Please fill all fields.")

    def clear_inputs(self):
        self.expense_entry.delete(0, tk.END)
        self.category_entry.delete(0, tk.END)

    def view_expenses(self):
        if not self.expenses:
            messagebox.showinfo("Info", "No expenses to display.")
            return

        top = tk.Toplevel(self.root)
        top.geometry('500x500')
        top.title("Expense Data")

        listbox = tk.Listbox(top,width=500,height=500)
        listbox.pack()

        for expense in self.expenses:
            listbox.insert(tk.END, f"Date: {expense['date']}, Expense: {expense['expense']}, Category: {expense['category']}")

        self.plot_expense_patterns()

    def plot_expense_patterns(self):
        if not self.expenses:
            messagebox.showinfo("Info", "No expenses to plot.")
            return

        categories = set(expense['category'] for expense in self.expenses)
        category_expenses = {category: sum(float(expense['expense']) for expense in self.expenses if expense['category'] == category) for category in categories}

        fig, ax = plt.subplots()
        ax.pie(category_expenses.values(), labels=category_expenses.keys(), autopct='%1.1f%%', startangle=90)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        plt.title('Expense Distribution by Category')

        plt.show()


def main():
    root = tk.Tk()
    expense_tracker = ExpenseTrackerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
