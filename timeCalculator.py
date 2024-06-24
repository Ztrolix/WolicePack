from datetime import datetime

print("------------------------")
while True:
	start_date = datetime(1970, 1, 1, 11, 0, 0)
	
	year = input("Year: ")
	month = input("Month: ")
	day = input("Day: ")

	end_date = datetime(int(year), int(month), int(day), 11, 0, 0)
	time_difference = end_date - start_date
	milliseconds_difference = time_difference.total_seconds() * 1000
	milliseconds_difference

	print("------------------------")
	print(milliseconds_difference)
	print("------------------------")