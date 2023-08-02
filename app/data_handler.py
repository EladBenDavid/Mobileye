import os
import json
import uuid


class DataHandler:
    # Dictionary to store vehicle IDs
    vehicle_ids = {}

    def __init__(self, clickhouse):
        """
        Constructor for the DataHandler class.

        Parameters:
        - clickhouse: An instance of the ClickhouseAdapter class to handle data insertion to ClickHouse.
        """
        self.clickhouse = clickhouse

    def on_new_files(self, files_diff):
        """
        Process new JSON files and handle the data based on the filename.

        Parameters:
        - files_diff: A list of filenames representing the new JSON files in the 'input_files' directory.
        """
        for json_file_name in files_diff:
            if json_file_name.startswith('vehicles_status_'):
                # Handle JSON files containing vehicle status data
                with open(os.path.join('input_files', json_file_name)) as data:
                    self.handle_vehicles_status(json.load(data))
            elif json_file_name.startswith('objects_detection_'):
                # Handle JSON files containing objects detection data
                with open(os.path.join('input_files', json_file_name)) as data:
                    self.handle_objects_detection(json.load(data))
            else:
                # Drop files with unknown prefixes
                print(f'Dropping file {json_file_name}')

    def handle_vehicles_status(self, data):
        """
        Handle vehicle status data.

        Parameters:
        - data: A dictionary containing vehicle status data.
        """
        for vehicle_status in data['vehicle_status']:
            self.clickhouse.add_vehicle_status(vehicle_status)

    def handle_objects_detection(self, data):
        """
        Handle objects detection data.

        Parameters:
        - data: A dictionary containing objects detection events data.
        """
        for object_detection in data['objects_detection_events']:
            self.clickhouse.add_objects_detection(object_detection)
