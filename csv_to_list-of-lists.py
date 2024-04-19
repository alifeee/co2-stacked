"""convert csv to list of lists for web component"""

import csv
import datetime

FILE_IN = "query.csv"
DT_FORMAT = "%Y-%m-%dT%H:%M:%SZ"
FILE_DUMP = "index.html"
START_TIME_H = 8

with open(FILE_IN, "r", encoding="utf-8") as f:
    reader = csv.DictReader(filter(lambda row: row[0] != "#", f))
    co2dict = []
    for line in reader:
        co2dict.append(line)

results = [[]]
day = 0
newday = False
start_time = datetime.datetime.strptime(co2dict[0]["_time"], DT_FORMAT)
last_time = datetime.datetime.strptime(co2dict[0]["_time"], DT_FORMAT)
# skip final line as time comes with microsecs...
# skip first line as it probably doesn't have full data...
for i, line in enumerate(co2dict[1:-1]):
    time = datetime.datetime.strptime(line["_time"], DT_FORMAT)
    if time.day != last_time.day:
        newday = True
    if newday is True and time.hour > START_TIME_H:
        day += 1
        newday = False
        results.append([])
    last_time = time

    results[day].append(line["_value"])

# skip first line as it is probably not as long as the others
# skip last line for similar reasons
print(f"got {len(results)} days of results")
data_str = str(results[1:-1]).replace(" ", "").replace("'", "")

with open(FILE_DUMP, "w", encoding="utf-8") as f:
    f.write(
        f"""<!DOCTYPE html>
    <html>
        <head>
            <script src="stacked-sparklines.0.0.5.js"></script>
            <style>
                html, body {{
                    margin: 0;
                    padding: 0;
                }}
                body {{
                    height: 100vh;
                    width: 100vw;
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    align-items: center;
                }}
                stacked-sparklines {{
                    border-radius: 2rem;
                }}
            </style>
        </head>
        <body>
            <h1>CO2 data</h1>
            <stacked-sparklines
                data-data="{data_str}"
                caption="Daily CO2"
                data-background="#00b7c6"
                data-foreground="white"
                size=1
                >
            </stacked-sparklines>
        </body>
    </html>
    """
    )
