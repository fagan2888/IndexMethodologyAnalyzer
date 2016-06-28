
'''
Base class Parser used for detailed 
implementation of different textual parsers
'''
class Parser:

	def __init__(self, text):
		self.text = text
		self.facts = dict()

	def analyze(self):
		print(text)

	def listFacts(self):
		for (k, v) in facts:
			print('\033[1m', k, '\033[0m', v)


class FactsheetParser(Parser):

	def analyze(self):
		self.facts["methodology"] = self.text.split("INDEX METHODOLOGY")[-1].split("ABOUT MSCI")[0]
		self.facts["top10stocks"] = self.text.split("TOP 10 CONSTITUENTS")[-1].split("Total")[0].split("\n")

class ESGMethodologyParser(Parser):

	def analyze(self):
		# your code here


class SRIMethodologyParser(Parser):

	def analyze(self):
		# your code here













