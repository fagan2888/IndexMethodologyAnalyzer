# MSCI index methodology analysis

* `downloadMethod.py`: download all MSCI index methodology files
* `downloadFS.py`: download all MSCI index performance Factsheets
* `createdb.py`: record to sqlite3 database (not finished)
* `Parser.py`: Parsers for different files, also record in database
* `parse.py`: parse and analyze files
* some R plots available in pdf
* top 10 holdings of each index recorded in `top10holding.csv`
* uses PDFMiner opensource API, currently only can run on linux/unix, try to resolve on windows