import csv

def load_data(path):
    """Loads data from csv file.

    :param path: Path to file.
    :returns: List of tuples containing the training data
    """
    data = []

    with open(path, 'r') as dt:
        d_csv = csv.reader(dt, delimiter=',')
        for row in d_csv:
            data.append((row[1],row[0]))

    return data[1:]
