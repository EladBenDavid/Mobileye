import os
from os import listdir
from os.path import isfile, join
import time

class FilesWatcher:
    # Function to return files in a directory
    def fileInDirectory(self, my_dir: str):
        """
        Returns a list of files in the specified directory.

        Parameters:
        - my_dir (str): The directory path to search for files.

        Returns:
        - only_files (list): A list of filenames in the directory.
        """
        if not os.path.exists(my_dir):
            # Create a new directory because it does not exist
            os.makedirs(my_dir)
        only_files = [f for f in listdir(my_dir) if isfile(join(my_dir, f))]
        return only_files

    # Function to compare two lists
    def listComparison(self, OriginalList: list, NewList: list):
        """
        Compares two lists and returns the differences.

        Parameters:
        - OriginalList (list): The original list to compare.
        - NewList (list): The new list to compare against.

        Returns:
        - differences_list (list): A list containing the items present in NewList but not in OriginalList.
        """
        differences_list = [x for x in NewList if x not in OriginalList] #Note if files get deleted, this will not highlight them
        return differences_list

    def fileWatcher(self, my_dir: str, poll_time: int, do_things_with_new_files):
        """
        Monitors a directory for new files and performs actions on new files.

        Parameters:
        - my_dir (str): The directory path to monitor for new files.
        - poll_time (int): The time interval in seconds between each check for new files.
        - do_things_with_new_files (function): A function to process the new files found.
        """
        while True:
            if 'watching' not in locals():  # Check if this is the first time the function has run
                previous_file_list = self.fileInDirectory(my_dir)
                watching = 1
                print(previous_file_list)

            time.sleep(poll_time)
            new_file_list = self.fileInDirectory(my_dir)
            file_diff = self.listComparison(previous_file_list, new_file_list)
            previous_file_list = new_file_list
            if len(file_diff) == 0: continue
            do_things_with_new_files(file_diff)
