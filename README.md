# CorpCrawler
**A sales assistant for information gathering on corporations**

![CorpCrawler Header Image](image.png)

This python scripts automates searching Google for specific information on a list of provided corporations.

It is purely a terminal application developed to assist Account Managers and Sales Managers in automating information gathering tasks on their accounts. It automates this process as it can become a highly time consuming task that can easily be automated.

The scripts expects an input CSV-file (-i, --input-file) that contains the name of a corporation per each line (no header needed). It will then iterate through each account and based on the provided search keywords (-s, --search-keywords) it will fetch the information from Google. Lastly, it will create an output CSV-file (-o, --output-file), in which all the fetched information including sources will pe stored.

*Why does this even exist?* Experience over the years has proven over and over again that the information at hand is often outdated or highly inaccuarate and having up-to-date information about enterprises would require hours to days to find updated information. This script will ease this process as it collects relevant information including its source in an automated fashion, so you can execute it regularly, to ensure you have the most relevant and up-to-date information whenever you need it.

# Installation
To use the script, please make sure you are running Python3 and have GIT installed. Also, the solution is using the "googlesearch-python" module to effectively search and parse the Google results, so make sure to install all required dependencies.

**Here are the steps to install all dependencies and run the script:**
1. Clone this repo in your terminal: ```git clone git@github.com:nicolaswehmeyer/corpcrawler.git && cd corpcrawler```
1. OPTIONAL: Create a virtual environment: ```python3 -m venv venv```
2. OPTIONAL: Activate the virtual environment: ```source venv/bin/activate```
2. Install dependencies: ```pip3 install -r requirements.txt```
3. Make script executable: ```chmod +x app.py```
4. Now you are ready to run it from your terminal. Example:
```./app.py --input-file <FILE_NAME> --output-file <FILE_NAME> --search-keywords "Employee Count" "Headquarter"```

# Usage
Assuming we are storing a list of accounts in a CSV-file called accounts.csv and want to store the fetched information in a new CSV-file called updated.csv, **this would be the command to execute:**
```
./app.py --input-file accounts.csv --output-file updated.csv --search-keywords "Employee Count" "Headquarter"
```
**The script supports the following options:**
```
./app.py --help
usage: app.py [-h] -i INPUT_FILE -o OUTPUT_FILE [-w WAIT] [-d] -s SEARCH_KEYWORDS [SEARCH_KEYWORDS ...]

Fetch and update company data from Google search.

options:
  -h, --help            show this help message and exit
  -i INPUT_FILE, --input-file INPUT_FILE
                        File name containing the accounts
  -o OUTPUT_FILE, --output-file OUTPUT_FILE
                        File name to save updated data in
  -w WAIT, --wait WAIT  Time (seconds) to wait between each Google Search. Default is 5.
  -d, --debug           Print debug log messages
  -s SEARCH_KEYWORDS [SEARCH_KEYWORDS ...], --search-keywords SEARCH_KEYWORDS [SEARCH_KEYWORDS ...]
```

# Example input CSV file
An example CSV-file would look like this
```
Company Name One
Company Name Two
...
```

# Example command line output
```
./app.py -i accounts.csv -o updated.csv -s "Employee Count"                           
Script started - Press CTRL + C to abort
Reading input file accounts.csv and saving results to updated.csv
Waiting for 5 seconds between each search request to avoid bot detection
Will research the following keywords per each account: Employee Count
----------
Progress [1/2] - Fetching and processing data for Company Name One
Progress [2/2] - Fetching and processing data for Company Name Two
----------
Script execution finished
```

# Example CSV output file
```
name,employee_count,employee_count_src
Company Name One,"Companies ranked by number of employees. companies: 8,295 total employees count: 122,817,161 suggest/edit icon download icon. Rank by Market Cap Earnings ...",https://companiesmarketcap.com/largest-companies-by-number-of-employees/
Company Name Two,"13.02.2024 — Largest companies in the world based on revenues, by number of employees 2023 ... Walmart had about 2.1 million employees in 2023, the highest of ...",https://www.statista.com/statistics/264671/top-50-companies-based-on-number-of-employees/
```

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Contributing

Contributions and feedback are always welcome! Feel free to provide suggestions at any given time!