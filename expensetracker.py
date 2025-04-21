import json
import datetime
import os

# Define a unique function to generate a report ID
def generate_report_id(timestamp):
    """Generates a unique report ID based on the timestamp."""
    return "RPT-" + timestamp.strftime("%Y%m%d-%H%M%S")

# Main function to handle expense tracking
def track_expenses():
    """
    This function allows users to input, store, analyze, and view their expenses.
    It incorporates error handling, data persistence, and generates unique report IDs.
    """

    # 1. User Input and Data Management [cite: 8, 15]
    def get_expense_input():
        """Gets expense details from the user."""
        amount = 0
        while True:
            try:
                amount = float(input("Enter expense amount: "))
                if amount <= 0:
                    print("Amount must be positive.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")

        description = input("Enter expense description: ")
        category = get_category_input()  # Use the category input function
        return {"amount": amount, "description": description, "category": category}

    # 2. Expense Categories [cite: 10, 17]
    def get_category_input():
        """Gets the expense category from the user with options."""
        categories = ["Food", "Transportation", "Entertainment", "Utilities", "Other"]
        print("Select a category:")
        for i, category in enumerate(categories):
            print(f"{i + 1}. {category}")

        while True:
            try:
                choice = int(input("Enter category number: "))
                if 1 <= choice <= len(categories):
                    return categories[choice - 1]
                else:
                    print("Invalid category number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    # 3. Data Storage [cite: 9, 16]
    def save_expense(expense):
        """Saves expense data to a JSON file."""
        filename = "expenses.json"
        expenses = []
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                try:
                    expenses = json.load(f)
                except json.JSONDecodeError:
                    expenses = []  # Handle empty or corrupted JSON file
        expenses.append(expense)
        with open(filename, 'w') as f:
            json.dump(expenses, f, indent=4)
        print("Expense saved.")

    # 4. Data Analysis [cite: 11, 18]
    def analyze_expenses():
        """Analyzes and displays expense data (monthly summary and category-wise)."""
        filename = "expenses.json"
        if not os.path.exists(filename):
            print("No expense data available.")
            return

        with open(filename, 'r') as f:
            try:
                expenses = json.load(f)
            except json.JSONDecodeError:
                print("Error reading expense data.")
                return

        # Monthly Summary
        print("\n--- Monthly Expense Summary ---")
        monthly_total = {}
        for expense in expenses:
            # Assuming expenses are stored without date, we'll analyze all as one period.
            # For a real app, you'd likely store with dates and filter.
            month = "All Time"  # Replace with actual month extraction if you store dates
            monthly_total[month] = monthly_total.get(month, 0) + expense["amount"]
        for month, total in monthly_total.items():
            print(f"{month}: {total}")

        # Category-wise Expenditure
        print("\n--- Category-wise Expenditure ---")
        category_totals = {}
        for expense in expenses:
            category = expense["category"]
            category_totals[category] = category_totals.get(category, 0) + expense["amount"]
        for category, total in category_totals.items():
            print(f"{category}: {total}")
        
        # Generate and display report ID
        report_id = generate_report_id(datetime.datetime.now())
        print(f"\nReport ID: {report_id}")  # Display the unique report ID

    # 5. User Interface [cite: 12, 19]
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. Analyze Expenses")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            expense = get_expense_input()
            save_expense(expense)
        elif choice == '2':
            analyze_expenses()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


# Run the expense tracker
if __name__ == "__main__":
    track_expenses()