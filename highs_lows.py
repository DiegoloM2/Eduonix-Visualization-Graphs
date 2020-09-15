import csv
import matplotlib.pyplot as plt
from datetime import datetime
#Get high temperatures from the file
filename = 'sitka_weather_2014.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)#returns the next line in the file.

    highs, lows = [], []
    dates = []
    
    #Here, we are extracting the first row of the csv file. 
    for row in reader:  
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        dates.append(current_date)
        highs.append(int(row[1]))
        lows.append(int(row[2]))


    #Plot data
    fig = plt.figure(dpi = 128, figsize = (10, 6))

    #the alpha arg controls a color's transparency.f
    plt.plot(dates,highs, c = 'red',alpha = 0.5)
    plt.plot(dates, lows, c = 'black', alpha = 0.5)
    plt.fill_between(dates, highs, lows, facecolor = 'black', alpha = 0.3)
    #Format the plot:
    plt.title("Daily high and low temperatures, 2014", fontsize=24)
    plt.xlabel('', fontsize = 16)
    fig.autofmt_xdate()#Draw the labels diagonally to prevent them from
                        #overlapping.
    plt.ylabel("Temperature (F)", fontsize = 16)
    plt.tick_params(axis = 'both', which = 'major', labelsize = 16)
    plt.show()

#Now let's try a similar thing with another file which has some data missing.

file2 = 'death_valley_2014.csv'

with open(file2) as f:
    read = csv.reader(f)
    header_row = next(read)
    print(header_row)
    highs1, lows1, dates1 = [],[],[]
    for row in read:
        try:
            current_date1 = datetime.strptime(row[0], "%Y-%m-%d")
            high =int(row[1])
            low = int(row[3])

        except ValueError:
            print(current_date, 'missing data')
        else:
            dates1.append(current_date1)
            lows1.append(low)
            highs1.append(high)

#Plot the data
    fig = plt.figure(dpi = 128, figsize = (10, 6))


    plt.plot(dates1,highs1, c = 'red',alpha = 0.5)
    plt.plot(dates1, lows1, c = 'black', alpha = 0.5)
    plt.fill_between(dates1, highs1, lows1, facecolor = 'black', alpha = 0.3)
    #Format the plot:
    plt.title("Daily high and low temperatures - Death Valley\n 2014", fontsize=24)
    plt.xlabel('', fontsize = 16)
    fig.autofmt_xdate()#Draw the labels diagonally to prevent them from
                        #overlapping.
    plt.ylabel("Temperature (F)", fontsize = 16)
    plt.tick_params(axis = 'both', which = 'major', labelsize = 16)
    plt.show()

