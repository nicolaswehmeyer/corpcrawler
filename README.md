# CorpCrawler
**A sales assistant for information gathering on accounts**

This python scripts automates searching Google for specific information on enterprises.

It is purely a terminal application developed to assist Account Managers and Sales Managers in automating information gathering tasks on their accounts. In this version it assists with finding out employee counts as well as headquarter locations of a list of given enterprises. It automates this process as it can become a highly time consuming task that can easily be automated.

The scripts expects an input CSV-file (--input-file, -i) that contains an account name per each line (no header needed). It will then iterate through each account and based on the fetched results from Google, it will create an output file (--output-file, -o), to which it will add the fetched information as well as the source urls.

# Installation
To use the script, please make sure you are running Python3. Also, the solution is using the "googlesearch-python" module to effectively search and parse the Google results, so make sure to install all required dependencies.

**Here are the steps to install all dependencies and run the script:**
1. Install dependencies: ```pip install -r requirements.txt```
2. Make script executable: ```chmod +x app.py```
3. Now you are ready to run it from your terminal

# Usage
Assuming we are storing a list of accounts in a CSV-file called accounts.csv and want to store the fetched information in a new CSV-file called updated.csv, **this would be the command to execute:**
```
./main.py --input-file accounts.csv --output-file updated.csv
```
**The script supports the following options:**
```
./main.py --help                                          
usage: main.py [-h] -i INPUT_FILE -o OUTPUT_FILE [-w WAIT] [-m {w,a}] [-v]

Fetch and update company data from Google search.

options:
  -h, --help            show this help message and exit
  -i INPUT_FILE, --input-file INPUT_FILE
                        File name containing the accounts
  -o OUTPUT_FILE, --output-file OUTPUT_FILE
                        File name to save updated data in
  -w WAIT, --wait WAIT  Time (seconds) to wait between each Google Search. Default is 5.
  -v, --verbose         Print debug log
```

# Example CSV
An example CSV-file would look like this
```
Company One
Company Two
Company Three
```

# Example output
```
./main.py --input-file accounts.csv --output-file updated.csv
Script started
Waiting for 5 seconds between each request to avoid bot detection
Parsing accounts.csv
Progress [0/2] - Fetching and processing data for Röchling SE & Co. KG
Progress [1/2] - Fetching and processing data for Heidelberger Druckmaschinen AG
Script execution finished
```


## License

[MIT](https://choosealicense.com/licenses/mit/)


## Contributing

Contributions and feedback are always welcome! Feel free to provide suggestions at any given time!