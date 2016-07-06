import re, sqlite3

'''
Base class Parser used for detailed 
implementation of different textual parsers
'''
class Parser:

	def __init__(self, path):
		self.path = path
		self.text = open(path).read()
		self.facts = dict()

	def analyze(self):
		print(text)

	def listFacts(self):
		for (k, v) in self.facts.items():
			print('\033[1m', k, '\033[0m', v)

	def register(self, db):
		print("empty fact dictionary for database")


class FactsheetParser(Parser):

	def analyze(self):
		excludedRegex = "(^[0-9][.,0-9]+|^[0-9]$|TOP|MSCI|Weight|Mkt|Country|ESG|SRI|SECTOR|Momentum|Carbon|Fuels|^[A-Z][A-Z]$)"

		self.facts["methodology"] = self.text.split("INDEX METHODOLOGY\n")[-1].split("ABOUT MSC\n")[0].replace("\n","")
		stocks = list(filter(bool, self.text.split("Largest\nSmallest\nAverage\nMedian\n")[-1].split("Total\n")[0].split("\n")))
		top10Stocks = list(filter(lambda s:not re.search(excludedRegex, s), stocks))
		if not len(top10Stocks) <= 10:
			raise Exception("not correct parsing", top10Stocks, len(top10Stocks))
		else:
			for i in range(1, len(top10Stocks)+1):
				self.facts["top{}".format(i)] = top10Stocks[i-1]








