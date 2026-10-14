import csv
import os
from datetime import date
FILE_NAME="expenses.csv"
def intialize_file():
  if not os.path.exists(FILE_NAME):
    with open(FILE_NAME,"w",newline="")as file:
      writer=csv.writer(file)
      writer.writerow(["Date","Category","Description","Amount"])
def add_expense():
  category=input("Enter category(Food,Travel,Shopping,etc.):").strip()
  description=input("Enter description:").strip()
  try:
    amount=float(input("Enter amount:"))
    if amount<=0:
      print("Amount must be greater than zero.")
      return 
  except ValueError:
    print("Please enter a valid number.")
    return
  with open(FILE_NAME,"a",newline="")as file:
    writer=csv.writer(file)
    writer.writerow([date.today(),category,description,amount])
  print("Expenses added successfully!")
def view_expenses():
  with open(FILE_NAME,"r",newline="")as file:
    expenses=list(csv.DictReader(file))
  if not expenses:
    print("No Expenses recorded yet.")
    return 
  print("\n--------All Expenses---------")
  for expense in expenses:
    print(f"Date:{expense['Date']}|"f"Category:{expense['Category']}|"f"Description:{expense['Description']}|"f"Amount:{float(expense['Amount']):.2f}")
def show_total():
  with open(FILE_NAME,"r",newline="")as file:
    expenses=list(csv.DictReader(file))
    total=sum(float(expense["Amount"])
    for expense in expenses)
    print(f"\n Total Expenses:{total:.2f}")
def expenses_by_category():
  category=input("Enter category to search:").strip().lower()
  with open(FILE_NAME,"r",newline="")as file:
    expenses=list(csv.DictReader(file))
    matching=[expense for expense in expenses
        if expense["Category"].strip().lower() ==category]
    if not matching:
          print("No expenses found in this category.")
          return
    total=0
    print(f"\n------{category.title()}Expenses-----")
    for expense in matching:
        amount=float(expense["Amount"])
        total+=amount
        print(f"Date:{expense['Date']}|"f"Description:{expense['Description']}|"f"Amount:{float(expense['Amount']):.2f}")
    print(f"Category Total:{total:.2f}")
def main():
  intialize_file()
  while True:
    print("\n=======PERSONAL EXPENSE TRACKER======")
    print("1.Add Expense")
    print("2.View all Expenses")
    print("3.Show Total Expenses")
    print("4.Search by Category")
    print("5.Exit")
    choice=input("choose an option(1-5):").strip()
    if choice=="1":
      add_expense()
    elif choice=="2":
      view_expenses()
    elif choice=="3":
      show_total()
    elif choice=="4":
      expenses_by_category()
    elif choice=="5":
      print("Thank you for using Expense Tracker!")
    else:
      print("Invalid choice.please enter 1-5.")
if __name__ =="__main__":
  main()





















  
      
