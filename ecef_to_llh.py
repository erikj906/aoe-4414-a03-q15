# script_name.py
#
# Usage: python3 script_name.py arg1 arg2 ...
#  Text explaining script usage
# Parameters:
#  arg1: description of argument 1
#  arg2: description of argument 2
#  ...
# Output:
#  A description of the script output
#
# Written by Erik Judy
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
# e.g., import math # math module
import sys
import math
# "constants"
# e.g., R_E_KM = 6378.137
R_E_KM = 6378.137
E_E    = 0.081819221456
# helper functions

## function description
# def calc_something(param1, param2):
#   pass
def calc_denom(ecc,lat_rad):
    return math.sqrt(1.0-ecc**2.0*math.sin(lat_rad)**2.0)

# initialize script arguments
r_x_km=float('nan')
r_y_km=float('nan')
r_z_km=float('nan')

# parse script arguments
if len(sys.argv)==4:
    r_x_km = float(sys.argv[1])
    r_y_km = float(sys.argv[2])
    r_z_km = float(sys.argv[2])
else:
   print(\
    'Usage: '\
    'python3 ecef_to_llh.py r_x_km r_y_km r_z_km'\
   )
   exit()

lat_rad=math.asin(r_z_km/math.sqrt(r_x_km**2+r_y_km**2+r_z_km**2))
r_lon_km=math.sqrt((r_x_km**2+r_y_km**2))
prev_lat=float('nan')
count=0
while (math.isnan(prev_lat) or abs(lat_rad-prev_lat_rad)>10e-12) and count<5:
    denom = calc_denom(E_E, lat_rad)
    c_e = R_E_KM/denom
    s_e = R_E_KM*(1-E_E**2)/denom
    prev_lat_rad = lat_rad
    lat_rad = mat.atan((r_z_km*c_e*E_E*E_E*math.sin(lat_rad))/r_lon_km)

hae_km = r_lon_km/math.cos(lat_rad)-c_E

print(lon_deg)
print(lat_rad*180.0/math.pi)
print(hae_km)
