import csv

data = []
with open('classvolume.csv') as file:
    r = csv.reader(file, delimiter=',')
    for row in r:
        data.append([str(x) for x in row])

print(data[0])
print(data[1])
print(data[2])
print(data[3])
print(data[4])
# for element in data:
#     print(element)

# try to get decibel values
decibels = []
i = 4
while i < len(data):
    print(data[i])
    intDecibel = int(data[i])
    print(intDecibel)
    # decibels.append(int(data[i]))
    i += 3

for element in decibels:
    print(element)
