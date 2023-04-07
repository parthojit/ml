import matplotlib.pyplot as plt
import numpy as np

TIME_STEP = 0.1
HOUR = 24
MIN = 60
# SEC = 60
SEC = 1
STEPS = 1/TIME_STEP

SIZE = int(STEPS*SEC*MIN*HOUR)

print(SIZE)

solar_cell_current = np.zeros((SIZE))
solar_cell_current[0:int(SIZE/HOUR)] = 1
print(solar_cell_current)

SET = 1
for i in range(0,24):
    solar_cell_current[int(SIZE/HOUR)*i:int(SIZE/HOUR)*(i+1)] = SET
    
    if i<11:
        SET+=1
    else:
        SET-=1
plt.plot(solar_cell_current)
plt.show()


