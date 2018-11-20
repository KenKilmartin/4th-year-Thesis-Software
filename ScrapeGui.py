from tkinter import *
import os
import subprocess
from subprocess import call

comand = "python WebScrapingRentalHouse.py"
comand2 = "python WebScrapingRentalApartments.py"
comand3 = "python WebScrapingRentalHouse.py & python WebScrapingRentalApartments.py"

window = Tk()

window.title("WebScrapper scraping")

window.geometry('350x200')



lbl = Label(window, text="Please be patient ")

lbl.grid(column=0, row=0)


def clicked():
    window.configure(background='red')
    lbl.configure(text="Houses starting to be scraped!!")
    os.system(comand)
    subprocess.Popen(comand)

def clicked2():
    window.configure(background='red')
    lbl.configure(text="Apartments starting to be scraped!!")
    os.system(comand2)
    subprocess.Popen(comand2)

def stop():
    window.configure(background='green')
    lbl.configure(text="Scraping Both!!")
    os.system(comand3)
    subprocess.Popen(comand3)


btn = Button(window, text="Scrape Houses", command=clicked)
btn2 = Button(window, text="Scrape Apartment", command=clicked2)
btn3 = Button(window, text="Scrape Both", command=stop)


btn.grid(column=1, row=2)
btn2.grid(column=4, row=2)
btn3.grid(column=3, row=6)



window.mainloop()