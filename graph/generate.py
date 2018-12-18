import csv
import pygal

song17_data = {}
artist17_data = {}
song18_data = {}
artist18_data = {}
style17_data = {}
style18_data = {}

# import csv file
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

        # pick data into dictionary
        if song in song18_data:
            song18_data[song] += 1
        else:
            song18_data[song] = 1

        if artist in artist18_data:
            artist18_data[artist] += 1
        else:
            artist18_data[artist] = 1

        if style in style18_data:
            style18_data[style] += 1
        else:
            style18_data[style] = 1

# import csv file
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

        # pick data into dictionary
        if song in song17_data:
            song17_data[song] += 1
        else:
            song17_data[song] = 1

        if artist in artist17_data:
            artist17_data[artist] += 1
        else:
            artist17_data[artist] = 1

        if style in style17_data:
            style17_data[style] += 1
        else:
            style17_data[style] = 1


song_stream = {}
artist_stream = {}
style_stream = {}

with open('../database/Streamchart.txt') as csvfile:
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

        # pick data into dictionary
        if song in song_stream:
            song_stream[song] += 1
        else:
            song_stream[song] = 1

        if artist in artist_stream:
            artist_stream[artist] += 1
        else:
            artist_stream[artist] = 1

        if style in style_stream:
            style_stream[style] += 1
        else:
            style_stream[style] = 1


artist_sell = {}

with open('../database/Sell.txt') as csvfile:
    readfile = csv.reader(csvfile, delimiter=',')

    for line in readfile:
        artist = str(line[0])

        if "@" in artist:
            artist = artist.replace("@", ",")

        # pick data into dictionary
        if artist in artist_sell:
            artist_sell[artist] += 1
        else:
            artist_sell[artist] = 1

song_yt= {}
artist_yt = {}

with open('../database/YtChart2018.txt') as csvfile:
    readfile = csv.reader(csvfile, delimiter=',')

    for line in readfile:
        song = str(line[0])
        artist = str(line[1])

        if "@" in song:
            song = song.replace("@", ",")
        if "@" in artist:
            artist = artist.replace("@", ",")

        # pick data into dictionary
        if song in song_yt:
            song_yt[song] += 1
        else:
            song_yt[song] = 1

        if artist in artist_yt:
            artist_yt[artist] += 1
        else:
            artist_yt[artist] = 1


# sort data
song17_data = list(sorted(song17_data.items(), key=lambda x: -x[1]))
artist17_data = list(sorted(artist17_data.items(), key=lambda x: -x[1]))
song18_data = list(sorted(song18_data.items(), key=lambda x: -x[1]))
artist18_data = list(sorted(artist18_data.items(), key=lambda x: -x[1]))
style17_data = list(sorted(style17_data.items(), key=lambda x: -x[1]))
style18_data = list(sorted(style18_data.items(), key=lambda x: -x[1]))
song_stream = list(sorted(song_stream.items(), key=lambda x: -x[1]))
artist_stream = list(sorted(artist_stream.items(), key=lambda x: -x[1]))
style_stream = list(sorted(style_stream.items(), key=lambda x: -x[1]))
artist_sell = list(sorted(artist_sell.items(), key=lambda x: -x[1]))
song_yt= list(sorted(song_yt.items(), key=lambda x: -x[1]))
artist_yt = list(sorted(artist_yt.items(), key=lambda x: -x[1]))


# create chart
line_chart = pygal.HorizontalBar()
line_chart.title = '1st song billboard chart 2017'
for song in song17_data:
    line_chart.add(song[0], song[1])
line_chart.render_to_file('song17.svg')

line_chart = pygal.HorizontalBar()
line_chart.title = '1st song billboard chart 2018'
for song in song18_data:
    line_chart.add(song[0], song[1])
line_chart.render_to_file('song18.svg')

line_chart = pygal.HorizontalBar()
line_chart.title = '1st artist billboard chart 2017'
for artist in artist17_data:
    line_chart.add(artist[0], artist[1])
line_chart.render_to_file('artist17.svg')

line_chart = pygal.HorizontalBar()
line_chart.title = '1st artist billboard chart 2018'
for artist in artist18_data:
    line_chart.add(artist[0], artist[1])
line_chart.render_to_file('artist18.svg')

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

line_chart = pygal.HorizontalBar()
line_chart.title = '1st steaming song 2018'
for song in song_stream:
    line_chart.add(song[0], song[1])
line_chart.render_to_file('song_stream.svg')

line_chart = pygal.HorizontalBar()
line_chart.title = '1st steaming artist 2018'
for artist in artist_stream:
    line_chart.add(artist[0], artist[1])
line_chart.render_to_file('artist_stream.svg')

line_chart = pygal.HorizontalBar()
line_chart.title = '1st steaming style 2018'
for style in style_stream:
    line_chart.add(style[0], style[1])
line_chart.render_to_file('style_stream.svg')

line_chart = pygal.HorizontalBar()
line_chart.title = '1st artist best sell song 2018'
for artist in artist_sell:
    line_chart.add(artist[0], artist[1])
line_chart.render_to_file('artist_sell.svg')

line_chart = pygal.HorizontalBar()
line_chart.title = '1st artist best sell song 2018'
for song in song_yt:
    line_chart.add(song[0], song[1])
line_chart.render_to_file('song_yt.svg')

line_chart = pygal.HorizontalBar()
line_chart.title = '1st artist best sell song 2018'
for artist in artist_yt:
    line_chart.add(artist[0], artist[1])
line_chart.render_to_file('artist_yt.svg')
