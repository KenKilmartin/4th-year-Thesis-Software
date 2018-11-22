from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv
import datetime

#constant for number of pages wanted to crawl
MAX_PAGE_NUM = 45

#need to download the chromedriver to get it to open page
chrome_path = r'C:\Python\Python37\Scripts\chromedriver\chromedriver.exe'


#The below path is for laptop
#chrome_path = r'C:\Python\Python37-32\Scripts\chromedriver.exe'


options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(chrome_path, chrome_options=options)


#driver = webdriver.Chrome(chrome_path)

now = datetime.datetime.now()

#writing csv file and labeling the csv file with date

# csv_file = open('test.csv', 'w')
csv_file = open('Scrapped Data Apartments/Scrape from ' + now.strftime("%d-%m-%Y at %H"+"H"+" %M M")+'.csv', 'w', newline='')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['House', 'Price', 'County'])


def getDataByCounty():
    countyFile = open("counties.txt")

    for line in countyFile:
        for i in range(0, MAX_PAGE_NUM):
            listings = i * 20
            url = "https://www.daft.ie/"+line+"/apartments-for-rent/?s%5Bignored_agents%5D%5B0%5D=428&s%5Bignored_agents%5D%5B1%5D=1551&offset=" + str(
                listings)
            driver.get(url)
            houses = driver.find_elements_by_class_name("box")
            crawlycrawl(houses)
        print(line)
    csv_file.close()


def findByCountyName(stringToSearch):

    stringArray = stringToSearch.split(',')
    county = stringArray[len(stringArray) - 1]
    return county

"""
going through each house on each page and
"""
def crawlycrawl(houses):
    for house in houses:
        houseName = house.find_element_by_class_name("search_result_title_box").text
        # and '- House to Ren'
        startOfStringToRemove = houseName.find(' - Apartment to Rent') and houseName.find(' - Apartment to Rent')
        houseName = houseName[:startOfStringToRemove]
        price = house.find_element_by_class_name("info-box").find_element_by_class_name("price")


       # print(houseName.text + " " + price.text)
        priceText = ''

        """
        This is looking for the price and if the price is per week if it finds per week it multiplys by 4 else it saves the value
        it also takes out the euro symbol and the per month per week string
        """

        for i in range(0, len(price.text)):
            if str.isdigit(price.text[i]):
                priceText += price.text[i]

        if "week" in str.lower(price.text):
            value = int(priceText) * 4  # this method would not take into account months that have 5 weeks
           # value = int(priceText) * 52 / 12
          #  "{0:.2f}".format(value)
        else:
            value = int(priceText)
        csv_writer.writerow([houseName]+[value] + [findByCountyName(houseName)])


#this closes the browser
print("Starting to Scrape Apartments")
getDataByCounty()
driver.close()




