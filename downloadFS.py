from lxml import html
import requests, os, urllib.request, re, csv

def searchFormat(name):
	return name.replace(" ", "%20")

def nameFormat(name):
	name = name.replace("& ", "")
	return name.replace(" ", "_")

cwd = os.getcwd()
savePath = input("Please input your desired pdf folder name for factsheets: ")
pwd = cwd + "/" + savePath
if not os.path.isdir(pwd):
	os.makedirs(pwd)
	print("---> input directory not exist in current workpath, creating new one...")


pdfToTxtBash = "pdf2txt.py {0}/{1}.pdf > {2}/{3}.txt"
deleteBash = "rm -f {0}/{1}.pdf"

with open("msci_list.csv") as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	for line in reader:
		name = line[0]
		link = 'https://www.msci.com/equity-fact-sheet-search?p_p_id=extendedlister_WAR_extendedlister_INSTANCE_yWFoRWV7pc2w&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-factsheet-search&p_p_col_count=1&_extendedlister_WAR_extendedlister_INSTANCE_yWFoRWV7pc2w_search={"lastModification":["MM","YYYY","MM","YYYY"],"keywords":"'+ searchFormat(name) +'","results":"10"}#yWFoRWV7pc2w'
		print(link)
		page = requests.get(link)
		tree = html.fromstring(page.content)
		print("Connect to factsheet webpage for", '\033[1m', name.upper(), '\033[0m')

		aTags = tree.xpath('//a[@class="factsheet-download"]')
		hrefs = [a.attrib['href'] for a in aTags]
		usName = nameFormat(name)
		try:
			urllib.request.urlretrieve(hrefs[0], savePath + "/" + usName + ".pdf")
			print("---> Downloading factsheet success")
		except:
			print('\033[1m', "---> ERROR: CANNOT Download file", usName, '\033[0m')

		os.system(pdfToTxtBash.format(savePath, usName, savePath, usName))
		os.system(deleteBash.format(savePath, usName))









