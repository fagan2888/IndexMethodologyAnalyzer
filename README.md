# Index methodology analysis
## a data mining tool for index methodologies and factsheets

* `downloadMethod.py`: download all MSCI index methodology files
* `downloadFS.py`: download all MSCI index performance Factsheets
* `createdb.py`: record to sqlite3 database all the web scraping results, built upon `downloadMethod.py` and `downloadFS.py`
* `Parser.py`: Parsers for different files, also record in database
* `parse.py`: parse and analyze files, also record to local sqlite database
* `top_10_holding_plots.Rmd` generates some R plots available in Rmd and PDF version about holdings of each MSCI index, also generates `top10holding.csv` for top 10 holding records
* uses PDFMiner opensource API, currently only can run on linux/unix, try to resolve on windows