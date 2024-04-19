# CO2 Stacked

A visualisation of CO2 levels as a vertically stacked graph, with days going upwards. Using @tomhazledine's [`<stacked-sparklines>`](https://github.com/tomhazledine/stacked-sparklines) web component.

![Screenshot of a webpage titled "CO2 data". Lots of lines are shown overlapping over one another, each with a spike near the start.](./images/stacked.png)

The original data looked something like this:

![Screenshot of graph. x-axis is time. y-axis is CO2 (ppm). graph has several vertical spikes.](images/data-original.png)

## How to create

Export CO2 data as CSV from InfluxDB via the data explorer. It should be several days of data, and the window range can be whatever, but probably change it from auto.

![Screenshot of InfluxDB data explorer, showing "Download CSV" button highlighted](images/export-csv.png)

Put this file in this repository, named `query.csv`. Then, run the python script to generate the visualisation.

```bash
python ./csv_to_list-of-lists.py
```

## Note

This was made brashly in a few minutes. Do not expect it to work perfectly ;)
