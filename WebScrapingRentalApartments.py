import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv
import datetime
import time

#constant for number of pages wanted to crawl
MAX_PAGE_NUM = 47
aproxPpr = 0

#need to download the chromedriver to get it to open page
#chrome_path = r'C:\Python\Python37\Scripts\chromedriver\chromedriver.exe'


#The below path is for laptop
chrome_path = r'C:\Python\Python37-32\Scripts\chromedriver.exe'

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(chrome_path, options=options)

now = datetime.datetime.now()

#writing csv file and labeling the csv file with date

# csv_file = open('test.csv', 'w')
csv_file = open('Scrapped Data Apartments/Scrape from ' + now.strftime("%d-%m-%Y at %H"+"H"+" %M M")+'.csv', 'w', newline='')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Apartment Index', 'Address', 'Price', 'County', 'Room', 'Approx price per room'])


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
        houseID = house.find_element_by_class_name("search_result_title_box").text
        getRidOfAllButIndex = houseID.find('.')
        houseID = houseID[:getRidOfAllButIndex]

        houseName = house.find_element_by_class_name("search_result_title_box").text
        # and '- House to Ren'
        lastPartOfStringToRemove = houseName.find(' - Apartment to Rent') and houseName.find(' - Apartment to Rent')
        getRidOfIndex = houseName.find('.')
        houseName = houseName[getRidOfIndex + 2:lastPartOfStringToRemove]

        price = house.find_element_by_class_name("info-box").find_element_by_class_name("price")

        priceText = ''

        room = house.find_element_by_class_name("info-box").find_element_by_class_name("info").text
        #if 'bed' in room.lower():
        indexOfBeds = room.lower().find('bed')
        # print(room)
        room = room[indexOfBeds - 2: indexOfBeds - 1]
        room = int(room)

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
            # value = "{0:.2f}".format(value)
        else:
            value = int(priceText)

        if room == 0:
             value = aproxPpr
        else:
            aproxPpr = value / room
            aproxPpr = "{0:.2f}".format(aproxPpr)

        csv_writer.writerow([houseID]+[houseName]+[value] + [findByCountyName(houseName)]+[room]+[aproxPpr])


#this closes the browser
print("Starting to Scrape Apartments")
start = time.time()

getDataByCounty()

end = time.time()
timetaken = end - start
minuteTaken = timetaken / 60
print('To run the scrape on Apartments it took ' + str(int(minuteTaken)) + ' minutes')

driver.close()




