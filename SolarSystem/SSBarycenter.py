import spiceypy
import datetime
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

spiceypy.furnsh('kernels/naif0012.tls')
spiceypy.furnsh('kernels/de432s.bsp')
spiceypy.furnsh('kernels/pck00010.tpc')

barycenter = []

initial_time = datetime.datetime(year=2000, month=1, day=1, hour=0, minute=0, second=0)

delta = 9125
print(datetime.timedelta(days=delta))
end_time = initial_time + datetime.timedelta(days=delta)

# Convert the datetime objects now to strings
initial_UTC = initial_time.strftime('%Y-%m-%dT%H:%M:%S')
end_UTC = end_time.strftime('%Y-%m-%dT%H:%M:%S')

# Print the starting and end times
print('Init time in UTC: %s' % initial_UTC)
print('End time in UTC: %s\n' % end_UTC)

# Convert to Ephemeris Time (ET) using the SPICE function utc2et
initial_et = spiceypy.utc2et(initial_UTC)
end_et = spiceypy.utc2et(end_UTC)

print('Covered time interval in seconds: %s\n' % (end_et - initial_et))
# We see that 5.0012845 seconds are added in this time period (leapseconds)

# Create a numpy array that covers a time interval in delta = 1 day step
delta_time = np.linspace(initial_et, end_et, delta)

for i in delta_time:

    position, _ = spiceypy.spkgps(targ=0, et = i, ref='ECLIPJ2000', obs=10)
    barycenter.append(position)

barycenter = np.array(barycenter)

print('Position (components) of the Solar System Barycentre w.r.t the\n' \
      'centre of the Sun (at inital time): \n' \
      'X = %s km\n' \
      'Y = %s km\n' \
      'Z = %s km\n' % tuple(np.round(barycenter[0])))

# ... let's determine and print the corresponding distance using the numpy
# function linalg.norm()
print('Distance between the Solar System Barycentre w.r.t the\n' \
      'centre of the Sun (at initial time): \n' \
      'd = %s km\n' % round(np.linalg.norm(barycenter[0])))

_, radi_sun = spiceypy.bodvcd(bodyid = 10, item = 'RADII', maxn = 3)

rad_sun = radi_sun[0]

barycenter_scaled = barycenter / rad_sun

# MATPLOTLIB PLOT SETTINGS

barycenter_XY = barycenter_scaled[:, 0:2]
plt.style.use('dark_background')
FIG, AX = plt.subplots(figsize=(12,8))

sun = plt.Circle((0.0, 0.0), 1.0, color='yellow', alpha=.5)
AX.add_artist(sun)

AX.plot(barycenter_XY[:, 0], barycenter_XY[:, 1], ls = 'solid', color = 'blue')

AX.set_aspect('equal')
AX.grid(True, linestyle='dashed', alpha=0.5)
AX.set_xlim(-2, 2)
AX.set_ylim(-2, 2)

# Some labelling
AX.set_xlabel('X in Sun-Radius')
AX.set_ylabel('Y in Sun-Radius')

# Saving the figure in high quality
plt.savefig('SSB_WRT_SUN.png', dpi=300)

# End section

barycenter_scaled = np.linalg.norm(barycenter_scaled, axis = 1)

print('Computation time: %s days\n' % delta)

outside_sun = len(np.where(barycenter_scaled > 1)[0])

print("The barycenter is outside the sun: %s %%" % ((100*outside_sun)/delta))
