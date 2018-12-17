import csv
import pygal

song_data = {}
artist_data = {}
style17_data = {}
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
            artist = artist.replace("@", ",")
        if "@" in style:
            style = style.replace("@", ",")

        if song in song_data:
            song_data[song] += 1
        else:
            song_data[song] = 1

        if artist in artist_data:
            artist_data[artist] += 1
        else:
            artist_data[artist] = 1

        if style in style18_data:
            style18_data[style] += 1
        else:
            style18_data[style] = 1

with open('../database/artist17.txt') as csvfile:
    readfile = csv.reader(csvfile, delimiter=',')

    for line in readfile:
        song = str(line[0])
        artist = str(line[1])
        style = str(line[2])

        if "@" in song:
            song = song.replace("@", ",")
        if "@" in artist:
            artist = artist.replace("@", ",")
        if "@" in style:
            style = style.replace("@", ",")

        if song in song_data:
            song_data[song] += 1
        else:
            song_data[song] = 1

        if artist in artist_data:
            artist_data[artist] += 1
        else:
            artist_data[artist] = 1

        if style in style17_data:
            style17_data[style] += 1
        else:
            style17_data[style] = 1

song_data = list(sorted(song_data.items(), key=lambda x: -x[1]))
artist_data = list(sorted(artist_data.items(), key=lambda x: -x[1]))
style18_data = list(sorted(style18_data.items(), key=lambda x: -x[1]))
style17_data = list(sorted(style17_data.items(), key=lambda x: -x[1]))

line_chart = pygal.HorizontalBar()
line_chart.title = '1st song billboard chart 2017-2018'
for song in song_data:
    line_chart.add(song[0], song[1])
line_chart.render_to_file('song.svg')

line_chart = pygal.HorizontalBar()
line_chart.title = '1st artist billboard chart 2017-2018'
for artist in artist_data:
    line_chart.add(artist[0], artist[1])
line_chart.render_to_file('artist.svg')

line_chart = pygal.HorizontalBar()
line_chart.title = '1st style billboard chart 2018'
for style in style18_data:
    line_chart.add(style[0], style[1])
line_chart.render_to_file('style18.svg')

line_chart = pygal.HorizontalBar()
line_chart.title = '1st style billboard chart 2017'
for style in style17_data:
    line_chart.add(style[0], style[1])
line_chart.render_to_file('style17.svg')
