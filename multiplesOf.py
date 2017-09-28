# Author: Volosevic Vladislav
# Version: 1.0 Stable
# Creation date 09/28/17

total_sum = 0
for i in range(1000):
    if (i%3 == 0 or i%5 == 0):
        total_sum = total_sum+i
print(total_sum)