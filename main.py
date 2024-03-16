#!/usr/bin/env python3
import sys
import csv
import time
import logging
import requests
import argparse
from googlesearch import search

# Disable warnings from the requests library about SSL certificates
requests.packages.urllib3.disable_warnings()

# Constants for search keywords
EMPLOYEE_COUNT_KEYWORD = "Mitarbeiterzahl"
HQ_LOCATION_KEYWORD = "Hauptsitz"


def configure_logging(verbose):
    """Configures logging to include error and debug information."""
    if verbose:
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s - %(levelname)s - %(message)s')


def parse_arguments():
    """Parses command-line arguments for the script.

    Returns:
        argparse.Namespace: Parsed arguments with input file, output file, and wait time.
    """
    parser = argparse.ArgumentParser(
        description="Fetch and update company data from Google search.")
    parser.add_argument("-i", "--input-file", required=True,
                        help="File name containing the accounts")
    parser.add_argument("-o", "--output-file", required=True,
                        help="File name to save updated data in")
    parser.add_argument("-w", "--wait", type=int, default=5,
                        help="Time (seconds) to wait between each Google Search. Default is 5.")
    parser.add_argument("-v", "--verbose", default=False,
                        action="store_true", help="Print debug log")
    return parser.parse_args()


def google_search(token, keyword, wait_time):
    """Performs a Google search for a given token and keyword.

    Args:
        token (str): The company name to search for.
        keyword (str): The specific keyword to append to the search query.
        wait_time (int): Time to wait between requests to prevent bot detection.

    Returns:
        The first search result if successful, None otherwise.
    """
    try:
        search_results = search(
            f"{token} {keyword}", lang="de", advanced=True, num_results=1)
        for result in search_results:
            return result
    except Exception as e:
        logging.error(
            "Failed to search Google. Check your internet connection or try again later.")
        logging.debug(str(e))
        return None
    finally:
        time.sleep(wait_time)


def count_csv_rows(file_path):
    """Counts the number of rows in a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        int: Number of rows in the file.
    """
    try:
        with open(file_path, 'r', newline='') as file:
            return sum(1 for _ in file)
    except Exception as e:
        logging.error(f"Failed to open source file. Error: {e}")
        sys.exit(1)


def iterate_csv_file(input_file, output_file, wait_time):
    """Iterates over each row in the input CSV file, fetches data, and appends it to the output CSV file.

    Args:
        input_file (str): Path to the input CSV file.
        output_file (str): Path to the output CSV file.
        wait_time (int): Time to wait between requests to prevent bot detection.
    """
    print(f"----------")
    row_count = count_csv_rows(input_file)
    with open(input_file, 'r', newline='') as file, open(output_file, 'w', newline='') as outfile:
        fieldnames = ['name', 'employee_count',
                      'employee_count_src', 'hq_location', 'hq_location_src']
        reader = csv.DictReader(file, fieldnames=fieldnames)
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        for index, account in enumerate(reader):
            print(
                f"Progress [{index}/{row_count}] - Fetching and processing data for {account['name']}")
            employee_count_result = google_search(
                account['name'], EMPLOYEE_COUNT_KEYWORD, wait_time)
            hq_location_result = google_search(
                account['name'], HQ_LOCATION_KEYWORD, wait_time)
            if employee_count_result and hq_location_result:
                writer.writerow({
                    'name': account['name'],
                    'employee_count': employee_count_result.description,
                    'employee_count_src': employee_count_result.url,
                    'hq_location': hq_location_result.description,
                    'hq_location_src': hq_location_result.url
                })
            outfile.flush()
    print(f"----------")


def main():
    """Main function to execute the script."""
    try:
        args = parse_arguments()
        configure_logging(args.verbose)
        print("Script started - Press CTRL + C to abort")
        print(
            f"Reading input file {args.input_file} and saving results to {args.output_file}")
        print(
            f"Waiting for {args.wait} seconds between each request to avoid bot detection")
        iterate_csv_file(args.input_file, args.output_file, args.wait)
    except KeyboardInterrupt:
        print("Script execution aborted")
        sys.exit()
    except Exception as e:
        print(f"Script execution failed. {e}")
        sys.exit()
    print("Script execution finished")


if __name__ == "__main__":
    main()
