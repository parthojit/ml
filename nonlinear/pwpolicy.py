import numpy as np
import time
import matplotlib.pyplot as plt
from solar import solar_cell_current


TIME_STEP = 0.01
i = 20
dq_gps:float = i*TIME_STEP # mAh - cost of charge for GPS transmission
time_left_gps:float = 0
# energy_cost_gps = 10
SOLAR_CELL_CHARGE = 0 # couloumbs
BATTERY_CHARGE_TOTAL = 100 # coulombs
BATTERY_CHARGE_THRESHOLD = 70
SOLAR_CELL_CURRENT_THRESHOLD = 6

total_charge:float = SOLAR_CELL_CHARGE + BATTERY_CHARGE_TOTAL # mAh
energy_left = 0
count = 0

event_counter_gps = []
event_strike_gps = []
event_time_gps = []


def pp_max_aggresive(total_charge:float,count:int,time_left_gps:float,dq_gps:float,event_time_gps:list,event_strike_gps:list):
    TIME_UNTIL_GPS_EVENT = TIME_STEP*20 # 2 seconds
    if time_left_gps-TIME_STEP<0:
        total_charge = total_charge - dq_gps
        time_left_gps = TIME_UNTIL_GPS_EVENT
        event_strike_gps.append(1)
        event_time_gps.append(TIME_STEP*count)
        event_counter_gps.append(time_left_gps)
        print("********* GPS Transmission has occurred *********")
        time.sleep(TIME_STEP)

    else:
        time_left_gps = time_left_gps-TIME_STEP
        event_strike_gps.append(0)
        event_time_gps.append(TIME_STEP*count)
        event_counter_gps.append(time_left_gps)
        time.sleep(TIME_STEP)

    print("GPS TIME LEFT UNTIL NEXT EVENT = %.2f" % time_left_gps)
    print("(PP: Max Aggressive) TOTAL CHARGE LEFT = %.2f" % total_charge)
    return total_charge,count+1,time_left_gps,event_time_gps,event_strike_gps

def pp_mod_aggressive(total_charge:float,count:int,time_left_gps:float,dq_gps:float,event_time_gps:list,event_strike_gps:list):
    TIME_UNTIL_GPS_EVENT = TIME_STEP*40 # 4 seconds
    if time_left_gps-TIME_STEP<0:
        total_charge = total_charge - dq_gps
        time_left_gps = TIME_UNTIL_GPS_EVENT
        event_strike_gps.append(1)
        event_time_gps.append(TIME_STEP*count)
        event_counter_gps.append(time_left_gps)
        print("********* GPS Transmission has occurred *********")
        time.sleep(TIME_STEP)

    else:
        time_left_gps = time_left_gps-TIME_STEP
        event_strike_gps.append(0)
        event_time_gps.append(TIME_STEP*count)
        event_counter_gps.append(time_left_gps)
        time.sleep(TIME_STEP)

    print("GPS TIME LEFT UNTIL NEXT EVENT = %.2f" % time_left_gps)
    print("(PP: Mod Aggressive) TOTAL CHARGE LEFT = %.2f" % total_charge)
    return total_charge,count+1,time_left_gps,event_time_gps,event_strike_gps

def pp_mod_conservative(total_charge:float,count:int,time_left_gps:float,dq_gps:float,event_time_gps:list,event_strike_gps:list):
    TIME_UNTIL_GPS_EVENT = TIME_STEP*60 # 6 seconds
    if time_left_gps-TIME_STEP<0:
        total_charge = total_charge - dq_gps
        time_left_gps = TIME_UNTIL_GPS_EVENT
        event_strike_gps.append(1)
        event_time_gps.append(TIME_STEP*count)
        event_counter_gps.append(time_left_gps)
        print("********* GPS Transmission has occurred *********")
        time.sleep(TIME_STEP)

    else:
        time_left_gps = time_left_gps-TIME_STEP
        event_strike_gps.append(0)
        event_time_gps.append(TIME_STEP*count)
        event_counter_gps.append(time_left_gps)
        time.sleep(TIME_STEP)

    print("GPS TIME LEFT UNTIL NEXT EVENT = %.2f" % time_left_gps)
    print("(PP: Mod Conservative) TOTAL CHARGE LEFT = %.2f" % total_charge)
    return total_charge,count+1,time_left_gps,event_time_gps,event_strike_gps

