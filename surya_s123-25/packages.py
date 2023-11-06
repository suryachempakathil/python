import statistics
import math
import time
print("the value of pi",math.pi)
seconds=time.time()
print("second since epoch(the point where time begins)=",seconds)
li=[1,2,3,3,2,2,2]
print("the average of list value is:",end=" ")
print(statistics.mean(li))
local_time=time.ctime(seconds)
print("local time:",local_time)
