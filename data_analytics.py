import csv
import matplotlib.pyplot as plt

data = []
with open('dataset_2.csv') as file:
    r = csv.reader(file, delimiter=',')
    for row in r:
        data.append([str(x) for x in row])

# subtractig 2 from len(data) since first 2 lines are titles, dividing by 3 since the bulk of the data is divided into 3 classes
classCount = int(((len(data) - 2)/3))

print(data[0])  # scrap this
print(data[1])  # first timestamp
print(data[2])  # first amplitude
print(data[3])  # first db value

decibelCount = 0  # total decibel sum for time duration
maxVal = 0
minVal = 100
count = 0  # used for average calculations (dividing by # of db values)
totalTime = 0  # what we use to iterate (for specific time durations)
# used to initialize the avg, max and min db values per time duration
timeStats = [[] for k in range(int(classCount/60))]
avgValues = []
maxValues = []
minValues = []
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
    if 80 <= float(''.join(data[3*i + 3])) < 85:
        greenTime = greenTime + 1
    elif 85 <= float(''.join(data[3*i + 3])) < 95:
        yellowTime = yellowTime + 1
    elif float(''.join(data[3*i + 3])) >= 95:
        redTime = redTime + 1
    elif float(''.join(data[3*i + 3])) < 80:
        safeTime = safeTime + 1

    # FINDING THE TIME DURATION OF EACH DECIBEL RANGE FOR ALL TIME
    if float(''.join(data[3*i + 3])) < 70:
        upToSeventy = upToSeventy + 1

    elif 70 <= float(''.join(data[3*i + 3])) < 80:
        seventyToEighty = seventyToEighty + 1

    elif 80 <= float(''.join(data[3*i + 3])) < 90:
        eightyToNinety = eightyToNinety + 1

    elif 90 <= float(''.join(data[3*i + 3])) < 100:
        ninetyToHundred = ninetyToHundred + 1

    elif float(''.join(data[3*i + 3])) >= 100:
        moreThanHundred = moreThanHundred + 1

    # FINDING AVERAGE, MAX AND MIN DECIBEL VALUES FOR EACH SET TIME DURATION (60s)
    if totalTime >= 60:
        timeStats[statsCounter].append(
            [int((decibelCount/60)), int(maxVal), int(minVal)])
        avgValues.append(int((decibelCount/60)))
        maxValues.append(int(maxVal))
        minValues.append(int(minVal))

        statsCounter = statsCounter + 1

        maxVal = 0
        minVal = 100
        decibelCount = 0
        totalTime = 0

    else:  # keep running if we havent reached 60s yet
        if float(''.join(data[3*i + 3])) > maxVal:
            maxVal = float(''.join(data[3*i + 3]))

        elif float(''.join(data[3*i + 3])) < minVal:
            minVal = float(''.join(data[3*i + 3]))

    # parsing every 3rd value starting from the 4th element in list
        decibelCount = decibelCount + float(''.join(data[3*i + 3]))
        count = count + 1
        totalTime = totalTime + 1
        runningTime = runningTime + 1

print(len(timeStats))
print("The average time, maximum and minimum dB values per each time period:", timeStats)
print("")
print("The percentage of unharmful hearing is",
      (int(100*((safeTime)/runningTime))), "%")
print("The percentage of time in the green zone is",
      (int(100*(greenTime)/runningTime)), "%")
print("The percentage of time in the yellow zone is",
      (int(100*((yellowTime)/runningTime))), "%")
print("The percentage of time in the red zone is",
      (int(100*((redTime)/runningTime))), "%")

print("")
print("The time spent in the range up to 70 dB is", int(upToSeventy), "s")
print("The time spent in the 70 - 80 dB range is", int(seventyToEighty), "s")
print("The time spent in the 80 - 90 dB range is", int(eightyToNinety), "s")
print("The time spent in the 90 - 100 dB range is", int(ninetyToHundred), "s")
print("The time spent in the 100 dB + range is", int(moreThanHundred), "s")
print("")

