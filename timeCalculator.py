from datetime import datetime

start_date = datetime(1970, 1, 1, 11, 0, 0)
end_date = datetime(2024, 6, 16, 11, 0, 0)
time_difference = end_date - start_date
milliseconds_difference = time_difference.total_seconds() * 1000
milliseconds_difference

print(milliseconds_difference)