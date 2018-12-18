import csv
import pygal

#2015

time_data = []
percents_data = []
with open('../database/time15.txt') as csvfile:
    readfile = csv.reader(csvfile, delimiter=',')

    for line in readfile:
        time = str(line[0])
        percent = float(line[1])
        time_data.append(time)
        percents_data.append(percent)

pie_chart = pygal.Pie()
pie_chart.title = 'By Time 2015'
pie_chart.add(time_data[0], percents_data[0])
pie_chart.add(time_data[1], percents_data[1])
pie_chart.add(time_data[2], percents_data[2])
pie_chart.add(time_data[3], percents_data[3])
pie_chart.add(time_data[4], percents_data[4])
pie_chart.add(time_data[5], percents_data[5])
pie_chart.render_to_file('time2015.svg')


day_data = []
percents_data = []
with open('../database/day15.txt') as csvfile:
    readfile = csv.reader(csvfile, delimiter=',')

    for line in readfile:
        day = str(line[0])
        percent = float(line[1])
        day_data.append(day)
        percents_data.append(percent)

pie_chart = pygal.Pie()
pie_chart.title = 'By Day 2015'
pie_chart.add(day_data[0], percents_data[0])
pie_chart.add(day_data[1], percents_data[1])
pie_chart.add(day_data[2], percents_data[2])
pie_chart.add(day_data[3], percents_data[3])
pie_chart.add(day_data[4], percents_data[4])
pie_chart.add(day_data[5], percents_data[5])
pie_chart.add(day_data[6], percents_data[6])
pie_chart.render_to_file('day2015.svg')


#2016

time_data = []
percents_data = []
with open('../database/time16.txt') as csvfile:
    readfile = csv.reader(csvfile, delimiter=',')

    for line in readfile:
        time = str(line[0])
        percent = float(line[1])
        time_data.append(time)
        percents_data.append(percent)

pie_chart = pygal.Pie()
pie_chart.title = 'By Time 2016'
pie_chart.add(time_data[0], percents_data[0])
pie_chart.add(time_data[1], percents_data[1])
pie_chart.add(time_data[2], percents_data[2])
pie_chart.add(time_data[3], percents_data[3])
pie_chart.add(time_data[4], percents_data[4])
pie_chart.add(time_data[5], percents_data[5])
pie_chart.render_to_file('time2016.svg')


day_data = []
percents_data = []
with open('../database/day16.txt') as csvfile:
    readfile = csv.reader(csvfile, delimiter=',')

    for line in readfile:
        day = str(line[0])
        percent = float(line[1])
        day_data.append(day)
        percents_data.append(percent)

pie_chart = pygal.Pie()
pie_chart.title = 'By Day 2016'
pie_chart.add(day_data[0], percents_data[0])
pie_chart.add(day_data[1], percents_data[1])
pie_chart.add(day_data[2], percents_data[2])
pie_chart.add(day_data[3], percents_data[3])
pie_chart.add(day_data[4], percents_data[4])
pie_chart.add(day_data[5], percents_data[5])
pie_chart.add(day_data[6], percents_data[6])
pie_chart.render_to_file('day2016.svg')


#2017

time_data = []
percents_data = []
with open('../database/time17.txt') as csvfile:
    readfile = csv.reader(csvfile, delimiter=',')

    for line in readfile:
        time = str(line[0])
        percent = float(line[1])
        time_data.append(time)
        percents_data.append(percent)

pie_chart = pygal.Pie()
pie_chart.title = 'By Time 2017'
pie_chart.add(time_data[0], percents_data[0])
pie_chart.add(time_data[1], percents_data[1])
pie_chart.add(time_data[2], percents_data[2])
pie_chart.add(time_data[3], percents_data[3])
pie_chart.add(time_data[4], percents_data[4])
pie_chart.add(time_data[5], percents_data[5])
pie_chart.render_to_file('time2017.svg')


day_data = []
percents_data = []
with open('../database/day17.txt') as csvfile:
    readfile = csv.reader(csvfile, delimiter=',')

    for line in readfile:
        day = str(line[0])
        percent = float(line[1])
        day_data.append(day)
        percents_data.append(percent)

pie_chart = pygal.Pie()
pie_chart.title = 'By Day 2017'
pie_chart.add(day_data[0], percents_data[0])
pie_chart.add(day_data[1], percents_data[1])
pie_chart.add(day_data[2], percents_data[2])
pie_chart.add(day_data[3], percents_data[3])
pie_chart.add(day_data[4], percents_data[4])
pie_chart.add(day_data[5], percents_data[5])
pie_chart.add(day_data[6], percents_data[6])
pie_chart.render_to_file('day2017.svg')


#2018

time_data = []
percents_data = []
with open('../database/time18.txt') as csvfile:
    readfile = csv.reader(csvfile, delimiter=',')

    for line in readfile:
        time = str(line[0])
        percent = float(line[1])
        time_data.append(time)
        percents_data.append(percent)

pie_chart = pygal.Pie()
pie_chart.title = 'By Time 2018'
pie_chart.add(time_data[0], percents_data[0])
pie_chart.add(time_data[1], percents_data[1])
pie_chart.add(time_data[2], percents_data[2])
pie_chart.add(time_data[3], percents_data[3])
pie_chart.add(time_data[4], percents_data[4])
pie_chart.add(time_data[5], percents_data[5])
pie_chart.render_to_file('time2018.svg')


day_data = []
percents_data = []
with open('../database/day18.txt') as csvfile:
    readfile = csv.reader(csvfile, delimiter=',')

    for line in readfile:
        day = str(line[0])
        percent = float(line[1])
        day_data.append(day)
        percents_data.append(percent)

pie_chart = pygal.Pie()
pie_chart.title = 'By Day 2018'
pie_chart.add(day_data[0], percents_data[0])
pie_chart.add(day_data[1], percents_data[1])
pie_chart.add(day_data[2], percents_data[2])
pie_chart.add(day_data[3], percents_data[3])
pie_chart.add(day_data[4], percents_data[4])
pie_chart.add(day_data[5], percents_data[5])
pie_chart.add(day_data[6], percents_data[6])
pie_chart.render_to_file('day2018.svg')


























