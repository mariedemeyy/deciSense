import csv
import numpy as np

data = []
with open('classvolume.csv') as file:
    r = csv.reader(file, delimiter=',')
    for row in r:
        data.append([str(x) for x in row])

# subtractig 2 from len(data) since first 2 lines are titles, dividing by 3 since the bulk of the data is divided into 3 classes
classCount = int(((len(data) - 2)/3))

print(data[0])  # scrap this
print(data[1])  # scrap this
print(data[2])  # first timestamp
print(data[3])  # first amplitude
print(data[4])  # first db value
print(data[5])  # second timstamp, etc etc

decibels = []  # ADD DECIBELS TO THIS ARRAY TO MAKE PARSING EASIER
decibelCount = 0  # total decibel sum for time duration
maxVal = 0
minVal = 100
count = 0  # used for average calculations (dividing by # of db values)
totalTime = 0  # what we use to iterate (for specific time durations)
# this is the array used to initialize the avg, max and min db values per time duration
timeStats = [[] for k in range(int(classCount/300))]
statsCounter = 0
greenTime = 0
yellowTime = 0
safeTime = 0
redTime = 0
runningTime = 0  # total operating time
upToSeventy = 0  # used to find total time for each decibel range
seventyToEighty = 0
eightyToNinety = 0
ninetyToHundred = 0
moreThanHundred = 0

for i in range(classCount):
    # FINDING THE GREEN, YELLOW AND RED % VALUES FOR ALL TIME

    if 80 <= float(''.join(data[3*i + 3])) > 85:
        greenTime = greenTime + 0.2
    elif 85 <= float(''.join(data[3*i + 3])) > 95:
        yellowTime = yellowTime + 0.2
    elif float(''.join(data[3*i + 3])) >= 95:
        redTime = redTime + 0.2
    elif float(''.join(data[3*i + 3])) < 80:
        safeTime = safeTime + 0.2

    # FINDING THE TIME DURATION OF EACH DECIBEL RANGE FOR ALL TIME
    if float(''.join(data[3*i + 3])) < 70:
        upToSeventy = upToSeventy + 0.2

    elif 70 <= float(''.join(data[3*i + 3])) < 80:
        seventyToEighty = seventyToEighty + 0.2

    elif 80 <= float(''.join(data[3*i + 3])) < 90:
        eightyToNinety = eightyToNinety + 0.2

    elif 90 <= float(''.join(data[3*i + 3])) < 100:
        ninetyToHundred = ninetyToHundred + 0.2

    elif float(''.join(data[3*i + 3])) >= 100:
        moreThanHundred = moreThanHundred + 0.2

    # FINDING AVERAGE, MAX AND MIN DECIBEL VALUES FOR EACH SET TIME DURATION (60s)
    if totalTime >= 60:
        timeStats[statsCounter].append(
            [int((decibelCount/300)), int(maxVal), int(minVal)])
        statsCounter = statsCounter + 1

        maxVal = 0
        minVal = 100
        decibelCount = 0
        totalTime = 0

    else:  # keep running if we havent reached 60s yet
        if float(''.join(data[3*i + 3])) > maxVal:
            maxVal = float(''.join(data[3*i + 4]))

        elif float(''.join(data[3*i + 3])) < minVal:
            minVal = float(''.join(data[3*i + 4]))

    # parsing every 3rd value starting from the 4th element in list
        decibelCount = decibelCount + float(''.join(data[3*i + 4]))
        count = count + 1
        totalTime = totalTime + 0.2
        runningTime = runningTime + 0.2

print("The count is", count)
print("The average decibel value is", int(decibelCount/count))
print("The max decibel value is", maxVal)
print("The min decibel value is", minVal)
print(timeStats)
print("")
print("The percentage of time in the green zone is",
      (100*int((greenTime)/runningTime)), "%")
print("The percentage of time in the yellow zone is",
      (100*int((yellowTime)/runningTime)), "%")
print("The percentage of time in the red zone is",
      (100*int((redTime)/runningTime)), "%")
print("The percentage of unharmful hearing is",
      (100*int((safeTime)/runningTime)), "%")
print("")
print("The time spent in the range up to 70 dB is", int(upToSeventy), "s")
print("The time spent in the 70 - 80 dB range is", int(seventyToEighty), "s")
print("The time spent in the 80 - 90 dB range is", int(eightyToNinety), "s")
print("The time spent in the 90 - 100 dB range is", int(ninetyToHundred), "s")
print("The time spent in the 100 dB + range is", int(moreThanHundred), "s")

# green 80 - 84
# yellow 85 - 94
# red 95+

# NEED TO PARSE:
# 1. Average db per hour duration (use the timestamp for displays stats per hour, day etc)
# 2. Max and min db values per time duration
# 3. Percentages of time duration composed of green, yellow and red-level sound exposures (pie chat - percentages)
# 4. Find the time per decibel value (or maybe easier, find the total time per range ie. time for 70-80 db, 80-90 db etc) - sampling rate is 200 ms
# 5. Elapsed time


# decibels = []
# i = 4
# while i < len(data):
# print(data[i])
# intDecibel = int(data[i])
# print(intDecibel)
# decibels.append(int(data[i]))
# i += 3

# for element in decibels:
# print(element)
