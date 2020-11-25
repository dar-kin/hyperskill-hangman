# put your python code here
from math import fabs

a = [int(input()) for i in range(6)]
first_time = a[0]*3600 + a[1]*60 + a[2]
second_time = a[3]*3600 + a[4]*60 + a[5]
print(int(fabs(first_time-second_time)))
