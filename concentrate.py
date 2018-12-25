#!/Users/markbolding/anaconda3/bin/python
import time
import datetime

start_time = time.time()


try:
    while True:
        time.sleep(1)
        elapsed_time = time.time() - start_time
        print(time.strftime("%H:%M:%S", time.gmtime(elapsed_time)),end='\r',flush=True)
except KeyboardInterrupt:
    print(time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))



# your script
