# ============================================================
# RUNGTA INTERNATIONAL SKILLS UNIVERSITY
# SCHOOL OF INFORMATION TECHNOLOGY
# BACHELOR OF COMPUTER APPLICATION (BCA)
#
# PROJECT TITLE : Bank Transaction Validator
# PROJECT NUMBER: PS No. 27
#
# STUDENT DETAILS
# ------------------------------------------------------------
# Name          : Suhana Raj
# ERP ID        : RU-26-00162
# Email         : suhana.raj@rungta.org
# Section       : BCA 1B
#
# PROJECT DESCRIPTION
# ------------------------------------------------------------
# Read bank transactions from a text file, validate each
# transaction, update the balance only for valid transactions,
# and save valid transactions in a separate output file.
#
# Opening balance: 10,000
# Maximum transaction amount: 100,000
#
# Python concepts: Functions, Conditions, Loops, Decimal
# Arithmetic, Exception Handling and File Handling.
# ============================================================

from decimal import Decimal, InvalidOperation


# ------------------------------------------------------------
# 1. CONSTANTS
# ------------------------------------------------------------

OPENING_BALANCE = Decimal("10000")
MAX_TRANSACTION_AMOUNT = Decimal("100000")

INPUT_FILE = "transactions.txt"
OUTPUT_FILE = "valid_transactions.txt"


# ------------------------------------------------------------
# 2. FORMAT AMOUNT FOR DISPLAY
# ------------------------------------------------------------

def format_amount(amount):
    """Remove unnecessary decimal zeros from an amount."""
    return f"{amount.normalize():f}"


# ------------------------------------------------------------
# 3. VALIDATE ONE TRANSACTION
# ------------------------------------------------------------

def validate_transaction(transaction_type, amount_text, balance):
    """
    Check the transaction against all banking rules.

    Return:
        (True, "", updated_balance) for a valid transaction.
        (False, reason, original_balance) for an invalid one.
    """

    # Remove extra spaces from the transaction details.
    transaction_type = transaction_type.strip()
    amount_text = amount_text.strip()

    # Convert the amount into Decimal for accurate calculations.
    try:
        amount = Decimal(amount_text)

        # Reject special values such as NaN and Infinity.
        if not amount.is_finite():
            raise InvalidOperation

    except (InvalidOperation, ValueError):
        return False, f"amount '{amount_text}' is not a number.", balance

    # Only Deposit and Withdraw transactions are accepted.
    if transaction_type not in ("Deposit", "Withdraw"):
        return False, f"unknown type '{transaction_type}'.", balance

    # Transaction amount must be positive.
    if amount <= 0:
        return False, "amount must be positive.", balance

    # Transaction amount must not exceed 100000.
    if amount > MAX_TRANSACTION_AMOUNT:
        return False, "exceeds limit of 100000.", balance

    # Withdrawal must not exceed the available balance.
    if transaction_type == "Withdraw" and amount > balance:
        return False, "insufficient balance.", balance

    # Update the balance only after every validation succeeds.
    if transaction_type == "Deposit":
        balance += amount
    else:
        balance -= amount

    return True, "", balance


# ------------------------------------------------------------
# 4. PROCESS TRANSACTIONS FROM THE INPUT FILE
# ------------------------------------------------------------

def process_transactions(input_file=INPUT_FILE, output_file=OUTPUT_FILE):
    """Read, validate, display and save bank transactions."""

    # Set the opening balance and transaction counters.
    balance = OPENING_BALANCE
    valid_count = 0
    invalid_count = 0

    # Store valid transaction lines for the output file.
    valid_transactions = []

    # Read all transaction lines from the input file.
    try:
        with open(input_file, "r", encoding="utf-8") as file:
            transactions = file.readlines()

    # Handle a missing input file.
    except FileNotFoundError:
        print(f"Error: '{input_file}' file not found.")
        return

    # Handle other file-reading errors.
    except OSError as error:
        print(f"Error: Unable to read '{input_file}': {error}")
        return

    # Process each transaction in its original line order.
    for line_number, line in enumerate(transactions, start=1):

        # Remove surrounding spaces and newline characters.
        line = line.strip()

        # Skip blank lines.
        if not line:
            continue

        # Split the line into transaction type and amount.
        parts = line.split(",", 1)

        # Reject a line that does not follow Type,Amount format.
        if len(parts) != 2:
            invalid_count += 1
            print(
                f"Line {line_number}: Invalid – "
                "transaction must be in Type,Amount format."
            )
            continue

        transaction_type, amount_text = parts

        # Validate the transaction without changing balance
        # unless all validation rules are satisfied.
        is_valid, message, updated_balance = validate_transaction(
            transaction_type,
            amount_text,
            balance
        )

        if is_valid:
            # Commit the updated balance for a valid transaction.
            balance = updated_balance
            valid_count += 1

            # Keep the valid transaction for the output file.
            valid_transactions.append(line)

            print(
                f"Line {line_number}: Valid | "
                f"Balance: {format_amount(balance)}"
            )

        else:
            # Invalid transactions do not affect the balance.
            invalid_count += 1
            print(f"Line {line_number}: Invalid – {message}")

    # Save only valid transactions to the output file.
    try:
        with open(output_file, "w", encoding="utf-8") as file:
            for transaction in valid_transactions:
                file.write(transaction + "\n")

    # Report an error if the output file cannot be written.
    except OSError as error:
        print(f"Error: Unable to save '{output_file}': {error}")
        return

    # Display the final counts and account balance.
    print(
        f"Valid: {valid_count} | "
        f"Invalid: {invalid_count} | "
        f"Final balance: {format_amount(balance)}"
    )


# ------------------------------------------------------------
# 5. MAIN PROGRAM
# ------------------------------------------------------------

# Run the program only when this file is executed directly.
if __name__ == "__main__":
    process_transactions()
