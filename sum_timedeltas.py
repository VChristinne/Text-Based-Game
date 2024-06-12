from datetime import datetime, timedelta

timestamp1 = datetime(2024, 1, 1, 1, 0, 10, 0)
timestamp2 = datetime(2024, 1, 1, 0, 5, 0, 0)

timedelta1 = timedelta(hours=timestamp1.hour, minutes=timestamp1.minute, seconds=timestamp1.second)
timedelta2 = timedelta(hours=timestamp2.hour, minutes=timestamp2.minute, seconds=timestamp2.second)

sum_of_timedeltas = timedelta1 + timedelta2

print(f"Soma dos tempos: {sum_of_timedeltas}")
print(f"Timestamp 1: {timestamp1}")
print(f"Timestamp 2: {timestamp2}")
