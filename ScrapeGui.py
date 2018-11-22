from tkinter import *
import os
import subprocess
from subprocess import call

command = "python WebScrapingRentalHouse.py"
command2 = "python WebScrapingRentalApartments.py"
command3 = "python WebScrapingRentalHouse.py & python WebScrapingRentalApartments.py"

window = Tk()

window.title("WebScrapper scraping")

window.geometry('400x100')


lbl = Label(window, text="Please be patient !! ")
lbl.grid(column=0, row=0)


def clicked():
    window.configure(background='red')
    lbl.configure(text="Houses starting to be scraped!!")
    os.system(command)
    subprocess.Popen(command)


def clicked2():
    window.configure(background='red')
    lbl.configure(text="Apartments starting to be scraped!!")
    os.system(command2)
    subprocess.Popen(command2)


def stop():
    window.configure(background='green')
    lbl.configure(text="Scraping Both!!")
    os.system(command3)
    subprocess.Popen(command3)


btn = Button(window, text="Scrape Houses", command=clicked)
btn2 = Button(window, text="Scrape Apartment", command=clicked2)
btn3 = Button(window, text="Scrape Both", command=stop)


btn.grid(column=1, row=2)
btn2.grid(column=4, row=2)
btn3.grid(column=3, row=6)


window.mainloop()