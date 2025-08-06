import os
import datetime

class Transaction:
    def __init__(self, trans_type, amount, category, notes='', date=None):
        self.trans_type = trans_type  
        self.amount = amount
        self.category = category
        self.notes = notes
        self.date = date if date else datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_line(self):
        
        return f"{self.trans_type}|{self.amount}|{self.category}|{self.notes}|{self.date}"

    @staticmethod
    def from_line(line): #create transaction object line to line
        
        parts = line.strip().split('|')
        if len(parts) != 5:
            raise ValueError('Malformed transaction line.')
        trans_type, amount, category, notes, date = parts
        return Transaction(trans_type, float(amount), category, notes, date)



class BudgetTracker:
    def __init__(self, filename='transactions.txt'):
        self.transactions = []
        self.filename = filename
        self.load_transactions()

    def add_transaction(self, trans_type, amount, category, notes):
        t = Transaction(trans_type, amount, category, notes)
        self.transactions.append(t)
        print(f"Transaction added: {t.trans_type.title()} of {t.amount} in {t.category}")

    def list_transactions(self):
        if not self.transactions:
            print("No transactions to display.")
            return
        print("\n - All Transactions - ")
        for i, t in enumerate(self.transactions, start=1):
            print(
                f"{i}. {t.date} | {t.trans_type.title():7} | {t.amount:8.2f} | "
                f"{t.category:12} | {t.notes}"
            )

    def filter_transactions(self, by_type=None, by_category=None):
        filtered = self.transactions
        if by_type:
            filtered = [t for t in filtered if t.trans_type == by_type]
        if by_category:
            filtered = [t for t in filtered if t.category.lower() == by_category.lower()]
        if not filtered:
            print(f"No transactions found for the given filter.")
        else:
            print("\n- Filtered Transactions -")
            for i, t in enumerate(filtered, start=1):
                print(
                    f"{i}. {t.date} | {t.trans_type.title():7} | {t.amount:8.2f} | "
                    f"{t.category:12} | {t.notes}"
                )

    def view_summary(self):
        income = sum(t.amount for t in self.transactions if t.trans_type == 'income')
        expense = sum(t.amount for t in self.transactions if t.trans_type == 'expense')
        net = income - expense
        print("\n- Summary -")
        print(f"Total Income : {income:.2f}")
        print(f"Total Expense: {expense:.2f}")
        print(f"Net Balance  : {net:.2f}")

    def save_transactions(self):
        try:
            with open(self.filename, 'w', encoding='utf-8') as f:
                for t in self.transactions:
                    f.write(t.to_line() + '\n')
            print("Transactions saved.")
        except Exception as e:
            print(f"Error saving transactions: {e}")

    def load_transactions(self):
        if not os.path.exists(self.filename):
            return
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                for line in f:
                    if line.strip() == '':
                        continue
                    try:
                        t = Transaction.from_line(line)
                        self.transactions.append(t)
                    except Exception as e:
                        print(f"Skipping malformed transaction: {line.strip()}")
        except Exception as e:
            print(f"Error loading transactions: {e}")

#CLI menu

def main_menu():
    print("\n----- Budget Tracker Menu -----")
    print("1. Add a Transaction")
    print("2. List All Transactions")
    print("3. Filter Transactions")
    print("4. View Summary")
    print("5. Save and Exit")
    print("------------------------------")

def get_amount_input():
    while True:
        amt = input("Amount: ")
        try:
            value = float(amt)
            if value <= 0:
                print("Amount must be positive!")
                continue
            return value
        except ValueError:
            print("Invalid number. Enter a valid amount.")

def main():
    tracker = BudgetTracker()
    while True:
        main_menu()
        choice = input("Select an option (1-5): ").strip()
        if choice == '1':
            ttype = ""
            while ttype not in ['income', 'expense']:
                ttype = input("Type (income/expense): ").strip().lower()
                if ttype not in ['income', 'expense']:
                    print("Invalid type. Please enter 'income' or 'expense'.")
            amount = get_amount_input()
            category = input("Category: ").strip()
            if not category:
                print("Category cannot be empty!")
                continue
            notes = input("Notes (optional): ").strip()
            tracker.add_transaction(ttype, amount, category, notes)
        elif choice == '2':
            tracker.list_transactions()
        elif choice == '3':
            ft = input("Filter by type? (income/expense/leave blank): ").strip().lower()
            if ft == "":
                ft = None
            elif ft not in ['income', 'expense']:
                print("Invalid type filter. Ignoring.")
                ft = None
            fc = input("Filter by category? (enter category or leave blank): ").strip()
            fc = fc if fc else None
            tracker.filter_transactions(by_type=ft, by_category=fc)
        elif choice == '4':
            tracker.view_summary()
        elif choice == '5':
            tracker.save_transactions()
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please select 1-5.")

if __name__ == "__main__":
    main()
