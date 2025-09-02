---

# 🏦 Bank Management System (OOP in Python)

This project is a simple **Object-Oriented Programming (OOP)** implementation of a basic **banking system** in Python.

It demonstrates how to use **classes, inheritance, and methods** to manage bank accounts such as **Saving Accounts** and **Checking Accounts**.

---

## 📌 Features

* Create accounts with account number, holder name, balance, and type.
* Deposit money into an account.
* Withdraw money with rules for savings vs. checking accounts.
* Transfer money between accounts.
* Check account details (number, holder name, type, and balance).

---

## 🛠️ Classes Overview

### `Account`

Base class for all account types.

**Attributes**:

* `account_number` – Unique identifier for the account.
* `holder_name` – Name of the account holder.
* `balance` – Current balance in the account.
* `type` – Account type (`SavingAccount` or `CheckingAccount`).
* `counter` – Tracks number of withdrawals (for savings accounts).

**Methods**:

* `deposit(amount)` – Add money to account.
* `withdraw(amount)` – Withdraw money:

  * Savings accounts have a **10-withdrawal limit**.
  * Checking accounts can withdraw without limit (but must have balance).
* `transfer(receiver, amount)` – Transfer funds between accounts.
* `check_balance()` – Returns account details as a dictionary.

---

### `savingAccount`

* Inherits from `Account`.
* Adds **withdrawal limit** (max 10 times).

### `CheckingAccount`

* Inherits from `Account`.
* No withdrawal limit (but requires positive balance).

---

## 🚀 Example Usage

```python
# Create accounts
Account1 = savingAccount(100, "Ahmed", 200, "SavingAccount")
Account2 = savingAccount(200, "Ali", 4000, "SavingAccount")

# Transfer money
Account1.transfer(Account2, 200)

# Print balances
print(Account1.balance)  # 0
print(Account2.balance)  # 4200
```

---

## 📂 Project Structure

```
Bank pro-OOP.py   # Main Python script with classes and usage example
README.md         # Project documentation
```

---
