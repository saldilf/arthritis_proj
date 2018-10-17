#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
data_proc.py
Demo processing data from csv

Handles the primary functions
"""

import sys
import argparse
import numpy as np
import os

IO_ERROR = 2

SUCCESS = 0
DEF_DATA_FILE = "data.csv"

def warning(*objs):
    """Writes a message to stderr."""
    print("WARNING: ", *objs, file=sys.stderr)


def canvas(with_attribution=True):
    """
    Placeholder function to show example docstring (NumPy format)

    Replace this function and doc string for your own project

    Parameters
    ----------
    with_attribution : bool, Optional, default: True
        Set whether or not to display who the quote is from

    Returns
    -------
    quote : str
        Compiled string including quote and optional attribution
    """

    quote = "The code is but a canvas to our imagination."
    if with_attribution:
        quote += "\n\t- Adapted from Henry David Thoreau"
    return quote

def data_analysis(data_array):
    print(type(data_array))
    print(data_array)
    num_patients, num_days = data_array.shape

    data_stats = np.zeros((num_patients, 3))

    data_stats[:, 0] = np.mean(data_array, axis = 1)
    data_stats[:, 1] = np.max(data_array, axis = 1)
    data_stats[:, 2] = np.min(data_array, axis = 1)

    return data_stats
#   Find min, max, avg for each of given array- one line per patient
#   Parameters
#    ----------
#   data_array : numpy array of patient data
#
#   Returns
#    --------
#   data_stats : numpy array



def parse_cmdline(argv):
    """
    Returns the parsed argument list and return code.
    `argv` is a list of arguments, or `None` for ``sys.argv[1:]``.
    """
    if argv is None:
        argv = sys.argv[1:]

    # initialize the parser object:
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--csv_data_file", help="The location of the csv file with data to analyze",
                        default=DEF_DATA_FILE)
    #parser.add_argument("-n", "--no_attribution", help="Whether to include attribution",
    #                   action='store_false')
    args = None
    try:
        args = parser.parse_args(argv)
        args.csv_data = np.loadtxt(fname=args.csv_data_file, delimiter=',' )
    except IOError as e:
        warning("Problems reading file:", e)
        parser.print_help()
        return args, IO_ERROR

    return args, SUCCESS


def main(argv=None):
    args, ret = parse_cmdline(argv)
    if ret != SUCCESS:
        return ret
    data_stats = data_analysis(args.csv_data)
    base_out_fname = os.path.basename(args.csv_data_file)
    base_out_fname = os.path.splitext(base_out_fname)[0] + '_stats'
    out_fname = base_out_fname + '.csv'
    np.savetxt(out_fname, data_stats, delimiter=',')
    print("Wrote file: {}".format(out_fname))
    return SUCCESS  # success


if __name__ == "__main__":
    status = main()
    sys.exit(status)
