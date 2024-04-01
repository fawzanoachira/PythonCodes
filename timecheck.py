import datetime
import time

now = datetime.datetime.now()
sleep_start = datetime.datetime(now.year, now.month, now.day, 10, 0)  # 10 am
sleep_end = datetime.datetime(now.year, now.month, now.day, 15, 15)   # 4 pm

print(now)
print(sleep_start)
print(sleep_end)

print((sleep_end - now).seconds)

if(sleep_start <= now <= sleep_end):
    print("Sleeping")
    time.sleep((sleep_end - now).seconds)
    print("Woke")