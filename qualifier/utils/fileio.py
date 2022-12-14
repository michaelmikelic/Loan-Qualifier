# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data

# define the save csv path needed for the app
def save_csv(csvpath, data, header = None):
    
    """""

    Args:
        csvpath (Path): The csv file path.
        data (list of lists): Data to be written to the csv file 
        header (list): optional header for the csv

    """

    with open(csvpath, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter = ',')
        if header:
            csvwriter.writerow(header)
        for row in data:
            csvwriter.writerow(row)