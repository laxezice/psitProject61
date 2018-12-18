import pygal
import csv

total = {}
# import csv file
with open('../database/mount12.txt') as csvfile:
    readfile = csv.reader(csvfile, delimiter=',')
    for line in readfile:
        artist = str(line[0])
        report = str(line[1]).split("@")
        for i in range(len(report)):
            if report[i] in "0123456":
                report[i] = int(report[i])
            else:
                report[i] = None
        total[artist] = report

line_chart = pygal.StackedBar()
line_chart.title = 'Total report'
line_chart.x_labels = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
for artist in total:
    if artist == 'None':
        line_chart.add(artist, total[artist] , stroke_style={'color' : '#000000'})
    print(artist, total[artist])
line_chart.render_to_file('../graph/total.svg')