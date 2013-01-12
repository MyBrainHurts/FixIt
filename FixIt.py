import os
import platform
import re
import urllib
import urllib2
import csv

from BeautifulSoup import BeautifulSoup

#Switch folders to the desired folder. PC or Mac. 

computer = platform.system()

if computer == 'Windows':
    os.chdir(r"c:\_VirusFixes")

elif computer == 'Darwin':
    os.chdir(r"/Users/aaron/Downloads")

#List of websites with the files to download

websites = [

'http://cdn.superantispyware.com/SUPERAntiSpyware.exe',
'http://www.simplysup.com/tremover/download.html',
'http://tigzy.geekstogo.com/Tools/RogueKiller.exe',
'http://support.kaspersky.com/downloads/utils/tdsskiller.exe',
'http://www.bleepingcomputer.com/download/malwarebytes-anti-malware/dl/7/?1',
]


#Downloads exe files directly. 

for url in websites:
	executable = url.split('/')[-1]
	e = os.path.splitext(executable)[-1]
	if e == ('.exe'):
		urllib.urlretrieve(url, os.path.basename(url))

#Scrapes the site for the exe file to download

else:
	page = urllib2.urlopen(url).read()
	soup = BeautifulSoup(page)
	dload = soup.findAll('a', attrs = { 'href' : re.compile(r'.exe') })

	for link in dload:
		dropit = link.get('href')
		urllib.urlretrieve(dropit, os.path.basename(dropit))


		print "Done"


	


