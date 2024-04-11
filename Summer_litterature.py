book_sheets = int(input())
sheets_per_hour = int(input())
days_needed = int(input())

total_hours = book_sheets / sheets_per_hour
hours_needed = total_hours / days_needed

print (int(hours_needed))

