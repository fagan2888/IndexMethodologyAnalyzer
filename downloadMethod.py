from lxml import html
import requests, os, urllib.request, re

cwd = os.getcwd()
savePath = input("Please input your desired pdf folder name for methodology: ")
pwd = cwd + "/" + savePath
if not os.path.isdir(pwd):
	os.makedirs(pwd)
	print("---> input directory not exist in current workpath, creating new one...")

link = 'https://www.msci.com/index-methodology?p_p_id=extendedlister_WAR_extendedlister_INSTANCE_BE0Rsh4xpcju&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-pressroomsearch&p_p_col_count=1&_extendedlister_WAR_extendedlister_INSTANCE_BE0Rsh4xpcju_search={"lastModification":["MM","YYYY","MM","YYYY"],"sort_by":"relevance","results":"500"}#BE0Rsh4xpcju'
page = requests.get(link)
tree = html.fromstring(page.content)
print("Connect to WSCI methodology webpage")

aTags = tree.xpath('//li[@class="msci-search-result"]/p/a')
hrefs = [a.attrib['href'] for a in aTags]
print("Get \033[1m {} \033[0m downloadable pdf links, start downlaoding...".format(len(hrefs)))

unnamed = list()
failed = list()
for h in hrefs:
	fileName = h.split("/")[-1]
	print(fileName)
	try:
		if not re.search('.pdf', fileName):
			print("---> Downloading unnamed file", fileName)
			urllib.request.urlretrieve(h, savePath + "/" + fileName + ".pdf")
			unnamed.append(fileName)
		else:
			print("---> Downloading named file", fileName)
			urllib.request.urlretrieve(h, savePath + "/" + fileName)
	except:
		print('\033[1m', "---> ERROR: CANNOT Download file", fileName, '\033[0m')
		failed.append(fileName)

print("Finished downloading, all files at", cwd)
print("Success Download: \033[1m {} \033[0m".format(len(os.listdir(savePath))))

print("\033[1m {} \033[0m Unnamed files:".format(len(unnamed)))
for f in unnamed:
	print(f)

print("\033[1m {} \033[0m Failed files:".format(len(failed)))
for f in failed:
	print(f)



















