# 06/jan/2016
#
# Igor Kelvin
# igorkelvin@gmail.com
# https://github.com/igorkelvin
#
# Script to download from 'http://tldp.org/LDP/abs/html/xrefindex.html' all
# html pages so I can access it while offline.
#
# My first attempt was to simple get a list with all important html link from
# the index and just download them. At first I thought it worked, but there was
# several missing links that the creator haven't put directly on the index.
#
# So, I got the first htmls manually and was getting the next link one by one
# until there is no 'Next'.
#
# Be sure you have BeautifulSoup4 installed!
#
# Written in Python3

import requests
from bs4 import BeautifulSoup

url_base = 'http://tldp.org/LDP/abs/html/'
global r

def download_file(name):

    print("Downloading {}... ".format(name), end='')

    try:
        with open(name, 'r') as f:
            print("File already exists")
    except FileNotFoundError:
        with open(name, 'w') as f:
            f.write(r.text)
            print("Done")

if __name__ == '__main__':

    try:
        html = 'index.html'
        r = requests.get(url_base + html)
        download_file(html)
        soup = BeautifulSoup(r.text, 'lxml')

        html = 'part1.html'
        while (html):

            r = requests.get(url_base + html)
            download_file(html)

            soup = BeautifulSoup(r.text, 'lxml')

            try:
                html = soup.find('a', accesskey='N').get('href')
            except AttributeError:
                break
        print("")
        print("Done")
    except:
        print("")
        print("Aborting")
