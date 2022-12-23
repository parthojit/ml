import numpy as np
import time
import matplotlib.pyplot as plt


TIME_STEP = 0.1
i = 20
dq_gps = i*TIME_STEP
time_left_gps = 0
# energy_cost_gps = 10
SOLAR_CELL_CHARGE = 100 # couloumbs
BATTERY_CHARGE = 50 # coulombs
TIME_UNTIL_GPS_EVENT = TIME_STEP*200 # 20 seconds

total_charge = SOLAR_CELL_CHARGE + BATTERY_CHARGE
energy_left = 0
count = 0

event_counter_gps = []
event_strike_gps = []
event_time_gps = []


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
        if time_left_gps-TIME_STEP<0:
            total_charge = total_charge - dq_gps
            time_left_gps = TIME_UNTIL_GPS_EVENT
            event_strike_gps.append(1)
            event_time_gps.append(TIME_STEP*count)
            event_counter_gps.append(time_left_gps)
            print("********* GPS Transmission has occurred *********")
            time.sleep(TIME_STEP/10000)

        else:
            time_left_gps = time_left_gps-TIME_STEP
            event_strike_gps.append(0)
            event_time_gps.append(TIME_STEP*count)
            event_counter_gps.append(time_left_gps)
            time.sleep(TIME_STEP/10000)

        print("GPS TIME LEFT UNTIL NEXT EVENT = %.2f" % time_left_gps)
        print("TOTAL CHARGE LEFT = %.2f" % total_charge)
        
    except KeyboardInterrupt:
        print("--  Keyboard Interrupt!")
        break

plt.plot(event_time_gps,event_strike_gps)
plt.xlabel("Event Time")
plt.ylabel("Event Strike")
plt.show()


