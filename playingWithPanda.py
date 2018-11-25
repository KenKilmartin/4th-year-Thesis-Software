# import pandas as pd
# import csv
#
# df = pd.read_csv("Scrapped Data Apartments/Scrape from 24-11-2018 at 23H 10 M.csv")
# print(df)
import pandas as pd

#had to look up that encoding  as woould come up with strange error
df = pd.read_csv('Scrapped Data Apartments/Scrape from 24-11-2018 at 23H 10 M.csv', encoding="ISO-8859-1")
print(df.head(5))

# df.pivot_table(index="County", columns="price")

