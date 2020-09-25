'''helpers for reading and structing data in the data directory'''

import os

__data_directory = os.path.join('.', 'project_euler', 'data')


def read_data(filename: str) -> str:
    '''reads the entire data file and returns it as a string'''
    with open(os.path.join(__data_directory, filename)) as contents:
        data = contents.read()
    return data
