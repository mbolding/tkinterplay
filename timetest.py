import time
import datetime

now = datetime.datetime.now()


try:
    while True:
        time.sleep(1)
        now = datetime.datetime.now()
        print(now.strftime("%H:%M"))
except KeyboardInterrupt:
    pass
