# Bank Transaction Validator

**Project Number:** PS No. 27  
**Project Title:** Bank Transaction Validator  
**University:** Rungta International Skills University  
**School:** School of Information Technology  
**Programme:** Bachelor of Computer Application (BCA)

## Student Details

| Field | Details |
|---|---|
| Name | Suhana Raj |
| ERP ID | RU-26-00162 |
| Email | suhana.raj@rungta.org |
| Section | BCA 1B |

## 1. Project Overview

The Bank Transaction Validator reads bank transactions from a text file, checks each transaction against banking rules, updates the account balance only for valid transactions, and saves valid transactions in a separate output file.

- Opening balance: **10,000**
- Maximum transaction amount: **100,000**

## 2. Validation Rules

- Only `Deposit` and `Withdraw` transaction types are accepted.
- The amount must be a valid number and greater than zero.
- The amount must not exceed 100,000 per transaction.
- A withdrawal cannot exceed the available balance.
- Invalid transactions must not change the balance.
- Only valid transactions are saved in `valid_transactions.txt`.

## 3. Python Concepts Used

- Variables and constants
- Functions and return values
- Conditional statements
- `for` loop
- String methods and splitting
- File handling
- Exception handling using `try-except`
- Decimal arithmetic

## 4. Folder Structure

```text
Bank_Transaction_Validator/
│
├── one.py
├── transactions.txt
├── test_cases.txt
├── README.md
└── valid_transactions.txt
```

- `one.py` — Main Python program.
- `transactions.txt` — Input file read by the program.
- `test_cases.txt` — Input and expected output for all four test cases.
- `README.md` — Project documentation.
- `valid_transactions.txt` — Automatically generated file containing only valid transactions.

## 5. How to Run in Jupyter Notebook

1. Keep `one.py` and `transactions.txt` in the same folder.
2. Open Jupyter Notebook in that folder.
3. Copy the input lines for one test case from `test_cases.txt`.
4. Paste those lines into `transactions.txt` and save the file.
5. Run this command in a Jupyter cell:

```python
%run one.py
```

6. Compare the displayed output with that test case's expected output.
7. Replace `transactions.txt` with the next test case and run the command again.

**Important:** Copy only the transaction input lines. Do not copy the test-case heading or expected-output lines into `transactions.txt`.

## 6. Test Cases

| Test Case | Description | Expected Summary |
|---|---|---|
| 1 | Normal Input | Valid: 2, Invalid: 0, Final balance: 13000 |
| 2 | Boundary / Minimum Input | Valid: 1, Invalid: 0, Final balance: 0 |
| 3 | Invalid Input | Valid: 0, Invalid: 4, Final balance: 10000 |
| 4 | Different Valid Scenario | Valid: 2, Invalid: 1, Final balance: 0 |

The complete inputs and expected console outputs are provided in `test_cases.txt`.

## 7. Output File

After processing, the program creates `valid_transactions.txt`. It contains only the transactions that passed all validation checks. Invalid transactions are not written to this file.

## 8. Requirements

- Python 3
- No external Python libraries are required.

---

## Project Mentor

**Mentored by:** [Mr. Satyaprakash Sethy](https://github.com/SATYAPRAKASHSETHY)

**GitHub:** [@SATYAPRAKASHSETHY](https://github.com/SATYAPRAKASHSETHY)

**Role:** Python Mentor / Technical Guide

### My Learning Experience

I am thankful to Mr. Satyaprakash Sethy for his continuous guidance and support throughout this project. His mentoring helped me understand the problem statement, develop the program step by step, improve my Python programming logic, and learn how to handle errors and work with files.

Whenever I faced difficulties, his explanations and practical suggestions helped me understand the right approach instead of simply copying a solution. Through this project, I gained more confidence in writing, testing, debugging, and implementing Python programs.

I truly appreciate his patience, encouragement, and dedication towards helping students improve their technical skills and complete their projects successfully.

**Thank you for being a supportive mentor and guiding me throughout this learning journey!**
