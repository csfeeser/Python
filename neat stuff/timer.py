import datetime
import time

def countdown(stop):
    while True:
        difference = stop - datetime.datetime.now()
        count_hours, rem = divmod(difference.seconds, 3600)
        count_minutes, count_seconds = divmod(rem, 60)
        if difference.days == 0 and count_hours == 0 and count_minutes == 0 and count_seconds == 0:
            print("Time's up Let's continue!")
            break
        display= f"Lunch Time Remaining: {count_hours} hour(s), {count_minutes} minutes, {count_seconds} second(s)."
        print(f'╭────────────────────────────────────────────────────────────────────────────╮')
        print(f'│ {display:74} │')
        print(f'╰────────────────────────────────────────────────────────────────────────────╯')
        print('\033[3A\033[2K', end='')
        time.sleep(1)


end_time = datetime.datetime(2023, 2, 16, 20, 30, 0)
countdown(end_time)
