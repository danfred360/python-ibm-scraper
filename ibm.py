'''
Author: Daniel Frederick
Date: October 19, 2018
'''

from lxml import html
import requests
import os
import datetime

mainurl = 'https://newsroom.ibm.com/announcements'
exarturl = 'https://newsroom.ibm.com/2018-10-18-IBM-Stop-the-Traffik-Western-Union-Barclays-Lloyds-Banking-Group-Liberty-Global-Europol-and-University-College-London-Unveil-International-Data-Hub-to-Combat-Human-Trafficking'

class scrape:
    def __init__(self, url):
        print('\nGetting site code from ' + url + ' ... ')
        self.page = requests.get(url)
        self.tree = html.fromstring(self.page.content)

    def run(self):
        title = self.titles()
        link = self.links()

    #returns array of titles
    def titles(self):
        print('Scraping titles ... ')
        return self.tree.xpath('//div[@class="wd_title"]/a/text()')

    #returns an array of links
    def links(self):
        print('Scraping links ... ' )
        hrefs = self.tree.xpath('//div[@class="wd_title"]/a')
        ans = []
        for href in hrefs:
            ans.append(href.attrib['href'])
        return ans

    #returns an array of p elements
    def content(self):
        print('Scraping article content ... ')
        temp = self.tree.xpath('//div[@class="wd_body wd_news_body"]/p/text()')
        return temp

class output:
    def __init__(self):
        pass

    def allOne(self, path):
        now = datetime.datetime.now()
        filename = 'output' + now.strftime(' %Y-%m-%d %H %M') + '.txt'
        filepath = os.path.join(path, filename)
        if not os.path.exists(path):
            print('Path does not exist. Creating now...\n')
            os.mkdir(path)
        f = open(filepath, "w")

        temp = scrape(mainurl)
        title = temp.titles()
        link = temp.links()
        for i in title:
            f.write('\n' + i + '\n')
            for j in link:
                x = scrape(j)
                for k in x.content():
                    print(k)
                    f.write(k)
        f.close()
        print('Outputed file ' + str(filename) + '.\n')
        t = input('Press any key to exit --> ')

    def allSep(self, path):
        now = datetime.datetime.now()
        temp = scrape(mainurl)
        title = temp.titles()
        link = temp.links()
        path = path + now.strftime(' %Y-%m-%d %H %M')
        linkCount = 0
        for i in title:
            j = link[linkCount]
            filename = i + '.txt'
            filepath = os.path.join(path, filename)
            if not os.path.exists(path):
                print('Path does not exist. Creating now...\n')
                os.mkdir(path)
            f = open(str(filepath), "w")

            f.write('\n' + str(i) + '\n')
            x = scrape(j)
            try:
                for k in x.content():
                    f.write(str(k))
            except UnicodeEncodeError:
                print('\n----- Unicode Encode Error for file ' + str(i) + ' -----\n')
            f.close()
            print('Outputed file ' + str(filename) + '.\n')
            linkCount += 1
        print('Scan completed')
        t = input('Press any key to exit --> ')

class server:
    def __init__(self):
        self.now = datetime.datetime.now()

    def run(self):
        if self.currentMin() > self.now:
            pass


    def currentMin(self):
        return datetime.datetime.now().minute()


y = output()
y.allSep(input('Please enter desired output path --> '))
