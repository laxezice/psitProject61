import csv
import pygal
import numpy

song_data = {}
artist_data = {}
style18_data = {}

with open('../database/artist.txt') as csvfile:
    readfile = csv.reader(csvfile, delimiter=',')

    for line in readfile:
        song = str(line[0])
        artist = str(line[1])
        style = str(line[2])

        if "@" in song:
            song = song.replace("@", ",")
        if "@" in artist:
            song = song.replace("@", ",")
        if "@" in style:
            song = song.replace("@", ",")

        if song in song_data:
            song_data[song] += 1
        else:
            song_data[song] = 1

        if artist in artist_data:
            artist_data[artist] += 1
        else:
            artist_data[artist] = 1

        if style in style_data:
            style18_data[style] += 1
        else:
            style18_data[style] = 1

print(song_data)
print(artist_data)
print(style_data)


# pie_chart = pygal.Pie()
# pie_chart.title = 'By Day 2018'
# pie_chart.add(day_data[0], percents_data[0])
# pie_chart.add(day_data[1], percents_data[1])
# pie_chart.add(day_data[2], percents_data[2])
# pie_chart.add(day_data[3], percents_data[3])
# pie_chart.add(day_data[4], percents_data[4])
# pie_chart.add(day_data[5], percents_data[5])
# pie_chart.add(day_data[6], percents_data[6])
# pie_chart.render_to_file('day2018.svg')