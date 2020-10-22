#!/home/stephen/miniconda3/bin/python
###############################################################################
# Author: Stephen Zhao
# App: rebrn
# Version: v0.1.1
# Last modified: 2020-10-11
# Description: Renames files by substituting a search pattern with a
#      replacement pattern, with datetime formatting and regex support.

import argparse
from datetime_matcher import DatetimeMatcher
import os
from pathlib import Path
import sys
from typing import List

IS_DEBUG = True

def debug(*args):
    if IS_DEBUG:
        print('[DEBUG]', *args)

# Prints a neat table
# shamelessly copied, courtesy of u/ParalysedBeaver, from:
# https://www.reddit.com/r/inventwithpython/comments/455qgj/automate_the_boring_stuff_chapter_6_table_printer/d3f5l3e/
def printTable(inputList: List[str]) -> None:
    # initialize the list "colWidths" with zeroes equal to the length of the input list
    colWidths = [0] * len(inputList)

    # iterate over the input list to find the longest word in each inner list
    # if its larger than the current value, set it as the new value
    for i in range(len(inputList)):
        for j in range(len(inputList[i])):
            if len(inputList[i][j]) > colWidths[i]:
                colWidths[i] = len(inputList[i][j])

    # assuming each inner list is the same length as the first, iterate over the input list
    # printing the x value from each inner list, right justifed to its corresponding value
    # in colWidths
    for x in range(len(inputList[0])):
        for y in range(len(inputList)):
            print(inputList[y][x].rjust(colWidths[y]), end = ' ')
        print('')

def parse_args(args: List[str]) -> any:
    argparser = argparse.ArgumentParser(
        description="Renames files by substituting a search pattern with a replacement \
            pattern, with datetime formatting and regex support.")
    argparser.add_argument('directory')
    argparser.add_argument('search_pattern')
    argparser.add_argument('replacement_pattern')
    return argparser.parse_args(args)

def main(args):
    # Parse arguments
    args = parse_args(args)

    # Get path to directory
    path_to_directory = Path(args.directory)

    # Handle directory path errors
    if path_to_directory.is_file():
        print("File input is still unsupported")
        exit(2)
    if not path_to_directory.is_dir():
        print("Invalid directory or file")
        exit(3)

    # Get list of files in directory
    pre_rename_files = list(file \
            for file in os.listdir(str(path_to_directory)) \
            if (path_to_directory / file).is_file())

    # Create a DatetimeMatcher to match regex with datetime formatting
    dtmatcher = DatetimeMatcher()

    # Generate new file names
    final_pre_rename_files = []
    final_post_rename_files = []
    for pre_rename_file in pre_rename_files:
        post_rename_file = dtmatcher.sub(args.search_pattern, args.replacement_pattern, pre_rename_file)
        if pre_rename_file != post_rename_file:
            final_pre_rename_files.append(pre_rename_file)
            final_post_rename_files.append(post_rename_file)

    # Get final length of files
    num_final_files = len(final_pre_rename_files)

    # Generate mapping
    files_oldtonew = dict((final_pre_rename_files[i], final_post_rename_files[i]) for i in range(num_final_files))

    # Make display table
    table_data = [final_pre_rename_files, ['-->' for i in range(num_final_files)], final_post_rename_files]

    # Early exit if no files to be renamed
    if num_final_files == 0:
        print("No renames to be done!")
        print("Exiting...")
        exit()

    # Display all files and pending rename results
    print("Pending renames to be done: ")
    printTable(table_data)

    # Confirm renaming operation
    is_input_invalid = True
    while is_input_invalid:
        confirm = input("Continue with file renaming? (y/n) ")
        if confirm == "n":
            print("Rename cancelled.")
            print("Exiting...")
            exit()
        if confirm == "y":
            is_input_invalid = False

    # Do renaming operation
    print("Processing rename...")
    for filename in final_pre_rename_files:
        try:
            os.rename(str(path_to_directory / filename), str(path_to_directory / files_oldtonew[filename]))
        except:
            print("An error occurred when trying to rename {}".format(filename))

    print("Rename done.")
    print("Exiting...")
    exit()

if __name__ == '__main__':
    main(sys.argv[1:])
