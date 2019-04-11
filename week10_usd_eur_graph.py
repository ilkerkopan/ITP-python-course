import pygal

dates = []
usd = []
eur = []
with open("USD-EUR.csv") as file:
    file.readline()
    for line in file:
        try :
            dates.append(line.split(",")[0])
            usd.append(float(line.split(",")[1]))
            eur.append(float(line.split(",")[2]))
        except:
            # ignore this line
            pass

#chart properties
line_chart = pygal.Line()
line_chart.title = 'USD and EURO Values over time'
line_chart.x_title = 'Dates'
line_chart.y_title = 'TL'
line_chart.x_labels = dates
line_chart.add('USD', usd)
line_chart.add('EURO',  eur)
line_chart.render_to_file('usd-eur.svg')