import os, re, sqlite3


savePath = input("Please input your pdf folder name: ")

pdfs = os.listdir(savePath)

esg = [f for f in pdfs if re.search("(esg|ESG)", f)]
sri = [f for f in pdfs if re.search("(SRI|sri)", f)]
env = [f for f in pdfs if re.search("environment", f.lower())]
cbn = [f for f in pdfs if re.search("carbon", f.lower())]
cli = [f for f in pdfs if re.search("climate", f.lower())]
 = [f for f in pdfs if re.search("sustainable", f.lower())]

conn = sqlite3.connect('msci.db')
c = conn.cursor()
c.execute('''CREATE TABLE methodology
				(INDEX, SHEET_PATH, LAST_UPDATE, AS_OF_DATE)''')

#insert sql

conn.commit()
conn.close()