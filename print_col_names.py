import pandas
#OK yeah I cheated a bit...
import re

data = pandas.read_csv("weather_data/weather_year.csv")

col_names = data.columns.values.tolist()
print col_names

col_names_nw = []

for i in col_names:
    print(re.sub(" ","",i))

# STEP 3 - Using the shell:
# (a) write ONLY the new non-whitespace column names to a new file called columnNames instead of the shell output (stdout)
# (b) similarly, sort the outputted column names into a new file called sortedColumnNames

# Push the following files to Aleksandra's github: this file containing the fixed code, file with the column names with spaces removed, and the file with the sorted names
# This will raise a pull request, so we can check your script