# CHECKS FOR PROLONGED EXPOSURE AND ALERTS USER IF THERE IS A WARNING
# for the purposes of testing, the alert exposure time is 60s
if int(eightyToNinety + ninetyToHundred + moreThanHundred) >= 60:
    print("WARNING: You've been exposed to 80+ db levels for", int(eightyToNinety +
          ninetyToHundred + moreThanHundred), "s. Seek hearing protection now!")

# NEED TO PARSE:
# 1. Average db per hour duration (use the timestamp for displays stats per hour, day etc)
# 2. Max and min db values per time duration
# 3. Percentages of time duration composed of green, yellow and red-level sound exposures (pie chat - percentages)
# 4. Find the time per decibel value (or maybe easier, find the total time per range ie. time for 70-80 db, 80-90 db etc) - sampling rate is 200 ms
# 5. Elapsed time

str_time_stats = "The average time, maximum and minimum dB values per each time period: " + \
    str(timeStats) + "\n"
str_unharmful_time = "The percentage of unharmful noise is " + \
    str(int(100*((safeTime)/runningTime))) + "%\n"
str_green_time = "The percentage of time in the green zone is " + \
    str(int(100*(greenTime)/runningTime)) + "%\n"
str_yellow_time = "The percentage of time in the yellow zone is " + \
    str(int(100*((yellowTime)/runningTime))) + "%\n"
str_red_time = "The percentage of time in the red zone is " + \
    str(int(100*((redTime)/runningTime))) + "%\n"
str_upto_seventy = "The time spent in the range up to 70 dB is " + \
    str(int(upToSeventy)) + "s\n"
str_seventy_eighty = "The time spent in the 70 - 80 dB range is " + \
    str(int(seventyToEighty)) + "s\n"
str_eighty_ninety = "The time spent in the 80 - 90 dB range is " + \
    str(int(eightyToNinety)) + "s\n"
str_ninety_hundred = "The time spent in the 90 - 100 dB range is " + \
    str(int(ninetyToHundred)) + "s\n"
str_hundred_plus = "The time spent in the 100 dB + range is " + \
    str(int(moreThanHundred)) + "s\n"
str_warning = "WARNING: You've been exposed to 80+ db levels for " + \
    str(int(eightyToNinety + ninetyToHundred + moreThanHundred)) + \
    "s. Seek hearing protection now!\n"

# PLOT DB-TIME PLOTS


# PLOT PERCENT BREAKDOWN
# pie_data = [int(100*((greenTime)/runningTime)), int(100 * ((yellowTime)/runningTime)),
#             int(100*((redTime)/runningTime)), int(100*((safeTime)/runningTime))]
# pie_labels = ["GREEN ZONE", "YELLOW ZONE", "RED ZONE", "SAFE ZONE"]
# pie_colours = ["green", "yellow", "red", "grey"]
# figure = plt.figure(figsize=(10, 7))
# plt.pie(pie_data, labels=pie_labels, colors=pie_colours)
# plt.title("Daily Exposure Level Breakdown")
# plt.show()


# WRITE THE ANALYTICS DATA TO A TXT FILE
fh = open('analytics_report.txt', 'w')
fh.write("DAILY ANALYTICS REPORT\n")
fh.write(str_time_stats)
fh.write("\n")
fh.write(str_unharmful_time)
fh.write(str_green_time)
fh.write(str_yellow_time)
fh.write(str_red_time)
fh.write("\n")
fh.write(str_upto_seventy)
fh.write(str_seventy_eighty)
fh.write(str_eighty_ninety)
fh.write(str_ninety_hundred)
fh.write(str_hundred_plus)
fh.write("\n")
if int(eightyToNinety + ninetyToHundred + moreThanHundred) >= 60:
    fh.write(str_warning)
fh.close()