def pp_max_conservative(total_charge:float,count:int,time_left_gps:float,dq_gps:float,event_time_gps:list,event_strike_gps:list):
    TIME_UNTIL_GPS_EVENT = TIME_STEP*80 # 8 seconds
    if time_left_gps-TIME_STEP<0:
        total_charge = total_charge - dq_gps
        time_left_gps = TIME_UNTIL_GPS_EVENT
        event_strike_gps.append(1)
        event_time_gps.append(TIME_STEP*count)
        event_counter_gps.append(time_left_gps)
        print("********* GPS Transmission has occurred *********")
        time.sleep(TIME_STEP)

    else:
        time_left_gps = time_left_gps-TIME_STEP
        event_strike_gps.append(0)
        event_time_gps.append(TIME_STEP*count)
        event_counter_gps.append(time_left_gps)
        time.sleep(TIME_STEP)

    print("GPS TIME LEFT UNTIL NEXT EVENT = %.2f" % time_left_gps)
    print("(PP: Max Conservative) TOTAL CHARGE LEFT = %.2f" % total_charge)
    return total_charge,count+1,time_left_gps,event_time_gps,event_strike_gps

start = time.time()

while True:
    try:
        if total_charge > BATTERY_CHARGE_THRESHOLD and solar_cell_current[count] > SOLAR_CELL_CURRENT_THRESHOLD:
            total_charge,count,time_left_gps,event_time_gps,event_strike_gps = pp_max_aggresive(total_charge=total_charge,count=count,time_left_gps=time_left_gps,
            dq_gps=dq_gps,event_time_gps=event_time_gps,event_strike_gps=event_strike_gps)
        

        elif total_charge > BATTERY_CHARGE_THRESHOLD and solar_cell_current[count] < SOLAR_CELL_CURRENT_THRESHOLD:
            total_charge,count,time_left_gps,event_time_gps,event_strike_gps = pp_mod_aggressive(total_charge=total_charge,count=count,time_left_gps=time_left_gps,
            dq_gps=dq_gps,event_time_gps=event_time_gps,event_strike_gps=event_strike_gps)


        elif total_charge < BATTERY_CHARGE_THRESHOLD and solar_cell_current[count] > SOLAR_CELL_CURRENT_THRESHOLD:
            total_charge,count,time_left_gps,event_time_gps,event_strike_gps = pp_mod_conservative(total_charge=total_charge,count=count,time_left_gps=time_left_gps,
            dq_gps=dq_gps,event_time_gps=event_time_gps,event_strike_gps=event_strike_gps)


        elif total_charge < BATTERY_CHARGE_THRESHOLD and solar_cell_current[count] < SOLAR_CELL_CURRENT_THRESHOLD:
            total_charge,count,time_left_gps,event_time_gps,event_strike_gps = pp_max_conservative(total_charge=total_charge,count=count,time_left_gps=time_left_gps,
            dq_gps=dq_gps,event_time_gps=event_time_gps,event_strike_gps=event_strike_gps)

        else:
            total_charge,count,time_left_gps,event_time_gps,event_strike_gps = pp_max_aggresive(total_charge=total_charge,count=count,time_left_gps=time_left_gps,
            dq_gps=dq_gps,event_time_gps=event_time_gps,event_strike_gps=event_strike_gps)



        print("-- count : %2d" % count)
        print("-- solar cell current : %2d" % solar_cell_current[count])
        
    except KeyboardInterrupt:
        print("--  Keyboard Interrupt!")
        break

plt.plot(event_time_gps,event_strike_gps)
plt.xlabel("Event Time")
plt.ylabel("Event Strike")
plt.savefig("./powerpolicy.png",dpi=300,bbox_inches="tight")


