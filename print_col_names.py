import pandas
#OK yeah I cheated a bit...
import re

data = pandas.read_csv("weather_data/weather_year.csv")

col_names = data.columns.values.tolist()

col_names_nw = []

for i in col_names:
    print(re.sub(" ","",i))
