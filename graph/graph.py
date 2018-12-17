import csv
import pygal

gender_data = []
percents_data = []
with open('../database/gender17.txt') as csvfile:
    readfile = csv.reader(csvfile, delimiter=',')

    for line in readfile:
        gender = str(line[0])
        percent = float(line[1])
        gender_data.append(gender)
        percents_data.append(percent)

pie_chart = pygal.Pie()
pie_chart.title = 'By Gender 2017'
pie_chart.add(gender_data[0], percents_data[0])
pie_chart.add(gender_data[1], percents_data[1])
pie_chart.render_to_file('gender2017.svg')


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
        time_data.append(day)
        percents_data.append(percent)

pie_chart = pygal.Pie()
pie_chart.title = 'By Time 2017'
pie_chart.add(day_data[0], percents_data[0])
pie_chart.add(day_data[1], percents_data[1])
pie_chart.add(day_data[2], percents_data[2])
pie_chart.add(day_data[3], percents_data[3])
pie_chart.add(day_data[4], percents_data[4])
pie_chart.add(day_data[5], percents_data[5])
pie_chart.add(day_data[6], percents_data[6])
pie_chart.render_to_file('day2017.svg')


age_data = []
percents_data = []
with open('../database/age17.txt') as csvfile:
    readfile = csv.reader(csvfile, delimiter=',')

    for line in readfile:
        age = str(line[0])
        percent = float(line[1])
        age_data.append(age)
        percents_data.append(percent)

pie_chart = pygal.Pie()
pie_chart.title = 'By Time 2017'
pie_chart.add(age_data[0], percents_data[0])
pie_chart.add(age_data[1], percents_data[1])
pie_chart.add(age_data[2], percents_data[2])
pie_chart.add(age_data[3], percents_data[3])
pie_chart.add(age_data[4], percents_data[4])
pie_chart.add(age_data[5], percents_data[5])
pie_chart.render_to_file('age2017.svg')











