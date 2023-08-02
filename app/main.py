from clickhouse_adapter import ClickhouseAdapter
from file_watcher import FilesWatcher
from data_handler import DataHandler

if __name__ == '__main__':
    # Create an instance of ClickhouseAdapter with connection details
    click_house = ClickhouseAdapter('clickhouse', '8123', 'admin', '1234')

    # Connect to the ClickHouse server
    click_house.connect()

    # Initialize the ClickHouse database and tables
    click_house.db_init()

    # Create an instance of FilesWatcher
    file_watcher = FilesWatcher()

    # Create an instance of DataHandler and pass the ClickhouseAdapter instance to handle data insertion
    data_handler = DataHandler(click_house)

    # Start monitoring the 'input_files' directory for new files every 3 seconds
    # When new files are found, the DataHandler's 'on_new_files' method is called to handle the data
    file_watcher.fileWatcher('input_files', 3, data_handler.on_new_files)
