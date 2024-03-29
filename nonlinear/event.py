import numpy as np
import time
import matplotlib.pyplot as plt


time_step = 0.1
i = 10
dq = i*time_step
dx = 0
cx = 10
del_x = time_step*200
count=0

DX = []
EVENT = []
TIME = []


def pp_max_aggresive():
    pass

def pp_max_conservative():
    pass

def pp_mod_aggresive():
    pass

def pp_mod_conservative():
    pass

start = time.time()

while True:
    try:
        count+=1
        if dx-time_step<0:
            dq = -10
            dx = del_x
            EVENT.append(1)
            TIME.append(time_step*count)
            DX.append(dx)
            time.sleep(time_step/10000)
        else:
            dx = dx-time_step
            EVENT.append(0)
            TIME.append(time_step*count)
            DX.append(dx)
            time.sleep(time_step/10000)

        print("dx=%.2f" % dx)
        

    except KeyboardInterrupt:
        print("--  Keyboard Interrupt!")
        break

plt.plot(TIME,EVENT)
plt.ylabel("Event")
plt.show()


