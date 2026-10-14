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
  with open(FILE_NAME,"r",new_line=""























  
      
