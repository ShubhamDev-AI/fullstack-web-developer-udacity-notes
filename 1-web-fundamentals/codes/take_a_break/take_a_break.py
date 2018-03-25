import webbrowser
import datetime
import time

SECONDS_PER_HOUR = 60 * 60
DEFAULT_BREAK_TIME = 2 * 5

print("This program started in {}".format(time.ctime()))
print("Waiting for {} seconds to remind a break".format(DEFAULT_BREAK_TIME))

break_count = 0
while break_count < 3:
    time.sleep(DEFAULT_BREAK_TIME)
    webbrowser.open("http://example.com")
    print("It's time to take a break")
    break_count += 1
