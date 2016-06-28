import os

for file in os.listdir("test2"):
	FactsheetParser("test2/"+file).listFacts()