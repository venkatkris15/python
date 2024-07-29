import mysql.connector
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

# Establish MySQL connection
try:
    conn = mysql.connector.connect(
        user='root',
        password='2525',
        host='127.0.0.1',
        port=3306,
        database='banking_system'  # Change this to your database name
    )
    print("Connected to MySQL Server successfully!")

except mysql.connector.Error as err:
    print(f"Error: {err}")
    exit(1)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Create accounts table if not exists
try:
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS accounts (
            account_id INT AUTO_INCREMENT PRIMARY KEY,
            account_number VARCHAR(20) UNIQUE NOT NULL,
            account_name VARCHAR(100) NOT NULL,
            balance DECIMAL(15, 2) NOT NULL DEFAULT 0.00,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    print("Accounts table created successfully!")

except mysql.connector.Error as err:
    print(f"Error: {err}")

# Create transactions table if not exists
try:
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            transaction_id INT AUTO_INCREMENT PRIMARY KEY,
            account_number VARCHAR(20) NOT NULL,
            transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            description VARCHAR(255),
            amount DECIMAL(15, 2),
            balance DECIMAL(15, 2),
            FOREIGN KEY (account_number) REFERENCES accounts(account_number)
        )
    """)
    print("Transactions table created successfully!")

except mysql.connector.Error as err:
    print(f"Error: {err}")

# Function to create a new account
def create_account(account_number, account_name):
    try:
        cursor.execute("""
            INSERT INTO accounts (account_number, account_name, balance)
            VALUES (%s, %s, 0.00)
        """, (account_number, account_name))
        conn.commit()
        print(f"Account '{account_number}' created successfully!")

    except mysql.connector.Error as err:
        conn.rollback()
        print(f"Error: {err}")

# Function to update balance
def update_balance(account_number, amount):
    try:
        cursor.execute("""
            UPDATE accounts
            SET balance = balance + %s
            WHERE account_number = %s
        """, (amount, account_number))
        conn.commit()

    except mysql.connector.Error as err:
        conn.rollback()
        print(f"Error: {err}")

# Function to fetch balance
def get_balance(account_number):
    try:
        cursor.execute("""
            SELECT balance FROM accounts
            WHERE account_number = %s
        """, (account_number,))
        result = cursor.fetchone()
        if result:
            return result[0]
        else:
            print(f"Account '{account_number}' not found.")
            return None

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Function to fetch account statement
def get_account_statement(account_number):
    try:
        cursor.execute("""
            SELECT transaction_date, description, amount, balance
            FROM transactions
            WHERE account_number = %s
            ORDER BY transaction_date
        """, (account_number,))
        statement = cursor.fetchall()
        return statement

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def download_statement_as_pdf(account_number, statement):
    pdf_filename = f"account_statement_{account_number}.pdf"
    c = canvas.Canvas(pdf_filename, pagesize=letter)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, 750, f"Account Statement for Account Number: {account_number}")
    c.setFont("Helvetica", 12)
    
    # Set initial y-coordinate for the statement entries
    y = 700
    
    for transaction in statement:
        transaction_date, description, amount, balance = transaction
        c.drawString(100, y, f"Date: {transaction_date}")
        c.drawString(250, y, f"Description: {description}")
        c.drawString(450, y, f"Amount: ₹{amount:.2f}")
        c.drawString(600, y, f"Balance: ₹{balance:.2f}")
        y -= 20
    
    c.save()
    print(f"PDF generated: {pdf_filename}")

# Function to add transaction
def add_transaction(account_number, description, amount, balance):
    try:
        cursor.execute("""
            INSERT INTO transactions (account_number, description, amount, balance)
            VALUES (%s, %s, %s, %s)
        """, (account_number, description, amount, balance))
        conn.commit()
        print("Transaction recorded successfully!")

    except mysql.connector.Error as err:
        conn.rollback()
        print(f"Error: {err}")

# Function to fetch account holders list
def get_account_holders():
    try:
        cursor.execute("""
            SELECT account_number, account_name, balance
            FROM accounts
        """)
        account_holders = cursor.fetchall()
        return account_holders

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Function to download account holders list as PDF
def download_account_holders_as_pdf(account_holders):
    pdf_filename = "account_holders_list.pdf"
    c = canvas.Canvas(pdf_filename, pagesize=letter)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, 750, "Account Holders List")
    c.setFont("Helvetica", 12)
    
    # Set initial y-coordinate for the account holders entries
    y = 700
    
    for account in account_holders:
        account_number, account_name, balance = account
        c.drawString(100, y, f"Account Number: {account_number}")
        c.drawString(300, y, f"Account Name: {account_name}")
        c.drawString(500, y, f"Balance: ₹{balance:.2f}")
        y -= 20
    
    c.save()
    print(f"PDF generated: {pdf_filename}")

# Close cursor and connection
def close_connection():
    cursor.close()
    conn.close()
    print("MySQL connection closed.")

# Main banking program
def main():
    is_running = True

    while is_running:
        print("********************")
        print("      Banking program      ")
        print("********************")
        print("1. Create Account")
        print("2. Show Balance")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Display Account Statement")
        print("6. Show Account Holders List")
        print("7. Exit")
        print("********************")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            account_number = input("Enter account number: ")
            account_name = input("Enter account name: ")
            create_account(account_number, account_name)

        elif choice == '2':
            account_number = input("Enter account number: ")
            balance = get_balance(account_number)
            if balance is not None:
                print(f"Balance for account '{account_number}' is ₹{balance:.2f}")

        elif choice == '3':
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to deposit: "))
            update_balance(account_number, amount)
            add_transaction(account_number, "Deposit", amount, get_balance(account_number))

        elif choice == '4':
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to withdraw: "))
            update_balance(account_number, -amount)
            add_transaction(account_number, "Withdrawal", -amount, get_balance(account_number))

        elif choice == '5':
            account_number = input("Enter account number: ")
            statement = get_account_statement(account_number)
            if statement:
                print("********************")
                print(f"Account Statement for '{account_number}':")
                print("********************")
                for transaction in statement:
                    transaction_date, description, amount, balance = transaction
                    print(f"Date: {transaction_date}, Description: {description}, Amount: ₹{amount:.2f}, Balance: ₹{balance:.2f}")
                
                # Ask user if they want to download as PDF
                download_choice = input("Do you want to download this statement as PDF? (yes/no): ").lower()
                if download_choice == 'yes':
                    download_statement_as_pdf(account_number, statement)
            else:
                print(f"No account statement found for '{account_number}'.")

        elif choice == '6':
            account_holders = get_account_holders()
            if account_holders:
                print("********************")
                print("Account Holders List:")
                print("********************")
                for account in account_holders:
                    account_number, account_name, balance = account
                    print(f"Account Number: {account_number}, Account Name: {account_name}, Balance: ₹{balance:.2f}")
                
                # Ask user if they want to download as PDF
                download_choice = input("Do you want to download the account holders list as PDF? (yes/no): ").lower()
                if download_choice == 'yes':
                    download_account_holders_as_pdf(account_holders)
            else:
                print("No account holders found.")

        elif choice == '7':
            is_running = False

        else:
            print("********************")
            print("That is not a valid choice")
            print("********************")

    close_connection()
    print("Thank you! Have a nice day!")

if __name__ == '__main__':
    main()
