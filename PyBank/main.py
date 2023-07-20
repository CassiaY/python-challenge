import os
import csv
import pandas as pd
from pathlib import Path

csv_path = os.path.join("PyBank", "Resources", "budget_data.csv")
with open(csv_path) as csv_file:
    csvreader=csv.reader(csv_file, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    months = len(list(csvreader))

pd_path = Path("PyBank/Resources/budget_data.csv")
bank_df=pd.read_csv(pd_path)

#Calculations:
net = bank_df["Profit/Losses"].sum()

#changes_df = bank_df["Profit/Losses"].diff()
#change = changes_df.iloc[:,0].sum()/(months-1)
#Returns pandas.errors.IndexingError: Too many indexers

inc = bank_df["Profit/Losses"].max()
inc_mo = "month"  #ran out of time to figure this out
dec = bank_df["Profit/Losses"].min()
dec_mo = "month"  #ran out of time to figure this out

#printing results in the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {months}")
print(f"Total:  ${net}")
#print(f"Average Change:  ${change}")
print(f"Greatest Increase in Profits:  {inc_mo} (${inc})")
print(f"Greatest Decrease in Profits:  {dec_mo} (${dec})")

#Exporting results to a text file:
output_path = os.path.join("PyBank/analysis/PyBank_output.txt")
with open(output_path, 'w') as text:
    text.write("Financial Analysis\n")
    text.write("----------------------------\n")
    text.write(f"Total Months:  {months}\n")
    text.write(f"Total:  ${net}\n")
    #text.write(f"Average Change:  ${change}\n")
    text.write(f"Greatest Increase in Profits:  {inc_mo} (${inc})\n")
    text.write(f"Greatest Decrease in Profits:  {dec_mo} (${dec})\n")
