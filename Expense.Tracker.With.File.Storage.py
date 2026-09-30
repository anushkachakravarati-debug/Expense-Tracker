# ===========EXPENSE TRACKER============

# ==============================
# CLASS EXPENSE
# ==============================

class Expense:
    def __init__(self,date,category,description,amount,):
        self.date = date
        self.category = category
        self.description = description
        self.amount = amount

    def to_file_format(self):
        return f"{self.date}|{self.category}|{self.description}|{self.amount}\n"

    @classmethod
    def from_file_format(cls,line):
        data = line.strip().split("|")
        return cls(
            data[0],
            data[1],
            data[2],
            float(data[3])
        )

# =====================
# CLASS EXPENSE TRACKER
# =====================

class ExpenseTracker:
    def __init__(self,filename ="expenses.txt"):
        self.filename = filename
        self.expenses = []
        self.load_from_file()

         # --------------
         # ADD EXPENSE
         # --------------

    def add_expense(self):
        date = input("Enter date: ")
        category = input("Enter category: ")
        description = input("Enter description: ")
        amount = float(input("Enter amount: "))

        expense = Expense(date,category,description,amount)
        
        self.expenses.append(expense)
        self.Save_to_file()
        print("Expense added Successfully! ")

        # ------------------
        # VIEW EXPENSE
        # ------------------

    def view_expenses(self):
        if not self.expenses:
            print("No expenses found. ")

            return

        print("\n====== ALL EXPENSES ======")

        for i, expense in enumerate(self.expenses,start=1):
            print(f"{i}. {expense.date} - {expense.category} - {expense.description} - Rs.{expense.amount}")

        # ------------------
        # SEARCH EXPENSE
        # ------------------

    def search_expense(self):
        category = input("Enter category to search: ")

        found = False

        for expense in self.expenses:
            if expense.category.lower() == category.lower():
                print(f"{expense.date}|{expense.category}|{expense.description}|Rs.{expense.amount}")

                found = True

                if not found:
                    print("No expense found in this category.")

        # --------------------
        # DELETE EXPENSE
        # --------------------

    def delete_expense(self):

        self.view_expenses()

        if not self.expenses:
            return

        number = int(input("Enter a expense number to delete: "))

        if 1 <= number <= len(self.expenses):

            deleted = self.expenses.pop(number - 1)
            self.Save_to_file()

            print(f"Deleted: {deleted.description} ({deleted.category})")

        else:
            print("Invalid expense number.")

        # ------------------------
        # SHOW TOTAL
        # ------------------------

    def show_total(self):
        total = 0
        for expense in self.expenses:
            total += expense.amount
            print(f"Total Expenses: Rs.{total}")

        # -----------------------
        # SAVE TO FILE
        # -----------------------

    def Save_to_file(self):
        with open(self.filename, "w") as file:

            for expense in self.expenses:
                file.write(expense.to_file_format())

        # -------------------
        # LOAD FROM FILE
        # -------------------


    def load_from_file(self):
        try: 

          with open(self.filename, "r") as file:
              
              for line in file:
                  if line.strip():
                      expense = Expense.from_file_format(line)

                      self.expenses.append(expense)

        except FileNotFoundError:
            pass

# ==================================
# MAIN PROGRAM
# ==================================


def main():

    tracker = ExpenseTracker()

    while True:

        print("\n========= EXPENSE TRACKER =========")
        print("1. Add Expense")
        print("2. View Expense")
        print("3. Search Expense")
        print("4. Delete Expense")
        print("5. Show Total")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            tracker.add_expense()

        elif choice == "2":
            tracker.view_expenses()

        elif choice == "3":
            tracker.search_expense()

        elif choice == "4":
            tracker.delete_expense()

        elif choice == "5":
            tracker.show_total()

        elif choice == "6":
            print("Thank you! ")
            break

        else:
            print("Invalid choice.")

main()