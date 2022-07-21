# 261 Design Project Updates

WEDNESDAY, JULY 20, 2022 - AMENA, JACQUELINE

Added:
- A new data file to test our device against (dataset_2.csv)
- Analytics Report (data_analytics.txt) that outputs our data analytics to the user (the file is overwritten every time .py file is run)

Changes:
- Made a final iteration of Python code (before design presentation)
- Wrote the output to a txt file (realized that csv had too many commas and was hard to read)
- Added code to plot the pie chart and line graphs
- Cleaned up code to make it more readable

_________________________________________________________________

MONDAY, JULY 18, 2022 - AMENA, MARIE

Added:
- Arduino code (version 1.5)

Changes:
- Fixed a few quick errors (was indexing the wrong value in the data array for % exposures)
- Added code to alert the user for long term exposures. For the scope of our project, since we can't collect data for hours, we are using a "day's" worth of data to be 5 - 10 min. Each "hour" will be 60s. So in our case, long-term exposures would be for 60s+

Left on the To-Do List:
- Write the output to a new .csv file

_________________________________________________________________

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
