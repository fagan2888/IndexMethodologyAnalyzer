import re, sqlite3

'''
Base class Parser used for detailed 
implementation of different textual parsers
'''
class Parser:

	def __init__(self, path, dbName, tableName):
		self.path = path
		self.dbName = dbName
		self.tableName = tableName
		self.text = open(path).read()
		self.facts = dict()

	def analyze(self):
		print(text)

	def listFacts(self):
		for (k, v) in self.facts.items():
			print('\033[1m', k, '\033[0m', v)

	def createDB(self):
		print("No data table to create")

	def registerRecord(self):
		print("No record to register")

class FactsheetParser(Parser):

	def analyze(self):
		facts["index"] = self.path.replace(".txt","").replace("_"," ").upper()
		excludedRegex = "(^[0-9][.,0-9]+|^[0-9]$|TOP|MSCI|Weight|Mkt|Country|ESG|SRI|SECTOR|Momentum|Carbon|Fuels|^[A-Z][A-Z]$)"

		self.facts["methodology"] = self.text.split("INDEX METHODOLOGY\n")[-1].split("ABOUT MSC\n")[0].replace("\n","")
		stocks = list(filter(bool, self.text.split("Largest\nSmallest\nAverage\nMedian\n")[-1].split("Total\n")[0].split("\n")))
		top10Stocks = list(filter(lambda s:not re.search(excludedRegex, s), stocks))
		if not len(top10Stocks) <= 10:
			raise Exception("not correct parsing", top10Stocks, len(top10Stocks))
		else:
			for i in range(1, len(top10Stocks)+1):
				self.facts["top{}".format(i)] = top10Stocks[i-1]

	def createDB(self):
		conn = sqlite3.connect(self.dbName)
		print("Open database {} to register analysis results".format(dbName))
		conn.execute('''CREATE TABLE {}
						(INDEX_NAME CHAR(50) PRIMARY KEY NOT NULL,
						 TOP1       INT                          ,  
						 TOP2       INT                          ,
						 TOP3       INT                          ,
						 TOP4       INT                          ,
						 TOP5       INT                          ,
						 TOP6       INT                          ,
						 TOP7       INT                          ,
						 TOP8       INT                          ,
						 TOP9       INT                          ,  
						 TOP10      INT                          ,
						 METHOD     CHAR(200)                    );
					'''.format(tableName)
		)
		conn.commit()
		conn.close()

	def registerRecord(self):
		conn = sqlite3.connect(self.dbName)
		conn.execute('''INSERT INTO {} (INDEX_NAME, TOP1, TOP2, TOP3, TOP4, TOP5, TOP6, TOP7, TOP8, TOP9, TOP10, METHOD)
						VALUES ({}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {})
					 '''.format(
					 	self.tableName, 
					 	self.facts["index"], 
					 	self.facts["top1"], self.facts["top2"], self.facts["top3"], self.facts["top4"], self.facts["top5"], 
					 	self.facts["top6"], self.facts["top7"], self.facts["top8"], self.facts["top9"], self.facts["top10"], 
					 	self.facts["methodology"])
		)
		conn.commit()
		conn.close()











