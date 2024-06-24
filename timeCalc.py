from datetime import datetime as date
import random as rand
import os

randNum = rand.randint(10000, 99999)
if not os.path.exists('logs'):
    os.mkdir('logs')

logLocation = f"logs/timeCalc-{randNum}.log"
def log(logStr, doPrint=True, logFile=logLocation):
	with open(logFile, 'a') as log_file:
		if doPrint == True:
			print(logStr)
		logString = logStr + "\n"
		log_file.write(logString)

def isInt(value):
    try:
        int(value)
        return True
    except ValueError:
        log("------------------------")
        log("ERROR: Value is String")
        log("------------------------")
        return False

log("------------------------")
while True:
    start_date = date(1970, 1, 1, 11, 0, 0)
    
    year = input("Year: ")
    log("Year: " + year, False)
    month = input("Month: ")
    log("Month: " + month, False)
    day = input("Day: ")
    log("Day: " + day, False)

    if isInt(year) and isInt(month) and isInt(day):
        try:
            end_date = date(int(year), int(month), int(day), 11, 0, 0)
            time_difference = end_date - start_date
            milliseconds_difference = time_difference.total_seconds() * 1000

            log("------------------------")
            log(str(milliseconds_difference))
            log("------------------------")
        except ValueError:
            log("------------------------")
            log("ERROR: Not Valid Date!")
            log("------------------------")
        except:
            log("------------------------")
            log("ERROR: Something went wrong!")
            log("------------------------")