from datetime import datetime
import random

def generate_random_number():
    return random.randint(10000, 99999)

random_number = generate_random_number()
log_file_name = f"timeCalc-{random_number}.log"

def log(logStr, doPrint=True):
	with open(log_file_name, 'a') as log_file:
		if (doPrint == None or doPrint == True):
			print(logStr)
		logString = logStr + "\n"
		log_file.write(logString)

log("------------------------")
while True:
    start_date = datetime(1970, 1, 1, 11, 0, 0)
    
    year = input("Year: ")
    log("Year: " + year, False)
    month = input("Month: ")
    log("Month: " + month, False)
    day = input("Day: ")
    log("Day: " + day, False)
    
    end_date = datetime(int(year), int(month), int(day), 11, 0, 0)
    time_difference = end_date - start_date
    milliseconds_difference = time_difference.total_seconds() * 1000
    
    log("------------------------")
    log(str(milliseconds_difference))
    log("------------------------")