import pandas as pd

#had to look up that encoding  as woould come up with strange error
df = pd.read_csv('Scrapped Data House/Scrape from 13-12-2018 at 10H 23 M.csv', encoding="ISO-8859-1")

description = df['Price'].describe()
print('Breakdown of Price for all of ireland\n')
print(description)