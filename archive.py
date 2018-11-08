'''
Author: Daniel Frederick
Date: November 7, 2018
'''

from lxml import html
import requests
import os
import datetime

url = 'https://www-03.ibm.com/press/us/en/pressreleases/finder.wss'

class Scrape:
    def __init__(self):
        print('\nGetting site code from ' + url + ' ... ')
        self.page = requests.get(url)
        self.tree = html.fromstring(self.page.content)

    def __repr__(self):
        return self.tree


class Archive:
    def __init__(self):
        path = self.getPath()
        now = datetime.datetime.now()
        self.tree = self.scrape(url)
        x = ['year', 'category']
        temp = self.getAnswer('Year or Category?', x)
        # articles by year
        if temp == 0:
            x = ['1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2016', '2017', '2018']
            year = self.getAnswer('Which year?', x)
            y = '/press/us/en/pressreleases/finder.wss?year={}'.format()
        # articles by category
        elif temp == 1:
            pass

    def scrape(self, url):
        print('\nGetting site code from ' + url + ' ... ')
        self.page = requests.get(url)
        return html.fromstring(self.page.content)

    # asks user question, and gives them options from ar options. Returns int corresponding to choice in options
    def getAnswer(self, question, options=['Yes', 'No']):
        print(question)
        for i in range(0, len(options)):
            print('Press {} for {}.'.format(i, options[i]))
        while True:
            choice = input('--> ')
            choice = int(choice)
            if choice < len(options):
                return choice
            else:
                print('Sorry, that is not an acceptable answer. Try again')




    def getPath(self):
        pass

yeet = Archive()
