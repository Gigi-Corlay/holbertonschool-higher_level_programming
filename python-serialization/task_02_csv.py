#!/usr/bin/python3

import csv
import json


def convert_csv_to_json(filename):
    """
    Convert a CSV file into a JSON file.

    Args:
        filename (str): Name of the CSV file to read.

    Returns:
        bool: True if conversion is successful, False otherwise.
    """
    try:
        data_list = []

        with open(filename, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                data_list.append(row)

        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data_list, json_file)

        return True
    except Exception:
        return False
