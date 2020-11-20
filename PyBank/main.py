# specify the column header row and the item delimiter
import csv

# load file and output it
file_to_load = "Resources/budget_data.csv"
file_to_output = "analysis/budget_analysis_1.txt"

# monitor revenues
total_months = 0
prev_revenue = 0
month_of_change = []
revenue_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_revenue = 0

# convert csv into a list of dictionaries
with open(file_to_load) as revenue_data:
    reader = csv.DictReader(revenue_data)

    for row in reader:

        # monitor change in total
        total_months = total_months + 1
        total_revenue = total_revenue + int(row["Profit/Losses"])

        # monitor change in revenue
        revenue_change = int(row["Profit/Losses"]) - prev_revenue
        prev_revenue = int(row["Profit/Losses"])
        revenue_change_list = revenue_change_list + [revenue_change]
        month_of_change = month_of_change + [row["Date"]]

        # determine the highest increase
        if (revenue_change > greatest_increase[1]):
            greatest_increase[0] = row["Date"]
            greatest_increase[1] = revenue_change

        # determine the highest decrease
        if (revenue_change < greatest_decrease[1]):
            greatest_decrease[0] = row["Date"]
            greatest_decrease[1] = revenue_change

# determine the Average change in Revenue 
revenue_change_list.pop(0)
revenue_avg = sum(revenue_change_list) / len(revenue_change_list)

# sumarize the output
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total Revenue: ${total_revenue}\n"
    f"Average Revenue Change: ${revenue_avg}\n"
    f"Greatest Increase in Revenue: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Revenue: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# Print the output 
print(output)

# Export the results 
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
