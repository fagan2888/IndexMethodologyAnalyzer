import os, re, Parser

for file in os.listdir("test2"):
	if re.search(".txt", file):
		# print("Start parsing file", file)
		parser = Parser.FactsheetParser("test2/"+file)
		parser.analyze()
		parser.register()
		# facts = parser.facts
		# print(file.replace(".txt","").replace("_"," ").upper(), facts.get("top1"), facts.get("top2"), facts.get("top3"), facts.get("top4"), facts.get("top5"), facts.get("top6"), facts.get("top7"), facts.get("top8"), facts.get("top9"), facts.get("top10"), sep=",")