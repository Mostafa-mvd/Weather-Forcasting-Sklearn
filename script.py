import csv

lines = []

with open("../WeatherForcasting/weather_aqx_data.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for idx_i, row in enumerate(reader):
        if idx_i:
            for idx , col in enumerate(row):
                if col == 'Â\xa0' or col == '' or col == '-':
                    row[idx] = "0"
            # line = [str(idx_i), *row[1:]]
            lines.append(row)
        else:
            lines.append(row)

    
with open("../WeatherForcasting/weather_aqx_data.csv", "w", encoding="utf-8") as file:
    writer = csv.writer(file)
    for line in lines:
        writer.writerow(line)
