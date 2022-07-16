# 261DesignProjectPython

SATURDAY, JULY 16, 2022 - AMENA, MARLEY

A few things that will help with understanding the code better:
1. We used the csv file in the github knowing that the sampling rate is 200 ms (this is used in many time calculations)
2. For our time duration statistics (ie. avg decibels/hr, max and min/hr), we use 60s as our time duration, so the stats you see in the timeStats list are per 60s

We sat together to extract the following statistics:
- Average, maximum and minimum dB values per time duration (60 s) - these are stored and printed in "timeStats"
- Percentage during total running time of green, yellow, red and safe sound ranges
- Elapsed time for various dB ranges (ie. upto 70 dB, 70-80 dB, 80-90 dB, etc)
- Total elapsed time the device is collecting data - stored in runningTime

Next on the To-Do List:
- Test the code on a bunch of data (ideally 5 - 10 min in length with varying noises)
- Testing for long-term noise exposures!
- Write the outputs to an excel/csv file
- Maybe cleanup outputs and display them better (ie. timeStats array could be presented better, elapsed time in minutes & seconds)
